from turtle import Turtle, Screen
import random
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.bgcolor("#27374D")
screen.listen()
snake = Snake()
food = Food()
current_Score = ScoreBoard()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move()
    current_Score.update_score()

    # Detect Collision
    if snake.head.distance(food) < 15:
        food.new_position()
        current_Score.increase_score()
screen.exitonclick()
