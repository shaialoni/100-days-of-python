import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
car_generation_counter = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if car_generation_counter % 6 == 0:
        car_manager.create_car()

    # detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            print("collision")
            scoreboard.game_over()
            game_is_on = False
    
    # check for level completion
    if player.is_at_finish_line():
        player.reset_position()
        scoreboard.level_up()
        car_manager.level_up()

    car_manager.move_left()
    car_generation_counter += 1


screen.exitonclick()