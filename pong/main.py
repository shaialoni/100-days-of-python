from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
scoreboard.update_scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
game_on = True
game_speed = 0.1

while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 330 and r_paddle.distance(ball) < 50 or ball.xcor() < -330 and l_paddle.distance(ball) < 50:
        ball.bounce_x()
    
    if ball.xcor() > 380:
        ball.ball_reset()
        scoreboard.l_point()
    
    if ball.xcor() < -390:
        ball.ball_reset()
        scoreboard.r_point()
    

screen.exitonclick()