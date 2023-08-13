from turtle import Turtle, Screen
import random
x_cors = [0, -20, -40]
turtle_list = []
for turtle_index in range(0,3):
 new_turtle = Turtle(shape="square")
 new_turtle.color("#E384FF")
 new_turtle.goto(x_cors[turtle_index], 0)
 turtle_list.append(new_turtle)
screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.bgcolor("#27374D")
screen.exitonclick()
