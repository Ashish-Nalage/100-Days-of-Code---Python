from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=600,height=600)  # setting up screen
screen.title("This is an snake game")
screen.bgcolor("black")

screen.tracer(0) # every thing after this is on canvs but aint visible


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")

game_is_on = True 

while game_is_on:
    screen.update() # canvas updated with 0.1 sec delay
    time.sleep(0.1)

    snake.move()
    
    if snake.head.distance(food) < 15: # detect collition with food
        scoreboard.score += 1
        food.refresh()
        snake.extend()
        scoreboard.update_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280: # detect collition with walls
        scoreboard.reset()
        scoreboard.update_score()
        snake.reset()

    for segment in snake.segments[1:]: # detect collition with snake body
        
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            scoreboard.update_score()
            snake.reset()

screen.exitonclick()