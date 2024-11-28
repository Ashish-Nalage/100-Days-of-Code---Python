import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
carmanager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.create_car()
    carmanager.move_cars()

    for car in carmanager.all_cars:  # detect collision with cars
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() > 280:   
        player.starting_position()  # respawn at starting point after reaching finish line
        carmanager.increase_speed() 
        scoreboard.level += 1
        scoreboard.update_level()

screen.exitonclick()
