from turtle import Turtle, Screen
import random

colors = ['red', 'blue', 'cyan', 'magenta', 'purple', 'green', 'darkgreen', 'dark orange', 'dark red', 'burlywood']

pummy = Turtle()
pummy.shape("turtle")

for i in range(3, 11):
    pummy.shapesize()
    pummy.color(random.choice(colors))
    for j in range(i):
        pummy.forward(100)
        pummy.left(360//i)