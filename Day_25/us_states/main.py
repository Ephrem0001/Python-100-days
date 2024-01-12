import turtle
import pandas

screen = turtle.Screen()
screen.title("U.s. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_List()

answer_state = screen.textinput(title="Guess the state", prompt="What's state's name")
print(answer_state)

if answer_state in all_states:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == answer_state]
    t.goto(state_data.x, state_data.y)
    t.write(state_data.state)
    
