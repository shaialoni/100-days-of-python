from turtle import Turtle, Screen, colormode
import random

colors = ['papaya whip', 'cornflower blue', 'dodger blue', 'aquamarine', 'spring green', 'gold', 'red', 'deep pink', 'blue2']
directions = [0, 90, 180, 270]
colormode(255)
tim = Turtle()
tim.shape("turtle")
tim.speed("fastest")
# print(tim.xcor())
# print(tim.ycor())
# tim.left(90)
# tim.penup()
# tim.forward(400)
# tim.left(90)
# tim.forward(50)
# tim.right(180)
# tim.pendown()

def color_generator():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    new_color = (r, g, b)
    return new_color


def run_shape(number_of_sides):
    angle_right_turn = 360 / number_of_sides
    for _ in range(number_of_sides):
        tim.forward(100)
        tim.right(angle_right_turn)

def random_move():
    tim.color(color_generator())
    tim.setheading(random.choice(directions))
    tim.forward(30)


def spirograph(size):
    for _ in range(int(360 / size)):
        tim.color(color_generator())
        tim.circle(100)
        tim.setheading(tim.heading() + size)


spirograph(int(input("enter size")))
# for _ in range(100):
#     random_move()   

 
# for shape_side_n in range(2,100):
#     run_shape(shape_side_n)


# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()




screen = Screen()
screen.exitonclick()