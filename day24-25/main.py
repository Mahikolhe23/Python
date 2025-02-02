import turtle
import pandas

# screen = turtle.Screen()
# screen.setup(width=600,height=600)
# screen.title('INDIA')
# image = 'india_map.gif'
# screen.addshape(image)
# turtle.shape(image)

data = pandas.read_csv('data.csv')

data = data.state.tolist()
new_data = []

for d in range(0,len(data)):
    if d % 2 ==0:
        new_data.append(data[d])

print(new_data)
df = pandas.DataFrame({'state':new_data})
df.to_csv('data.csv')

# screen.exitonclick()




