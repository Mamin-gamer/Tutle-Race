import turtle
import random
from matplotlib import pyplot as plt


win_x = 500
win_y = 500
FINISH = 200

played_games = 0

class Runner:
    def __init__(self, colour, x_position):
        self.colour = colour
        self.x_position = x_position
        self.turt = turtle.Turtle()
        self.turt.shape('turtle')
        self.turt.color(colour)
        self.turt.penup()
        self.turt.setpos(x_position, -200)
        self.turt.setheading(90)

    def move(self):

        self.turt.pendown()
        self.turt.fd(random.randint(1,10))

        return (self.turt.pos()[1], self.turt.color()[0])

def start():
    global played_games
    played_games +=1
    turtle.clearscreen()
    turtle.hideturtle()
    players = int(input('How many Turtles? \n'))
    if players > 9:
        print('too many Turtles')
        start()
    else:
        turtle.screensize(win_x,win_y)
        turtleList = []
        colours = ["red", "green", "blue", 'yellow', 'pink', 'orange', 'purple', 'black', 'grey']
        x_start = -25*(players-1)
        x_position = x_start
        for t in range(players):
            turtleList.append(Runner(colours[t], x_position))
            x_position+=50

    maximum = 0
    run = True
    while run:
        l = []
        for i in turtleList:
            y_cor, current_colour = i.move()
            if y_cor >=200:
                run = False
                print(f"the winner is --->{current_colour}<---")
                stats_write(current_colour)
                break


def stats_write(current_colour):
    with open('Turtle Race.txt', 'r') as file:
        old = [list(line.split()) for line in file]

    for l in old:
        if current_colour in l:
            l[1] = int(l[1]) + 1

    with open('Turtle Race.txt', 'w') as file:
        for line in old:
            file.write(str(line[0]) + ' ' + str(line[1])+ '\n')


def stats_read():
    colours =   []
    times_won = []
    with open('Turtle Race.txt', 'r') as file:
        old = [list(line.split()) for line in file]

    for row in old:
        colours.append(row[0])
        times_won.append(int(row[1]))


    plt.title('what colour won the most')
    plt.pie(times_won, colors = colours)
    plt.legend(times_won, title = 'colours', loc = 'center left', bbox_to_anchor = (1,0,0.5,1))
    plt.show()


start()


while True:
    print('-----------------------------------')
    user = input('Would you like to play again')
    if user == 'y':
        start()
    else:
        turtle.bye()
        user = input('WOuld u like to check statistics of all games?(y/n)')
        if user == 'y':

            stats_read()
        else:
            break
