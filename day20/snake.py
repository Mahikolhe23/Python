from turtle import Turtle , Screen
import random

snake = Turtle()
scree = Screen()

scree.screensize(200,200)
snake.speed('slow')

def snake_body():
    snake.hideturtle()
    snake.dot(15)
    snake.penup()
    
def move():
    while True:
        snake.forward(1)

def up_arrow():
    snake.setheading(90)
    snake_body()
    move()

def down_arrow():
    snake.setheading(270)
    snake_body()
    move()

def left_arrow():
    snake.setheading(180)
    snake_body()
    move()

def right_arrow():
    snake.setheading(0)
    snake_body()
    move()

scree.listen()
scree.onkey(key='w',fun=up_arrow)
scree.onkey(key='a',fun=left_arrow)
scree.onkey(key='d',fun=right_arrow)
scree.onkey(key='s',fun=down_arrow)















scree.exitonclick()
