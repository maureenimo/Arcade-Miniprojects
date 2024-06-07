from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
for colors in COLORS:
    colors
class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(colors)
        self.penup()
        self.shapesize(stretch_len=2, stretch_wid=1)
        y = random.randint(-280, 280)
        self.goto(STARTING_MOVE_DISTANCE, y)
        
        
    def move(self):
        self.forward(MOVE_INCREMENT)