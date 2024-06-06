from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("The Pong Game - A famous Arcade Game!")

paddle = Paddle()


screen.listen()
screen.keypress(paddle.up, "Up")




screen.exitonclick()