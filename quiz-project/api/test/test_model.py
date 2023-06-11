import pytest
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError

# this gives access to the database
pytestmark = pytest.mark.django_db


class TestQuestionModel:
    # functions to test the Question model
    def test_str_method(self, question_factory):

        # confirms the __str__ method for the Question model
        #  returns the right result
        x = question_factory(content='adams')
        assert x.__str__() == "1. adams"

    def test_content_unique_field(self, question_factory):

        # confirms that an error is raised
        # when the 'content' UNIQUE field
        #  restriction is violated
        question_factory(content="what?")
        with pytest.raises(IntegrityError):
            question_factory(content="what?")
           
    def test_username_max_length(self, question_factory):

        # confirms that an error is raised
        # when the maximum length of characters is exceeded
        #  for 'correct_option' field
        correct_option = "A" * 200
        obj = question_factory(correct_option=correct_option)
        with pytest.raises(ValidationError):
            obj.full_clean()


class TestQuizModel:
    # functions to test the Quiz model
    def test_str_method(self, quiz_factory):

        # confirms the __str__ method for the Quiz model
        #  returns the right result
        x = quiz_factory.create_batch(15)
        print(x[0].first_ans)
        assert x[0].__str__() == "paul_0"   

    def test_username_max_length(self, quiz_factory):

        # confirms that an error is raised
        # when the maximum length of characters is exceeded 
        # for 'username' field
        username = "A" * 200
        obj = quiz_factory(username=username)
        with pytest.raises(ValidationError):
            obj.full_clean()

    def test_username_unique_field(self, quiz_factory):

        # confirms that an error is raised
        # when the 'username' UNIQUE field
        #  restriction is violated
        quiz_factory(username="paul_1")
        with pytest.raises(IntegrityError):
            quiz_factory(username="paul_1")

    def test_email_unique_field(self, quiz_factory):

        # confirms that an error is raised
        # when the 'email' UNIQUE field
        #  restriction is violated
        quiz_factory(email="p@mail.com_1")
        with pytest.raises(IntegrityError):
            quiz_factory(email="p@mail.com_1")
        

    