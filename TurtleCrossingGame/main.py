import time
from turtle import Screen
from player import Player
from carmanager import CarManager
from scoreboard import Scoreboard

# Initialization
screen = Screen()
player = Player()
score = Scoreboard()
car_manager = CarManager()

# screen
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

screen.onkey(player.up, "Up")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()
    
    # finishes game
    if player.finish_line():
        player.refresh_game()
        car_manager.increase_speed()
        score.update_score()
        
        
    # collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_on = False
            score.game_over()
            
screen.exitonclick()