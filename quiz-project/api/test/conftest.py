import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient
from .factories import QuestionFactory, QuizFactory

register(QuestionFactory)
register(QuizFactory)


@pytest.fixture
def api_client():
    return APIClient