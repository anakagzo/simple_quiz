from django.urls import path, include
from .views import QuestionList,QuestionDetail

urlpatterns = [
    path('question', QuestionList.as_view()),
    path('question/<int:pk>', QuestionDetail.as_view())
]
