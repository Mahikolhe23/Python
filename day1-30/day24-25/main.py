import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=600,height=600)
screen.title('INDIA')
image = 'india_map.gif'
screen.addshape(image)
turtle.shape(image)

ans_text = screen.textinput(title='Guess the state',prompt='Whats the anathor state name ?').title()
data = pandas.read_csv('data.csv')
df = pandas.DataFrame(data=data)
all_states = df.state.tolist()

if ans_text in all_states:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == ans_text]
    print(state_data)
    t.goto(state_data.x.item(), state_data.y.item())
    t.write(ans_text)

screen.exitonclick()

