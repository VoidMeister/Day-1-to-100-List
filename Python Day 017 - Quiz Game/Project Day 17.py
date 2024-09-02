from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

#List of question objects, each being initialized with a question and an answer. Dictionary comes from question_data
question_bank = [
    #Question(q1, a1),
    #Question(q2, a2),
    #...
]

#question_1 = Question("text", "answer")
for dictionary in question_data:
    # Write a for loop ot iterate over the question_Data
    # Create a question object from each entry in question_data
    # Append each question object to the question_bank
    question = Question(dictionary["text"],dictionary["answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
