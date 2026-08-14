from django.urls import path

from .views import (
    QuestionListAPIView,
    QuizResultAPIView,
)

urlpatterns = [
    path(
        "questions/",
        QuestionListAPIView.as_view(),
        name="questions",
    ),

    path(
        "result/",
        QuizResultAPIView.as_view(),
        name="quiz-result",
    ),
]