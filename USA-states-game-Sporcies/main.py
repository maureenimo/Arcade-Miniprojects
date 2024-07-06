import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "USA-states-game-Sporcies/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("USA-states-game-Sporcies/50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name? ").title()

    all_states = data.state.to_list()
    
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]

        states_to_learn = pandas.DataFrame(missing_states)
        states_to_learn.to_csv("USA-states-game-Sporcies/states_to_learn.csv")
        break
        
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        matching_row = data[data.state == answer_state]
        t.goto(int(matching_row.x), int(matching_row.y))
        t.write(answer_state)
        
