from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

turtle_color = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []
race_is_on = False

user_bet = screen.textinput(title="Turtle race game",prompt="which turtle do you think will win")

y_position = [-100, -60, -20, 20, 60, 100]
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(turtle_color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    turtle_list.append(new_turtle)
    
if user_bet:
    race_is_on = True

while race_is_on:
    
    for turtle in turtle_list:
        
        if turtle.xcor() > 230:
            race_is_on =False
            winning_color = turtle.pencolor()
            
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner")
            else:
                print(f"You lost! The {winning_color} turtle is the winner")
        
        random_step = random.randint(0,10)
        turtle.forward(random_step)



screen.exitonclick()