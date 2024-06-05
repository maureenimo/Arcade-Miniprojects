from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_score()
        
    def track_score(self):
        self.write(f"Score: {self.score}", True, align="center", font=("Raleway",24,"bold"))
        
        
    def update_score(self):
        self.score += 1
        self.clear()
        self.update_score()
        