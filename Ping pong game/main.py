import turtle as t
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Creating our Screen
screen = t.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# Creating our Paddles
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with wall
    if ball.ycor() >= 285 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detecting R paddle misses
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.increase_score_l()

    # Detecting L paddle misses
    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.increase_score_r()
screen.exitonclick()
