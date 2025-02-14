import time
from turtle import Screen
from car_manager import CarManager
from scoreboard import Scoreboard
from player import Player

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Scoreboard()

game_is_on = True

screen.listen()

while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.onkey(player.go_up,'Up')

    car_manager.create_car()
    car_manager.move_car()
    
    # detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()

    # detect successfull crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        score.increase_level()

screen.exitonclick()
