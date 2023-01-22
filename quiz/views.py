from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, ListView, CreateView, DetailView, TemplateView
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from quiz.models import Question, Form, UserResponse, Marks_Of_User
from quiz.forms import UserResponseCreateForm
from quiz.utils import get_client_ip


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

    def post(self, request: HttpRequest, form_id: int, question_id: int):
        question: Question = get_object_or_404(Question, form=form_id, pk=question_id)
        form = Form.objects.filter(pk=form_id).first()
        next_questions = form.get_next_questions(question)
        print(next_question)

        data = request.POST.dict()
        print(request.POST, data)
        data["user_ip"] = get_client_ip(request)
        data["selected_options"] = request.POST.getlist("selected_options", [])
        user_response_form = UserResponseCreateForm(data)

        if user_response_form.is_valid():
            instance = user_response_form.save()
            
            next_question = next_questions.first()
            if next_question:
                print("Redirecting")
                return redirect(
                    "quiz:answer_form_question",
                    **{"form_id": form.pk, "question_id": next_question.pk},
                )
            else:
                return redirect("quiz:form_thanks", **{"form_id": form.pk})
        else:
            print(user_response_form.errors)
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

def bootstrap4_index(request):
    return render(request, "form_thanks.html", {})

class 
def home(request):
    score=50
    total =90
    if request.method == 'POST':
        print(request.POST)
        questions=Question.objects.all()
        score=50
        wrong=0
        correct=0
        total=0
        for q in questions: 
            total+=1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.correct_option ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'form_results.html',context)
    else:
        questions=Question.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'form_results.html',context)
# Create your views here.
