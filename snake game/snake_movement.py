import turtle as t
from snake import Snake
from food import Food
import scoreboard
import time


screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
snake_food = Food()
scores = scoreboard.Scoreboard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    if snake.all_turtles[0].distance(snake_food) < 15:
        scores.increase_score()
        snake_food.refresh_location()
        snake.extend()

    if snake.all_turtles[0].xcor() > 280 or snake.all_turtles[0].xcor() < -280 or snake.all_turtles[0].ycor() > 280 or snake.all_turtles[0].ycor() < -280:
        game_is_on = False
        scores.game_over()

    for turtles in snake.all_turtles[1:]:
        if snake.all_turtles[0].distance(turtles) < 10:
            game_is_on = False
            scores.game_over()

    # for turtle in range(1,len(snake.all_turtles)):
    #     pass
    #     if snake.all_turtles[0].distance(all_turtles[turtle]) < 10:
    #         game_is_on = False
    #         scores.game_over()



screen.exitonclick()

