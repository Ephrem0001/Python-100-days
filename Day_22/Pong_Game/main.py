from turtle import Screen
from paddle import Paddle
from ball import Ball
import random

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

x_ball = random.randint(0,350)
y_ball = random.randint(0,350)

ball_pos = Ball(x_ball, y_ball)

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
