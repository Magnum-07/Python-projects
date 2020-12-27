import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle racer")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.make_car()
    cars.move()

    if player.finish_line():
        scoreboard.increase_level()
        cars.increase_car_speed()

    for i in cars.all_cars:
        if player.distance(i) < 20:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()
