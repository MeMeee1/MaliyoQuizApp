from django.shortcuts import render
from .models import Quiz, Question, Answer, Result
from django.views.generic import ListView, TemplateView
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse


class QuizListView(ListView):
    model = Quiz 
    template_name = 'main.html'

def quiz_first_page (request,pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = quiz.get_questions()
    return render(request, 'newquiz.html',{'quiz':quiz, 'questions':questions})

def quiz_view(request, pk):
   quiz = Quiz.objects.get(pk=pk)
   questions = quiz.get_questions()
   paginator = Paginator(questions, 1) # Show 1 question per page
   page_number = request.GET.get('page')
   page_obj = paginator.get_page(page_number)
   return render(request, 'quiz.html', {'obj':quiz, 'page_obj': page_obj})

def quiz_data_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = []
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answers():
            answers.append(a.text)
        questions.append({str(q): answers})
    return JsonResponse({
        'data': questions,
        'time': quiz.time,
    })
def form_thanks_view(request,pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request, 'formthanks.html',{'quiz':quiz})
def save_quiz_view(request, pk):
    if request.is_ajax():
        questions = []
        data = request.POST
        data_ = dict(data.lists())

        data_.pop('csrfmiddlewaretoken')

        for k in data_.keys():
            print('key: ', k)
            question = Question.objects.get(text=k)
            questions.append(question)
        print(questions)

        user = request.user
        quiz = Quiz.objects.get(pk=pk)

        score = 0
        multiplier = 100 / quiz.number_of_questions
        results = []
        correct_answer = None

        for q in questions:
            a_selected = request.POST.get(q.text)

            if a_selected != "":
                question_answers = Answer.objects.filter(question=q)
                for a in question_answers:
                    if a_selected == a.text:
                        if a.correct:
                            score += 1
                            correct_answer = a.text
                    else:
                        if a.correct:
                            correct_answer = a.text

                results.append({str(q): {'correct_answer': correct_answer, 'answered': a_selected}})
            else:
                results.append({str(q): 'not answered'})
            
        score_ = score * multiplier
        Result.objects.create(quiz=quiz, user=user, score=score_)

        results.append({'score': score_})

        if score_ >= quiz.required_score_to_pass:
            return JsonResponse({'passed': True, 'results': results})
        else:
            return JsonResponse({'passed': False, 'results': results})
    else:
        return HttpResponse("This view only accepts AJAX requests.")




