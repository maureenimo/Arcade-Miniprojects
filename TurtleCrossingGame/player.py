from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("pink")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.move_speed = 0.1
        
    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
        
        
    def refresh_game(self):
        self.goto(STARTING_POSITION)
        self.move_speed = 0.09