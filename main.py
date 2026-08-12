from fastapi import FastAPI

app = FastAPI()

questions = [
    {
        "id": 1,
        "question": "What is the capital of India?",
        "options": ["Mumbai", "Delhi", "Kolkata", "Chennai"],
        "answer": "Delhi"
    },
    {
        "id": 2,
        "question": "Which language is used to create FastAPI applications?",
        "options": ["Python", "Java", "C++", "PHP"],
        "answer": "Python"
    },
    {
        "id": 3,
        "question": "What does API stand for?",
        "options": [
            "Application Programming Interface",
            "Advanced Programming Interface",
            "Application Python Interface",
            "Advanced Python Internet"
        ],
        "answer": "Application Programming Interface"
    }
]


@app.get("/")
def home():
    return {"message": "Quiz API is running"}


@app.get("/questions")
def get_questions():
    return questions


@app.get("/questions/{question_id}")
def get_question(question_id: int):

    for question in questions:
        if question["id"] == question_id:
            return question

    return {"message": "Question not found"}