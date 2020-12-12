import turtle as t
import random
is_game_on = False
screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Who do you think will win?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
for i in range(40,241,40):
    t_i = t.Turtle(shape="turtle")
    t_i.penup()
    t_i.color(colors[i//40 - 1])
    t_i.goto(x=-230, y=-100 + i)
    all_turtles.append(t_i)

if user_bet:
    is_game_on = True

while is_game_on:
    for turtles in all_turtles:
        if turtles.xcor() > 230:
            is_game_on = False
            winning_color = turtles.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} is the winner!")
            else:
                print(f"You lost! The {winning_color} is the winner!")
        rand_distance = random.randint(0,10)
        turtles.forward(rand_distance)

print(user_bet)
screen.exitonclick()
