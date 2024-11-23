from turtle import Screen, Turtle

screen = Screen()


snake = []
y_position = [0,-20,-40]

screen.setup(width=600,height=600)
screen.title("This is an snake game")
screen.bgcolor("black")

for turtle_index in range(3):
    new_turtle = Turtle("square")
    new_turtle.goto(0,y_position[turtle_index])
    snake.append(new_turtle)





screen.exitonclick()