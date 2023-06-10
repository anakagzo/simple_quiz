import pytest
import json

# this gives access to the database
pytestmark = pytest.mark.django_db


class TestQuestionListEndpoints:

    endpoint = '/api/question'

    def test_get_method(self, question_factory, api_client):
        # confirms that the endpoint returns a list of all the questions
        # when a GET request is made
        question_factory.create_batch(4)
        response = api_client().get(self.endpoint)
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 4

    def test_post_method(self, api_client):
        # confirms that the endpoint accepts a post request,
        # and creates a question in the database

        data = {"content": "drg?",
                "option1": "a",
                "option2": "b",
                "option3": " c",
                "option4": "d",
                "correct_option": "d"}

        response = api_client().post(self.endpoint, data)
        assert response.status_code == 201
        assert json.loads(response.content)['content'] == 'drg?'
            

class TestQuestionDetailEndpoints:    

    endpoint = '/api/question/'

    def test_get_method(self, question_factory, api_client):
        # confirms that the endpoint retrieves a question 
        # associated with the primary key
        #  when a GET request is made
        x = question_factory.create_batch(4)
        response = api_client().get(f"{self.endpoint}{x[0].pk}")
        assert response.status_code == 200
        print(json.loads(response.content))
        assert len(json.loads(response.content)) == 7

    def test_put_method(self, question_factory, api_client):
        # confirms that the endpoint accepts a put request,
        # and updates the question associated with the
        # primary key

        data = {"content": "drg?",
                "option1": "a",
                "option2": "b",
                "option3": " c",
                "option4": "d",
                "correct_option": "d"}

        database = question_factory.create_batch(4)
        
        response = api_client().put(f"{self.endpoint}{database[1].pk}", data)
        
        print(response.content)
        assert response.status_code == 202
        assert database[1].pk == json.loads(response.content)['id']
        assert json.loads(response.content)['content'] == 'drg?'

    def test_delete_method(self, question_factory, api_client):
        # confirms that the endpoint accepts a delete request,
        # and deletes the question associated with the
        # primary key

        x = question_factory.create_batch(4)
        
        response = api_client().delete(f"{self.endpoint}{x[1].pk}")
        
        assert response.status_code == 204
        
              
class TestQuizEndpoints:   

    endpoint = '/api/quiz'

    def test_get_method(self, question_factory, api_client):
        # confirms that the endpoint creates a quiz with six questions 
        question_factory.create_batch(15)
        response = api_client().get(self.endpoint)
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 6

    def test_post_method(self, quiz_factory, api_client):
        # confirms that the endpoint accepts a post request,
        # and stores in user details and answers

        data = {"username": "Ben",
                "email": "a@gmail.com",
                "first_ans": "bhun",
                "second_ans": "bt",
                "third_ans": "dh",
                "fourth_ans": "hv",
                "fifth_ans": "hv",
                "sixth_ans": "d"
                }

        response = api_client().post(self.endpoint, data)
        assert response.status_code == 202
        assert json.loads(response.content)['username'] == 'Ben'    