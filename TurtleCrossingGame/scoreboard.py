from turtle import Turtle

FONT = ("Raleway", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.track_score()
        
        
    def track_score(self):
        self.goto(-100,270)
        self.write(f"Level: {self.level}", align="center", font=FONT)
        
    def update_score(self):
        self.level +=1
        self.clear()
        self.track_score()
        
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=FONT)
        