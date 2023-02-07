from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "orange", "yellow", "green", "blue", "violet"]
all_turtles = []
is_race_on = False

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle would win the race? Enter a color: ")

posx = -230
posy = 160

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=posx, y=posy)
    posy -= 60
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            if turtle.pencolor() == user_bet:
                print(f"Congratulations! The {turtle.pencolor()} turtle has won!")
            else:
                print(f"Sorry, your turtle lost, the {turtle.pencolor()} turtle won.")

screen.exitonclick()