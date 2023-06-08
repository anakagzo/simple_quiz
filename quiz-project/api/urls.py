from django.urls import path, include
from .views import QuestionList,QuestionDetail,Quiz

urlpatterns = [
    path('question', QuestionList.as_view()),
    path('question/<int:pk>', QuestionDetail.as_view()),
    path('quiz', Quiz.as_view()),

]
