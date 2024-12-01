import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "Day-025/us_states_game/blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

answer = screen.textinput(title="Guess The State", prompt="What's another state's name: ")
tim = turtle.Turtle()
tim.penup()
tim.hideturtle()
tim.goto(236,104)
tim.write(f"{answer}", align="center", font=("Courier", 12, "normal"))





screen.exitonclick()