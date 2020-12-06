import turtle as t
import random


def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)



t.colormode(255)
timmy = t.Turtle()
timmy.speed("fastest")
for i in range(5,720,5):
    new_color = random_color()
    timmy.color(new_color)
    timmy.circle(100)
    timmy.setheading(i)

screen = t.Screen()
screen.exitonclick()
