from django.urls import path
from quiz import views

app_name = "quiz"

urlpatterns = [
    path("home/", views.bootstrap4_index, name="home"),
    path(
        "<int:form_id>/question/<int:question_id>/",
        views.AnswerQuestionView.as_view(),
        name="answer_form_question",
    ),
    path("<int:form_id>/thanks/", views.FormThanksView.as_view(), name="form_thanks"),
    path("<int:form_id>/", views.FormView.as_view(), name="form_main"),
]
