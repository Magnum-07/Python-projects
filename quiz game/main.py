from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []
for question in question_data:
    new_entry = Question(question["question"], question["correct_answer"])
    question_bank.append(new_entry)

quiz_brain = QuizBrain(question_bank)
while quiz_brain.still_has_questions() and quiz_brain.wanna_play:
    quiz_brain.next_question()


print("you've completed the quiz")
print(f"Your final score was {quiz_brain.score}/{quiz_brain.question_number}")