# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application.



## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```

## API Reference

### Getting Started
- Backend Base URL: http://127.0.0.1:5000/
- Frontend Base URL: http://localhost:3000

## Testing
To run the tests, run
```bash
dropdb trivia_test [<username>]
createdb trivia_test [<username>]
psql trivia_test [<username>] < trivia.psql
python test_flaskr.py
```


## Endpoints


- ### GET /categories
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: all categories
- Response Arguments:
    - dictionary of all `categories`

- sample: `curl http://127.0.0.1:5000/categories`

```
{
  "CATEGORIES": [
    {
      "id": 1,
      "type": "Science"
    },
    {
      "id": 2,
      "type": "Art"
    },
    {
      "id": 3,
      "type": "Geography"
    },
    {
      "id": 4,
      "type": "History"
    },
    {
      "id": 5,
      "type": "Entertainment"
    },
    {
      "id": 6,
      "type": "Sports"
    }
  ],
  "SUCCESS": true
}

```

- ### GET /questions
- Fetches a dictionary of questions
- Fetches a dictionary of categories
- Request Arguments: None
- Returns: 10 questions in each page
- Response Arguments:
    - dictionary `categories`
    - dictionary `questions`

sample: `curl http://127.0.0.1:5000/questions`

```
{
  "CATEGORIES": [
    {
      "id": 1,
      "type": "Science"
    },
    {
      "id": 2,
      "type": "Art"
    },
    {
      "id": 3,
      "type": "Geography"
    },
    {
      "id": 4,
      "type": "History"
    },
    {
      "id": 5,
      "type": "Entertainment"
    },
    {
      "id": 6,
      "type": "Sports"
    }
  ],
  "questions": [
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ],
  "success": true,
  "total": 25
}


```
- ### DELETE '/question/` <int:question_id> `'
- delete question by id
- Response Arguments:
    - `delete_id`
    - `message`
- Sample:
`curl http://127.0.0.1:5000/questions/15 -X DELETE`
```
{{
  "DELETE_ID": 15,
  "MESSAGE": "QUESTION successfully deleted",
  "SUCCESS": true
}
```
- ### POST /questions
- Create new question and COMMIT to the database

- Response Arguments:
     - `question`
    - `answer`
    - `difficulty`
    - `category
- Sample:
`curl -L -X POST 'http://127.0.0.1:5000/questions' -H 'Content-Type: application/json' --data-raw '{
    "question": "What is the most popular video-streaming engine used today?",
    "answer": "Youtube",
    "difficulty": 2,
    "category": 5
}'`
```
{
  "ANSWER": "Youtube",
  "CATEGORY": 5,
  "DIFFICULTY": 2,
  "QUESTION": "What is the most popular video-streaming engine used today?",
  "SUCCESS": true
}

```
- ### POST /questions/search
- Returns search result for questions
- Request Arguments: `searchTerm` search term
- Response Arguments: `current_category` and `totalQuestions
- Sample: `curl -L -X POST 'http://127.0.0.1:5000/questions/search' -H 'Content-Type: application/json' --data-raw '{ "searchTerm": "video-streaming"} `
```
{
  "current_category": 5,
  "questions": [
    {
      "answer": "Youtube",
      "category": 5,
      "difficulty": 2,
      "id": 31,
      "question": "What is the most popular video-streaming engine used today?"
    }
  ],
  "success": true,
  "totalQuestions": 1
}
```

- ### GET /categories/`<int:category_id>`/questions
- get questions based on category
- Response Arguments:
    - `questions` get maximum 10 questions
    - 'COUNT' number of related questions

- Sample: `curl http://127.0.0.1:5000/categories/4/questions`
```
{
  "COUNT": 4,
  "QUESTIONS": [
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Scarab",
      "category": 4,
      "difficulty": 4,
      "id": 23,
      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
    }
  ],
  "success": true
}


```



```

- ### POST /quizzes
- Fetches a unique question for the quiz on selected or unselected category
- Request Arguments:
   - `previous_questions` list of id of previous questions
   - `quiz_category` id of category
- Response Arguments:
   - `question` Random question
- Sample: `curl -L -X POST 'http://127.0.0.1:5000/quizzes' -H 'searchTerm: a' -H 'Content-Type: application/json' --data-raw '{
    "previous_questions": [
        3,
        4,
        10,
        12,
        11,
        5
    ],
    "quiz_category": "0"
}'`


```
{
  "question": {
    "answer": "Alexander Fleming",
    "category": 1,
    "difficulty": 3,
    "id": 21,
    "question": "Who discovered penicillin?"
  },
  "success": true
}
```


## Error Handling
Errors are returned in the following json format:
```
{
  "error": 400,
  "message": "bad request",
  "success": false
}
```
HTTP response status codes currently returned are:
- 404 : resource not found
- 422 : unprocessable
- 400 : bad request
- 500 : Internal Server Error
