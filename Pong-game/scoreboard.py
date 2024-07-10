from turtle import Turtle
FONT = ("Raleway", 20, "normal")
ALIGNMENT = "center"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        
        self.left_score = 0
        self.right_score = 0
        
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.goto(-100,200)
        self.write(f"{self.left_score}", align= ALIGNMENT, font=FONT)
        # right side
        self.goto(100,200)
        self.write(f"{self.right_score}", align= ALIGNMENT, font=FONT)
        
    def left_point(self):
        self.left_score +=1
        self.update_score()
        
    
    def right_point(self):
        self.right_score +=1
        self.update_score()
        