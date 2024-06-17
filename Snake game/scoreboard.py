from turtle import Turtle
FONT = ("Raleway",20,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.track_score()
        
    def track_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=FONT)
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.track_score()
        
    def update_score(self):
        self.score += 1
        self.track_score()
        