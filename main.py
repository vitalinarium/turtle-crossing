import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
cars = CarManager()
scoreboard = Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.car_move()
    screen.onkey(player.move, 'Up')
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.ycor() > player.finish_line:
        player.refresh_position()
        scoreboard.increase_score()
        cars.level_up()

screen.exitonclick()
