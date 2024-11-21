from turtle import Turtle, Screen

def forward():
    tim.forward(10)

def right():
    tim.right(10)

def backward():
    tim.backward(10)

def left():
    tim.left(10)

def clear():
    tim.penup()
    tim.clear()
    tim.home()
    tim.pendown()
    
tim = Turtle()
screen = Screen()

screen.listen()
screen.onkeypress(fun=forward,key="w")
screen.onkeypress(fun=backward,key="s")
screen.onkeypress(fun=right,key="a")
screen.onkeypress(fun=left,key="d")
screen.onkeypress(fun=clear,key="c")

screen.exitonclick()