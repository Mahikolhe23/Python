from food import Food
from turtle import Screen
from snake import Snake
from scoreboard import Scoreboard
import time

screen = Screen()

screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

game_is_on  = True

screen.listen()
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")


while game_is_on :
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collison with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.score_counter()
    
    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.xcor() < -280:
        game_is_on = False
        score.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            Scoreboard.game_over()
        
screen.exitonclick()
