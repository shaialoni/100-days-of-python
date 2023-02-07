from turtle import Turtle, Screen
screen = Screen()
tim = Turtle()
tim.speed("fastest")

def move_forward():
    tim.forward(10)

def move_back():
    tim.backward(10)

def turn_right():
    tim.right(10)

def turn_left():
    tim.left(10)

def clear_screen():
    screen.resetscreen()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()