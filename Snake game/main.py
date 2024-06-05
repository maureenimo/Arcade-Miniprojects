from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

# Initialize snake & food
snake= Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

# move snake
game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # Detect the food collision
    if snake.head.distance(food) < 15:
        food.refresh_food()
        scoreboard.update_score()
    

screen.exitonclick()








screen.exitonclick()