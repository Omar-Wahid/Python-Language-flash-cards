from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.goto(0, -250)
        self.shape("turtle")
        self.setheading(90)

    def move(self):
        self.goto(0, self.ycor() + MOVE_DISTANCE)

    def finish(self):
        self.goto(0, -250)
