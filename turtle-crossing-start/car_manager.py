from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.move_speed = - STARTING_MOVE_DISTANCE
        self.car_list = []
        self.lanes = []
        for lane in range(-200, 250):
            self.lanes.append(lane)
        self.lanes = self.lanes[::42]
        self.create_car()

    def create_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.up()
        new_car.color(random.choice(COLORS))
        new_car.goto(300, random.choice(self.lanes))
        self.car_list.append(new_car)

    def move(self):
        for car in self.car_list:
            car.goto(car.xcor()+self.move_speed, car.ycor())

    def speed_up(self):
        self.move_speed -= MOVE_INCREMENT
