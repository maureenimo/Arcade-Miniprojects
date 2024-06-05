from turtle import Turtle 
import random
# Drawing a square
t = Turtle()
for _ in range(4):
    t.forward(100)
    t.right(90)
    

# Drawing a triangle, square, pentagon, hexagon, octagon, nonagon & decagon

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        t.forward(100)
        t.right(angle)

for shape_side_n in range(3, 10):
    t.color(random.choice(colours))
    draw_shape(shape_side_n)
    
# Drawing random walks
directions = [0, 90, 180, 270]
t.pensize(20)
t.speed("fastest")

for _ in range(200):
    t.color(random.choice(colours))
    t.forward(30)
    t.setheading(random.choice(directions))

# Drawing a dashed line
for _ in range(20):
    t.forward(10)
    t.penup()
    t.forward(10)
    t.pendown()
