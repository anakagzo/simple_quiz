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
