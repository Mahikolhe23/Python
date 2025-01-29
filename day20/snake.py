from turtle import Turtle , Screen
import random

snake = Turtle()
scree = Screen()

scree.screensize(200,200)
snake.speed('slowest')

def snake_body():
    snake.pensize(15)
    snake.dot(15)
    snake.forward(15)
    snake.dot(15)

def up_arrow():
    current_heading = snake.heading()
    if current_heading == 0:
        snake.left(90)
        snake.forward(100)
    else:
        snake.right(90)
        snake.forward(100)    
def down_arrow():
    current_heading = snake.heading()
    if current_heading == 180:
        snake.left(90)
        snake.forward(100)
    else:
        snake.right(90)
        snake.forward(100)    
def left_arrow():
    current_heading = snake.heading()
    if current_heading == 90:
        snake.left(90)
        snake.forward(100)
    else:
        snake.right(90)
        snake.forward(100)    

def right_arrow():
    current_heading = snake.heading()
    if current_heading == 90:
        snake.right(90)
        snake.forward(100)
    else:
        snake.left(90)
        snake.forward(100)    
    
scree.listen()
scree.onkey(key='w',fun=up_arrow)
scree.onkey(key='a',fun=left_arrow)
scree.onkey(key='d',fun=right_arrow)
scree.onkey(key='s',fun=down_arrow)
snake_body()














scree.exitonclick()
