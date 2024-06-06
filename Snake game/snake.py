from turtle import Turtle
starting_positions = [(0,0),(-20,0), (-40,0)] 
move_distance = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]
       
    def create_snake(self):
        for position in starting_positions:
            self.add_snake_segment(position)
    
    # add segment
    def add_snake_segment(self, position):
        snake = Turtle('square')
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.snake_list.append(snake)
    
    def extend_snake(self):
        self.add_snake_segment(self.snake_list[-1].position())
    
    def move(self):
        for snake_num in range(len(self.snake_list)-1,0,-1):
            new_x = self.snake_list[snake_num -1].xcor()
            new_y = self.snake_list[snake_num -1].ycor()
            self.snake_list[snake_num].goto(new_x, new_y)
        self.head.forward(move_distance)
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    