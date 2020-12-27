import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
# SHAPES = ["turtle", "square", "circle"]


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = MOVE_INCREMENT

    def make_car(self):
        random_num = random.randint(1, 6)
        if random_num == 1:
            car = Turtle("square")
            car.penup()
            car.color(random.choice(COLORS))
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.goto(300, random.randint(-250, 250))
            self.all_cars.append(car)

    def move(self):
        for i in self.all_cars:
            i.backward(self.car_speed)

    def increase_car_speed(self):
        self.car_speed += MOVE_INCREMENT
