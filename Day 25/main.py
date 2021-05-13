import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
# reading csv data
data = pd.read_csv('50_states.csv')
states = data["state"].to_list()

guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missed_states_list = []
        for i in states:
            if i not in guessed_states:
                missed_states_list.append(i)

        missed_states_dict = {"states": missed_states_list}
        df = pd.DataFrame(missed_states_dict)
        df.to_csv("missed_states.csv")
        break
    elif answer_state in states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
    else:
        print("not in this")
# Getting mouse click event





screen.mainloop()
