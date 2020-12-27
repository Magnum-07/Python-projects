from turtle import Turtle, Screen
import random
colors = ['red', 'blue', 'cyan', 'magenta', 'purple', 'green', 'darkgreen', 'dark orange', 'dark red', 'burlywood']

pummy = Turtle()
screen = Screen()
screen.bgcolor("black")
pummy.shape("turtle")
pummy.pensize(5)
pummy.speed(10)
directions = [0, 90, 180, 270]

# TODO 2:- Make the turtle randomly walk
#
for i in range(1000):
    pummy.color(random.choice(colors))
    pummy.forward(20)
    pummy.setheading(random.choice(directions))

screen.exitonclick()
