from turtle import Turtle , Screen
import random

tom = Turtle()
screen = Screen()
screen.colormode(255)
tom.speed('fastest')

def get_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

def draw_circle(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tom.circle(100)
        tom.color(get_color())
        tom.setheading(tom.heading() + size_of_gap)

draw_circle(10)








screen.exitonclick()

