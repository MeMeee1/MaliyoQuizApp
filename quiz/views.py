from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, ListView, CreateView, DetailView, TemplateView
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from quiz.models import Question, Form, UserResponse
from quiz.forms import UserResponseCreateForm
from quiz.utils import get_client_ip


class AnswerQuestionView(View):
    def get(self, request: HttpRequest, form_id: int, question_id: int):
        question: Question = get_object_or_404(Question, form=form_id, pk=question_id)
        form = Form.objects.filter(pk=form_id).first()
        next_questions = form.get_next_questions(question)
        return render(
            request,
            "answer_question.html",
            context={
                "form": form,
                "question": question,
                "next_questions": next_questions,
            },
        )

    def post(self, request: HttpRequest, form_id: int, question_id: int):
        question: Question = get_object_or_404(Question, form=form_id, pk=question_id)
        form = Form.objects.filter(pk=form_id).first()
        next_questions = form.get_next_questions(question)
        

        data = request.POST.dict()
       
        data["user_ip"] = get_client_ip(request)
        data["selected_options"] = request.POST.getlist("selected_options", [])
        user_response_form = UserResponseCreateForm(data)

        if user_response_form.is_valid():
            instance = user_response_form.save()
            
            next_question = next_questions.first()
            if next_question:
                
                return redirect(
                    "quiz:answer_form_question",
                    **{"form_id": form.pk, "question_id": next_question.pk},
                )
            else:
                return redirect("quiz:form_thanks", **{"form_id": form.pk})
        else:
           
            return render(
                request,
                "answer_question.html",
                context={
                    "form": form,
                    "question": question,
                    "next_questions": next_questions,
                    "form_errors": user_response_form.errors,
                },
            )


class FormView(View):
    def get(self, request: HttpRequest, form_id: int) -> HttpResponse:
        form: Form = get_object_or_404(Form, pk=form_id)
        form_questions = form.get_ordered_questions()
        return render(
            request,
            "form_main.html",
            context={"form": form, "form_questions": form_questions},
        )


class FormThanksView(TemplateView):
    template_name = "form_thanks.html"

class FormNoTimeView(TemplateView):
    template_name = "form_time_over.html"

class ShowFirstQuestionView(View):
    def get(self, request: HttpRequest, form_id: int, question_id: int):
        question: Question = get_object_or_404(Question, form=form_id, pk=question_id)
        form = Form.objects.filter(pk=form_id).first()
        
        return render(
            request,
            "answer_question.html",
            context={
                "form": form,
                "question": question,
                
            },
        )
class ResultView(View):
    def get(self, request: HttpRequest, form_id: int):
        form = get_object_or_404(Form, id=form_id)
        questions = form.questions.all()
        score = 0
        for question in questions:
            correct_option = question.get_correct_option()
            user_answer = request.POST.get(question.id)
            if user_answer == correct_option.value:
                score += question.score_amount
        return render(request, 'form_results.html', {'score': score})
def bootstrap4_index(request):
    return render(request, "form_thanks.html", {})



# Create your views here.
