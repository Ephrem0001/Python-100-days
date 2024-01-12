import turtle
import pandas

screen = turtle.Screen()
screen.title("U.s. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

answer_state = screen.textinput(title="Guess the state", prompt="What's state's name")
print(answer_state)
