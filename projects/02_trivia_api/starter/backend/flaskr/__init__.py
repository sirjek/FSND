import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def paginate(request, questions, QUESTIONS_PER_PAGE):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
    questions = [question.format() for question in questions]
    current = questions[start:end]
    return current



def create_app(test_config=None):
  # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app, supports_credentials=True, resources={r"/api/*": {"origins": "*"}})


    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,PATCH,OPTIONS')
        return response

    '''
    @TODO:
    Create an endpoint to handle GET requests \
    for all available categories.
    '''
    @app.route('/categories')
    def Categories():
        try:
            categories = {}
            category = Category.query.all()
            list = paginate(request, category, QUESTIONS_PER_PAGE)
            return jsonify({
                'SUCCESS': True,
                'CATEGORIES': list
            })

        except Exception:
            abort(500)

    '''
    @TODO:
    Create an endpoint to handle GET requests for questions,
    including pagination (every 10 questions).
    This endpoint should return a list of questions,
    number of total questions, current category, categories.
    '''

    @app.route('/questions')
    def question():
        try:
            questions = Question.query.all()
            total = len(questions)
            category = Category.query.all()
            list = paginate(request , questions, QUESTIONS_PER_PAGE)
            current_category = [c.format() for c in category]
            return jsonify({
                'success': True,
                'CATEGORIES': current_category,
                'questions': list,
                'total': total
            })

        except:
            abort(404)




    '''
    @TODO:
    Create an endpoint to DELETE question using a question ID.

    TEST: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page.
    '''
    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def deleteQuestion(question_id):
        try:
            question = Question.query.filter_by(id=question_id).delete()
            return jsonify({
                'SUCCESS': True,
                'DELETE_ID': question_id,
                'MESSAGE': "QUESTION successfully deleted"
            })

        except:
            abort(422)



    '''
    @TODO:
    Create an endpoint to POST a new question,
    which will require the question and answer text,
    category, and difficulty score.

    TEST: When you submit a question on the "Add" tab,
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.
    '''
    @app.route('/questions', methods=['POST'])
    def createQuestions():
        new =''
        new = request.get_json()
        question = new.get('question')
        answer = new.get('answer')
        difficulty = new.get('difficulty')
        category = new.get('category')


        try:
            create = Question(question = question, answer = answer, difficulty = difficulty, category = category)
            create.insert()
            return jsonify({
                'SUCCESS': True,
                'QUESTION': question,
                'CATEGORY': category,
                'DIFFICULTY': difficulty,
                'ANSWER': answer

            })

        except:
            abort(422)
    '''
    @TODO:
    Create a POST endpoint to get questions based on a search term.
    It should return any questions for whom the search term
    is a substring of the question.

    TEST: Search by any phrase. The questions list will update to include
    only question that include that string within their question.
    Try using the word "title" to start.
    '''
    @app.route('/questions/search', methods=['POST'])
    def searchQuestions():
        try:
            page = request.args.get('page', 1, type=int)
            start = (page - 1) * 10
            end = start + 10
            searchTerm = request.get_json()
            search_term_lower = search_term.get('searchTerm', '').lower()
            questions = Question.query.all()
            count = 0
            data = []
            for question in questions:
                if search_term_lower in question.question:
                    count += 1
                    data.append(question.format())
            return jsonify({
                'success': True,
                'questions': data[start:end],
                'total_questions': count,
                'current_category': 'test'
            })
        except:
            abort(404)

    '''
    @TODO:
    Create a GET endpoint to get questions based on category.

    TEST: In the "List" tab / main screen, clicking on one of the
    categories in the left column will cause only questions of that
    category to be shown.
    '''
    @app.route('/categories/<int:category_id>/questions', methods=['GET'])
    def getQuestions(category_id):
        try:
            questions = Question.query.filter_by(category=category_id).all()
            link = paginate(request, questions, QUESTIONS_PER_PAGE)
            count = 0
            for question in questions:
                count+=1
            return jsonify({
                'success': True ,
                'QUESTIONS': link,
                'COUNT': count
            })

        except:
            abort(404)


    @app.route('/quizzes', methods=["POST"])
    def quiz():
        quizData = request.get_json()
        previous_questions = quizData.get('previous_questions', '')
        quiz_category = quizData.get('quiz_category', '')
        if ((quiz_category is None) or (previous_questions is None)):
            abort(400)
        category_id = quiz_category['id']
        if category_id == 0:
            questions = Question.query.all()
        else:
            questions = Question.query.filter_by(
                    category=category_id).all()

        def getRandomQuestions():
            randomQuestions = questions[random.randint(0, len(questions)-1)]
            if randomQuestions.id in previous_questions:
                return getRandomQuestions()
            else:
                return randomQuestions
        nextQ = getRandomQuestions()
        return jsonify({
                'success': True,
                'question': nextQ.format()
        })




    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
      "SUCCESS": False,
      "ERROR": 404,
      "MESSAGE": "resource not found"
      }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
      "SUCCESS": False,
      "ERROR": 422,
      "MESSAGE": "unprocessable"
      }), 422

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
      "SUCCESS": False,
      "ERROR": 400,
      "MESSAGE": "bad request"
      }), 400

    @app.errorhandler(500)
    def bad_request(error):
        return jsonify({
      "SUCCESS": False,
      "ERROR": 500,
      "MESSAGE": "Internal Server Error"
      }), 500




    return app
