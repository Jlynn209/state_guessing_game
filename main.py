import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S State Game")
img = "./us-states-game-start/blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50", prompt="What's another state's name?").title()

    data = pandas.read_csv("./us-states-game-start/50_states.csv")

    all_states = data.state.to_list()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
            new_data = pandas.DataFrame(missing_states)

            new_data.to_csv("states_to_learn.csv")

        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        row = data[data.state == answer_state]
        t.goto(int(row.x), int(row.y))
        t.write(answer_state)






screen.onscreenclick()
