from turtle import Turtle
FONT = ("Raleway", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        
        self.track_score()
        
    def track_score(self):
        self.goto(-180, 260)
        self.write(f"Level: {self.level}", align="center", font=FONT)
        
        
    def update_score(self):
        self.level += 1
        self.clear()
        self.track_score()
        
        
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=FONT)
        