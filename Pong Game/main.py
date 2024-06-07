from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Screen setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("The Pong Game - A famous Arcade Game!")
# Turns off animation
screen.tracer(0)

# Initialize
right_paddle = Paddle((350,0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


# Events from screen
screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "Left")
screen.onkey(left_paddle.down, "s")

# while loop starts
game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall and bounce
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    # Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect right paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()
    
    # Detect left paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()

screen.exitonclick()