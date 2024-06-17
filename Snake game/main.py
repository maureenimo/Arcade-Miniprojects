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
game_not_over = True
while game_not_over:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # Detect the food collision
    if snake.head.distance(food) < 15:
        food.refresh_food()
        snake.extend_snake()
        scoreboard.update_score()
    
    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor()< -280:
        scoreboard.reset()
        snake.reset()
        
    # Detect collision with tail
    for segment in snake.snake_list[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()




