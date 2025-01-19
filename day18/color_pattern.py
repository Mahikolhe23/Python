from turtle import Turtle, Screen
import random

turtle = Turtle()
screen = Screen()
turtle.pensize(15)
screen.colormode(255)
turtle.speed('fastest')

def get_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    new_color = (r,g,b)
    return new_color

def draw_point_table(n):
    turtle.penup()
    turtle.setheading(225)
    turtle.forward(300)
    turtle.setheading(0)
    for _ in range(10):
        for _ in range(10):
            turtle.pendown()
            turtle.dot(15,get_color())
            turtle.penup()
            turtle.forward(50)
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)

draw_point_table(5)
screen.exitonclick()