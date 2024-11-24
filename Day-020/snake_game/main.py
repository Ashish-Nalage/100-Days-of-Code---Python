from turtle import Screen, Turtle
import time
from snake import Snake

screen = Screen()

screen.setup(width=600,height=600)
screen.title("This is an snake game")
screen.bgcolor("black")


screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")

game_is_on = True 
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    

screen.exitonclick()