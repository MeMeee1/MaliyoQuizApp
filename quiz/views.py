from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView, CreateView, DetailView
from django.http import HttpRequest, HttpResponse
from quiz.models import Question, Form, UserResponse


class AnswerQuestionView(View):
    def get(self, request: HttpRequest, form_id: int, question_id: int):
        question: Question = get_object_or_404(Question, form=form_id, pk=question_id)
        form = Form.objects.filter(pk=form_id).first()
        next_questions = form.get_next_questions(question)
        print(next_questions)
        return render(
            request,
            "answer_question.html",
            context={
                "form": form,
                "question": question,
                "next_questions": next_questions,
            },
        )

    def post(self, request):
        ...


class FormView(View):
    def get(self, request: HttpRequest, form_id: int) -> HttpResponse:
        form: Form = get_object_or_404(Form, pk=form_id)
        form_questions = form.get_ordered_questions()
        print(form_questions)
        return render(
            request,
            "form_main.html",
            context={"form": form, "form_questions": form_questions},
        )


def bootstrap4_index(request):
    return render(request, "index.html", {})


# Create your views here.
