import random
from turtle import Turtle, Screen

dummy = Turtle()

for a in range(1,5):
    turn = a + 2
    angle = 360 / turn
    length = 100
    color = ['red','green','blue','black','purple']
    dummy.color(random.choice(color))
    while turn > 0 :
        dummy.forward(length)
        dummy.right(angle)
        turn -= 1




screen = Screen()
screen.exitonclick()
