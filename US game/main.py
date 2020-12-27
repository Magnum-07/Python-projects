import turtle
import pandas as pd
guessed_answers = []

# Creating screen
screen = turtle.Screen()
screen.title("US STATES GAME")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data["state"].tolist()
number_of_states = len(data.state)

for i in range(number_of_states):
    user_answer = screen.textinput(title=f"{len(guessed_answers)}/{number_of_states}Guess the state?", prompt="Guess the next state name?").title()
    state_details = data[data.state == user_answer]
    if user_answer == "Break":
        not_guessed = []
        for state in data.state:
            if state not in guessed_answers:
                not_guessed.append(state)

        data_study = pd.DataFrame(not_guessed)
        data_study.to_csv("Study.csv")
        screen.bye()
    if user_answer in guessed_answers:
        print("You have already guessed the answer!")
    elif len(state_details) == 0:
        print("Galat")
    else:
        guessed_answers.append(user_answer)
        new_t = turtle.Turtle()
        new_t.penup()
        new_t.hideturtle()
        new_t.goto(int(state_details.x), int(state_details.y))
        new_t.write(arg=f"{user_answer}")


# print(f"You guessed these answers {guessed_answers}")

# states that was not guessed

