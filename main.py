from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import random
import time

paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()

screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

screen.listen()
screen.onkey(paddle_r.right_up, "Up")
screen.onkey(paddle_r.right_down, "Down")
screen.onkey(paddle_l.left_up, "w")
screen.onkey(paddle_l.left_down, "s")

scoreboard = Scoreboard()

time_s = 0.1
game_is_on = True
while game_is_on:
    time.sleep(time_s)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    elif ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        time_s -= 0.001
        ball.bounce_x()

    elif ball.xcor() > 400:
        scoreboard.clear()
        scoreboard.score_increase_r()
        ball.home()

    elif ball.xcor() < -400:
        scoreboard.clear()
        scoreboard.score_increase_l()
        ball.home()
    if scoreboard.score_left == 5 or scoreboard.score_right == 5:
        ball.home()
        scoreboard.finish()
        game_is_on = False











screen.exitonclick()