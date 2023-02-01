from django.urls import path
from .views import (
    QuizListView,
    quiz_view,
    quiz_data_view,
    save_quiz_view,
    quiz_first_page,
    form_thanks_view,
    
)

app_name = 'newquiz'

urlpatterns = [
    path('<pk>/thanks/', form_thanks_view, name="formthanks"),
    path('', QuizListView.as_view(), name="main"),
   
    path('<pk>/', quiz_view, name='quiz-view'),
    path('<pk>/save/', save_quiz_view, name='save-view'),
    path('<pk>/data/', quiz_data_view, name='quiz-data-view'),
    path('q/quiz/<pk>/',quiz_first_page, name='first-view'),
    
]