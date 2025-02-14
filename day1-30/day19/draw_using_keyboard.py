from turtle import Turtle,Screen
import random

turtle = Turtle()
screen = Screen()

def move_forward():
    turtle.forward(50)

def move_backward():
    turtle.backward(50)

def clockwise():
    turtle.circle(50)
    
def anti_clockwise():
    turtle.setheading(180)
    turtle.circle(50)
def clear_screen():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()

screen.listen()
screen.onkey(key='w',fun=move_forward)
screen.onkey(key='s',fun=move_backward)
screen.onkey(key='a',fun=clockwise)
screen.onkey(key='d',fun=anti_clockwise)
screen.onkey(key='c',fun=clear_screen)


screen.exitonclick()
