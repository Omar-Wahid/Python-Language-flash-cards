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
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkey(player.move, "Up")

game_is_on = True
loop = 0

while game_is_on:
    time.sleep(0.1)
    loop += 1
    if player.ycor() > 280:
        player.finish()
        # scoreboard.level_up()
        car_manager.speed_up()
    if loop > 6:
        loop = 0
        car_manager.create_car()
    for car in car_manager.car_list:
        if player.distance(car) < 20:
            game_is_on = False
    car_manager.move()
    
    screen.update()
