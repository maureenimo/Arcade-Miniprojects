from turtle import Screen
from snake import Snake
import time
# screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()

# Initialize snake
snake= Snake()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

snake.create_snake()
# move snake
game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    











screen.exitonclick()