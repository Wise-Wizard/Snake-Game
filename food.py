from turtle import Turtle
import random
from scoreboard import ScoreBoard


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.shape("circle")
        self.color("#865DFF")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        x_value = random.randint(-280, 280)
        y_value = random.randint(-280, 250)
        self.goto(x_value, y_value)

    def new_position(self):
        new_x_value = random.randint(-280, 280)
        new_y_value = random.randint(-280, 280)
        self.goto(new_x_value, new_y_value)
