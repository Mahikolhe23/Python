from turtle import Turtle, Screen
import random

screen = Screen()
tim = Turtle()
tim.pensize(15)
screen.colormode(255)
tim.speed('fastest')
def get_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

angle = [0,90,180,270]
for _ in range(50):
    tim.color(get_color())
    tim.forward(30)
    tim.setheading(random.choice(angle))

screen = Screen()
screen.exitonclick()

