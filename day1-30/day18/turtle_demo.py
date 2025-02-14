from turtle import Turtle, Screen

dummy = Turtle()

dummy.color('red')
dummy.shape('turtle')

for _ in range(4):
    dummy.forward(100)
    dummy.right(90)



screen = Screen()
screen.exitonclick()
