from turtle import Turtle
FONT = ("Raleway",20,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.track_score()
        
    def track_score(self):
        self.write(f"Score: {self.score}", align="center", font=FONT)
        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)
        
    def update_score(self):
        self.score += 1
        self.clear()
        self.track_score()
        