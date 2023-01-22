import string
from datetime import date, datetime

from django.urls import reverse, reverse_lazy
from django.db import models
from django.db.models import QuerySet, F
from django.forms import ValidationError
from django.db.models.constraints import UniqueConstraint


class QuestionTypes(models.TextChoices):
    RADIO = "RADIO"
    CHECKBOX = "CHECKBOX"
    COLOR = "COLOR"
    DATE = "DATE"
    DATETIME = "DATETIME"


class Question(models.Model):
    
    display_text = models.CharField(
        max_length=500,
        help_text="Actual question text that gets displayed to the user.",
    )
    question_type = models.CharField(
        max_length=20,
        choices=QuestionTypes.choices,
        help_text="Determines the type of question, and the corresponding HTML element that gets created",
    )
    # TODO: Support config like min_date, max_selected_items etc
    extra_parameters = models.JSONField(
        blank=True,
        default=dict,
        help_text="Can be used to store extra data for validating different question types",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    correct_option = models.ForeignKey(
        "quiz.QuestionOption", related_name="correct_option", on_delete=models.CASCADE, default = 1
    )
    class Meta:
        verbose_name = "question"
        verbose_name_plural = "questions"
        ordering = ["-last_updated_at", "-created_at"]

    def __str__(self) -> str:
        return f"{self.display_text}"[:50]

    @property
    def is_radio(self):
        return self.question_type == QuestionTypes.RADIO

    @property
    def is_checkbox(self):
        return self.question_type == QuestionTypes.CHECKBOX

    @property
    def is_color(self):
        return self.question_type == QuestionTypes.COLOR

    @property
    def is_date(self):
        return self.question_type == QuestionTypes.DATE

    @property
    def is_datetime(self):
        return self.question_type == QuestionTypes.DATETIME


class QuestionOption(models.Model):
    
    display_text = models.CharField(
        max_length=250, help_text="Actual option text that gets displayed to the user"
    )
    value = models.CharField(
        max_length=250, help_text="The value that gets stored in the DB"
    )
    question = models.ForeignKey(
        "quiz.Question",
        on_delete=models.CASCADE,
        related_name="options",
        related_query_name="option",
    )

    class Meta:
        verbose_name = "question option"
        verbose_name_plural = "question options"

    def __str__(self) -> str:
        return f"{self.display_text}"


class Form(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    questions = models.ManyToManyField(
        "quiz.Question",
        through="quiz.FormQuestion",
        related_name="forms",
        related_query_name="form",
    )
    max_fill_attempts = models.PositiveIntegerField(
        default=1,
        help_text="The number of times a particular IP Address can fill a form",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "form"
        verbose_name_plural = "forms"
        ordering = ["-last_updated_at", "-created_at"]

    def get_absolute_url(self):
        return reverse_lazy("quiz:form_main", kwargs={"form_id": self.pk})

    def __str__(self) -> str:
        return f"{self.title}"

    def get_ordered_questions(self) -> QuerySet[Question]:
        return (
            Question.objects.filter(form_question__form=self)
            .order_by("form_question__order")
            .prefetch_related()
        )

    def get_next_questions(self, question: Question) -> QuerySet[Question]:
        q = (
            Question.objects.filter(pk=question.pk)
            .annotate(order=F("form_question__order"))
            .first()
        )
        return Question.objects.filter(form_question__form=self).filter(
            form_question__order__gt=q.order
        )


class FormQuestion(models.Model):
    question = models.ForeignKey(
        "quiz.Question", related_name="form_question", on_delete=models.CASCADE
    )
    form = models.ForeignKey(
        "quiz.Form", related_name="form_question", on_delete=models.CASCADE
    )
    order = models.PositiveIntegerField()

    class Meta:
        # TODO: Ensure question can only be added to form once
        ...


class UserResponse(models.Model):
    form = models.ForeignKey(
        "quiz.Form",
        on_delete=models.CASCADE,
        help_text="Form for which the response was recorded",
    )
    question = models.ForeignKey(
        "quiz.Question",
        on_delete=models.CASCADE,
        help_text="The question the user is answering",
    )
    selected_options = models.ManyToManyField(
        "quiz.QuestionOption",
        blank=True,
        help_text="Selected option if user is limited to a specific set of options",
    )
    user_value = models.CharField(max_length=500, help_text="The user provided value")

    user_ip = models.GenericIPAddressField(
        help_text="The IP Address of the user device"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "user response"
        verbose_name_plural = "user reponses"
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.user_ip} - {self.question}"

    def save(self, *args, **kwargs) -> None:
        # self._validate_user_response()
        return super().save(*args, **kwargs)

    def _validate_user_response(self):
        """
        Ensure the user's input is valid for our question.
        Input should be of the expected type and format
        """
        if self.question.is_radio:
            if not (self.selected_options.count() == 1):
                raise ValidationError(
                    {
                        "question_option": "User must select a single option for Radio Questions/Inputs"
                    }
                )

        elif self.question.is_checkbox:
            ...

        elif self.question.is_color:
            self.user_value = self.user_value.strip()
            if not (
                (self.user_value[0] == "#")
                and all([c in string.hexdigits for c in self.user_value[1:]])
                and len(self.user_value) == 7
            ):
                raise ValidationError(
                    {
                        "user_value": "Invalid color provided. Color must be in hexadecimal format e.g '#eeffcc'"
                    }
                )

        elif self.question.is_date:
            self.user_value = self.user_value.strip()
            try:
                date.fromisoformat(self.user_value)
            except Exception as errors:
                raise ValidationError({"user_value": f"Invalid date: {errors}"})

        elif self.question.is_datetime:
            self.user_value = self.user_value.strip()
            try:
                datetime.fromisoformat(self.user_value)
            except Exception as errors:
                raise ValidationError({"user_value": f"Invalid datetime: {errors}"})

        else:
            raise ValidationError(
                {
                    "message": "Failed to validate user input for question of unknown type"
                }
            )

    def select_option(self, option: QuestionOption):
        self.selected_options.add(option)
        self.user_value = option.value

    def can_edit_entry(self) -> bool:
        no_previous_responses = UserResponse.objects.filter(
            user_ip=self.user_ip, question=self.question
        ).count()
        if no_previous_responses >= self.question.form.max_attempts:
            return False
        return True
class Marks_Of_User(models.Model):
    question = models.ForeignKey("quiz.Question", on_delete=models.CASCADE)
    score = models.FloatField()
    def __str__(self):
        return str(self.question)