from turtle import Turtle, Screen
import random

screen = Screen()
turtles = []
color = ['red','black','green','blue','purple']
user_input = screen.textinput(title='Make Your bet', prompt='Who will be winner ? Enter the color')

def get_turtle_list():
    for number in range(1,6):
        new_turtle = f'turtle_{number}'
        new_turtle = Turtle()
        new_turtle.color(color[number-1])
        new_turtle.penup()
        new_turtle.setheading(225)
        new_turtle.forward(300)
        new_turtle.shape('turtle')
        turtles.append(new_turtle)

def set_turtle_position():
    for num in range(1,5):
        turtle = turtles[num]
        turtle.setheading(90)
        turtle.forward(num * 50)
        turtle.setheading(0)
    turtle_1 = turtles[0]
    turtle_1.setheading(0)

def start_race():
    count = 600
    turtle_score= [0,0,0,0,0]
    while count > 0 :
        for num in range(0,len(turtles)):
            turtle = turtles[num]
            random_number = random.randint(1,3) * 10 
            turtle.forward(random_number)
            turtle_score[num] += random_number
        count -= 30
    max = 0
    index = 0 
    for n in range(0,len(turtle_score)):
        if max < turtle_score[n] :
            max = turtle_score[n]
            index = n    
    winner = color[index]
    if winner == user_input:
        print('You Won')
    else:
        print('You Loose')    

get_turtle_list()
set_turtle_position()
start_race()

screen.exitonclick()