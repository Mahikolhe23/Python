from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width = 800,height = 600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with top wall
    if ball.ycor() > 280 or ball.ycor() < - 280:
        ball.bounce_y() 

    # collision with paddle
    if ball.distance( r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:        
        ball.bounce_x()

    # detect when right paddle miss 
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # detect when left paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()





screen.exitonclick()

