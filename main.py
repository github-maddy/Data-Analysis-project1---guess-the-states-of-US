import turtle as t
import pandas

screen = t.Screen()
pen = t.Turtle()
file = "50_states.csv"
screen.title("Guess the states")
screen.addshape("blank_states_img.gif")
pen.shape("blank_states_img.gif")

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guess_states = []


while len(guess_states)<51:
    guess = screen.textinput(title=f"{len(guess_states)}/50 guess a state", prompt="Enter another state").title()

    if guess == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guess_states:
                missing_states.append(state)
        print_states = pandas.DataFrame(missing_states)
        print(print_states)
        break



    if guess in all_states:
        pen2 = t.Turtle()
        guess_states.append(guess)
        pen2.penup()
        pen2.hideturtle()
        answer = data[data.state == guess]
        pen2.goto(int(answer.x),int(answer.y))
        pen2.write(guess)


def get_mouse_click(x,y):
    print(x,y)


screen.onclick(get_mouse_click)
t.mainloop()




