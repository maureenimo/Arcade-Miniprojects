from turtle import Screen
from carmanager import CarManager
from player import Player
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Initializes
car = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")


game_on = True
while game_on:
    time.sleep(player.move_speed)
    screen.update()
    car.move()
    
    # if turtle hits top edge, refreshes
    if player.ycor() > 280:
        player.refresh_game()
        # scoreboard.update_score()
    
    # If car hits player
    # if player.distance(car) < 15:
    #     scoreboard.game_over()
    
    
    
    
    
    
    
screen.exitonclick()