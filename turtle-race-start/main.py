from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="your bet", prompt="chose your color ")
colors = ["red", "blue", "green", "yellow", "purple", "magenta"]
all_turtles = []
y_pos = -70
race_on = False

for index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    all_turtles.append(new_turtle)
    new_turtle.up()
    new_turtle.color(colors[index])
    new_turtle.goto(x=-230, y=y_pos)
    y_pos += 30

tim = Turtle()
tim.up()
tim.hideturtle()
tim.goto(225, -80)
tim.down()
tim.goto(225, 100)

if user_bet:
    race_on = True

while race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 220:
            race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print("you won")
            else:
                print("you lose")

        speed = random.randint(0, 5)
        turtle.fd(speed)



screen.exitonclick()
