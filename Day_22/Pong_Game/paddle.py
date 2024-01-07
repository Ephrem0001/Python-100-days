from turtle import Turtle


class Paddle:
    def __init__(self, x_value, y_value):
        self.x_value = x_value
        self.y_value = y_value

    def paddle_move_direction(self):
        paddle = Turtle()
        paddle.shape("square")
        paddle.color("white")
        paddle.shapesize(stretch_wid=5, stretch_len=1)
        paddle.penup()
        paddle.goto(self.x_value, self.y_value)
