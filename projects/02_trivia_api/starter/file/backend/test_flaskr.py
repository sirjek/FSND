import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass


    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """

    def test_categories(self):
        res = self.client().get('/categories')
        data = json.loads(new.data)
        self.assertEqual(new.status, 200)
        self.assertEqual(data['SUCCESS'], True)
        self.assertEqual(data['CATEGORIES'])


    def test_questions(self):
        res = self.client().get('/questions')
        data = json.loads(new.data)
        self.assertEqual(new.status, 200)
        self.assertEqual(data['SUCCESS'], True)
        self.assertEqual(data['CATEGORIES'])
        self.assertEqual(data['QUESTIONS'])

    def test_error_questions(self):
        res = self.client().get('/questions?page=10000000')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['SUCCESS'], False)
        self.assertEqual(data['MESSAGE'], 'resource not found')



    def test_delete_question(self):
        id= 2                                              #id for pass the id to delete the record has same the id
        #code for test DELETE methods  that send DELETE reaquset to /example/<int:id>
        res = self.client().delete('/questions/{}'.format(id))
        data = json.loads(res.data)                             #featch the delete response

        self.assertEqual(res.status_code, 200)                  #confirm the status response code is 200 is mean Ok
        self.assertEqual(data['SUCCESS'], True)
        self.assertEqual(data['MESSAGE'], "Question successfully deleted")
        self.assertTrue(data['DELETE_ID'])



    def test_delete_error(self):
                                                                    #code for test DELETE methods  that send DELETE reaquset to /example/<int:id>
        res = self.client().delete('/questions/{}'.format(1))
        data = json.loads(res.data)                             #fetch the delete response

        self.assertEqual(res.status_code, 422)                  #confirm the status response code is 422 is mean unprocessable
        self.assertEqual(data['SUCCESS'], False)
        self.assertEqual(data['MESSAGE'], "unprocessable")




    def test_search_in_questions(self):
        data_json={
            'searchTerm': 'Which is the only team to play in every soccer World Cup tournament?'
        }
        res = self.client().post('/questions/search', json=data_json)   #code for test POST methods  that send POST reaquset to /example
        data = json.loads(res.data)                                     #fetch the post response
        self.assertEqual(res.status_code, 200)                          #confirm the status response code is 200 is mean Ok
        self.assertIsNotNone(data['QUESTIONS'])


    def test_get_questions_on_category(self):
        res = self.client().get('/categories/{}/questions'.format(2))  #code for test GET methods  that send Get reaquset to /example
        data = json.loads(res.data)                                     #featch the GET response

        self.assertEqual(res.status_code, 200)                          #confirm the status response code is 200 is mean Ok
        self.assertEqual(data['success'], True)
        self.assertEqual(data['categories'], 'Art')
        self.assertTrue(data['categories'])
        self.assertTrue(data['totalQuestions'])
        self.assertTrue(data['questions'])


    def test_get_erorr_questions_on_category(self):
        '''
        Test get question on category with data not exit in db
        :pass
        '''
        res = self.client().get('/categories/{}/questions'.format(10))  #code for test GET methods  that send Get reaquset to /example
        data = json.loads(res.data)                                     #featch the GET response

        self.assertEqual(res.status_code, 404)                          #confirm the status response code is 404 is mean resource not found
        self.assertEqual(data['success'], False)


    def test_get_all_quizzes(self):
        '''
        Test play quizzes on all categores with data in db
        :pass
        '''
        data_json={
            	"previous_questions": [3, 4, 10, 12, 11, 5],
	            "quiz_category": {"type": "click", "id": 0}
        }
        res = self.client().post('/quizzes', json=data_json)    #code for test POST methods  that send POST reaquset to /example
        data = json.loads(res.data)                             #featch the post response
        self.assertEqual(res.status_code, 200)                  #confirm the status response code is 200 is mean Ok
        self.assertEqual(data['success'], True)
        self.assertIsNotNone(data['question'])
        self.assertNotEqual(data['question']['id'], 3)
        self.assertNotEqual(data['question']['id'], 12)


    def test_get_quizzes_in_category(self):
        '''
        Test play quizzes on category with data in db
        :pass
        '''
        data_json={
            	"previous_questions": [3, 4, 10, 12, 11, 5],
	            "quiz_category": {"type": "Art", "id": 2}
        }
        res = self.client().post('/quizzes', json=data_json)    #code for test POST methods  that send POST reaquset to /example
        data = json.loads(res.data)                             #featch the post response
        self.assertEqual(res.status_code, 200)                  #confirm the status response code is 200 is mean Ok
        self.assertEqual(data['success'], True)
        self.assertIsNotNone(data['question'])
        self.assertNotEqual(data['question']['id'], 3)
        self.assertNotEqual(data['question']['id'], 12)

    def test_error_quiz_category_not_found_quizzes(self):
        '''
        Test play quizzes on none (no data) category with data in db
        :pass
        '''
        data_json={
            	"previous_questions": [3, 4, 10, 12, 11, 5],
	            "quiz_category": None
        }
        res = self.client().post('/quizzes', json=data_json)    #code for test POST methods  that send POST reaquset to /example
        data = json.loads(res.data)                             #featch the post response
        self.assertEqual(res.status_code, 400)                  #confirm the status response code is 400 is mean bad request
        self.assertEqual(data['success'], False)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
