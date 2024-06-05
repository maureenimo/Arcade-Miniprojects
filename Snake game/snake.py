from turtle import Turtle
starting_positions = [(0,0),(-20,0), (-40,0)] 
move_distance = 20

class Snake:
    def __init__(self):
        self.snake_list = []
        self.create_snake()
       
    def create_snake(self):
        for position in starting_positions:
            snake = Turtle('square')
            snake.color("white")
            snake.penup()
            snake.goto(position)
            self.snake_list.append(snake)
    
    def move(self):
        for snake_num in range(len(self.snake_list)-1,0,-1):
            new_x = self.snake_list[snake_num -1].xcor()
            new_y = self.snake_list[snake_num -1].ycor()
            self.snake_list[snake_num].goto(new_x, new_y)
        self.snake_list[0].forward(move_distance)
        
    def up(self):
        pass
    
    def down(self):
        pass
        
    def left(self):
        pass
        
    def right(self):
        pass