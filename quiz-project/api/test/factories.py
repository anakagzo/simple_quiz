import factory

from api.models import Question, Quiz


# create a factory class to supply the test  database with records
class QuestionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Question

    content = factory.sequence(lambda n: "name_%d" % n)
    option1 = factory.sequence(lambda n: "obi_%d" % n)
    option2 = factory.sequence(lambda n: "ada_%d" % n)
    option3 = factory.sequence(lambda n: "ben_%d" % n)
    option4 = factory.sequence(lambda n: "toby_%d" % n)
    correct_option = factory.sequence(lambda n: "toby_%d" % n)


# create a factory class to supply the test  database with records
class QuizFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Quiz

    username = factory.sequence(lambda n: "paul_%d" % n)
    email = factory.sequence(lambda n: "p@mail.com_%d" % n)
    first_ans = factory.sequence(lambda n: "one_%d" % n)
    second_ans = factory.sequence(lambda n: "two_%d" % n)
    third_ans = factory.sequence(lambda n: "three_%d" % n)
    fourth_ans = factory.sequence(lambda n: "four_%d" % n)
    fifth_ans = factory.sequence(lambda n: "five_%d" % n)
    sixth_ans = factory.sequence(lambda n: "six_%d" % n)
    
