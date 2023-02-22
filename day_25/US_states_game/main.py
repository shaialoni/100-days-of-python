import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
game_is_on = True
guessed_states = set()

while game_is_on:
    answer_state = screen.textinput(title=f"Guess the State {len(guessed_states)}/50", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        print("in exit", answer_state)
        missed_states = [state for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missed_states.append(state)
        df = pandas.DataFrame(missed_states)
        df.to_csv("missed_states.csv")
        break
    #print("answer is - ", answer_state)
    if answer_state in all_states:
        state_data = data[data.state == answer_state]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
        #print(state_data.state)
        guessed_states.add(answer_state)
    
    if len(guessed_states) == len(all_states):
        game_is_on = False

    print(guessed_states, len(guessed_states))

screen.exitonclick()