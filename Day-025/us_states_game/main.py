import turtle
import pandas

guessed_states_list = []
missing_states = []
no_of_states_guessed = 0

# set up the screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "Day-025/us_states_game/blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)


# create dataframe of states 
df = pandas.read_csv("Day-025/us_states_game/50_states.csv")
all_states_list = df.state.to_list()
 
while no_of_states_guessed < 50:

    # user input
    answer_state = screen.textinput(title=f"{no_of_states_guessed}/50 State's Guessed", prompt="What's another state's name: ")
    answer_state = answer_state.title()

    # adding exit option for user when stuck and create csv to learn missing states
    if answer_state == "Exit":
        for state in all_states_list:
            if state not in guessed_states_list:
                missing_states.append(state)
        states_to_learn = pandas.DataFrame(missing_states)
        states_to_learn.to_csv("Day-025/us_states_game/states_to_learn.csv")
        break

    if answer_state in all_states_list and answer_state not in guessed_states_list:
        state_row = df[df.state == answer_state]

        # initiate turtle for writing states name text on screen
        text = turtle.Turtle()
        text.penup()
        text.hideturtle()

        # extract x and y coordinates from respective state
        x = state_row.x.item()
        y = state_row.y.item()

        # print name on map
        text.goto(x,y)
        text.write(f"{answer_state}")

        # keeping track of guessed states
        guessed_states_list.append(answer_state)
        no_of_states_guessed += 1

