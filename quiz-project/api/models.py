from django.db import models


class Question(models.Model):
    content = models.TextField(unique=True)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.pk) + ". " + self.content


class Quiz(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    first_ans = models.CharField(max_length=100, null=True)
    second_ans = models.CharField(max_length=100, null=True)
    third_ans = models.CharField(max_length=100, null=True)
    fourth_ans = models.CharField(max_length=100, null=True)
    fifth_ans = models.CharField(max_length=100, null=True)
    sixth_ans = models.CharField(max_length=100, null=True)
    seventh_ans = models.CharField(max_length=100, null=True)
    eighth_ans = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return str(self.username)
    