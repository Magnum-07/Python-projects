class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        self.wanna_play = True

    def still_has_questions(self):
        length = len(self.question_list)
        return self.question_number < length

    def next_question(self):
        question_text = self.question_list[self.question_number]
        self.question_number += 1
        userInput = input(f"Q.{self.question_number}: {question_text.text}. (True or False)?: ").lower()
        self.check_answer(userInput, question_text.answer.lower())

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("You got it right!")
            self.score += 1
        elif user_answer == "exit":
            self.wanna_play = False
        else:
            print("You are wrong!")
            print(f"The correct answer is {correct_answer}")
        print(f"Current Score: {self.score}/{self.question_number}\n")