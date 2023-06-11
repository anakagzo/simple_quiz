from django.shortcuts import get_object_or_404
from .models import Question
from rest_framework import views, status
from rest_framework.response import Response
from .serializers import QuestionSerializer, QuizSerializer
from random import randint


class QuestionList(views.APIView):
    def get(self, request, format=None):
        # gets a list of all the questions
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # creates a new question
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDetail(views.APIView):
    def get(self, request, pk, format=None):
        # gets the details of a question using the primary key
        question = get_object_or_404(Question.objects.all(), pk=pk)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        # updates a question
        question = get_object_or_404(Question.objects.all(), pk=pk)
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        # deletess a question
        question = get_object_or_404(Question.objects.all(), pk=pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Quiz(views.APIView):
    def get(self, request, format=None):
        # creates a quiz using the questions stored in the database
        # The quiz contains 8 different questions
        question_list = []
        questions = Question.objects.all()

        count = len(questions)
        num = randint(0, count)
        for int in range(num, num + 8):
            if int < count:
                question_list.append(questions[int])
            else:
                int = int % count
                question_list.append(questions[int])

        serializer = QuestionSerializer(question_list, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # takes in user details and answers
        serializer = QuizSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
