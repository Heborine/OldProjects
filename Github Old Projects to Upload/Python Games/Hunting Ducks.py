import turtle
import random
from turtle import Screen
import time

sc = turtle.Screen()
sc.setup(500, 500)


def my_handler(x, y):
    global score
    print("Click_Check")
    screen.onclick(None)  # unbind the handler
    # handle the request.  This could be a set of statements to position a turtle.

    cord1 = x
    cord2 = y

    statement_printer = str(score)
    crosshair.goto(x, y)
    screen.onclick(my_handler)  # bind the handler again
    if ducks[0][0].isvisible():
        if crosshair.pos() == ducks[0][0].pos():
            ducks[0][0].hideturtle()
            if ducks[0][1].isvisible():
                score = 100
                statement_printer = str(score)
                score_writer.clear()
                score_writer.write(statement_printer, move=False, align="right", font=("Arial", 20, "normal"))
            else:
                score += 100
                statement_printer = str(score)
                score_writer.clear()
                score_writer.write(statement_printer, move=False, align="right", font=("Arial", 20, "normal"))
        elif ducks[0][0].xcor() - 10 <= cord1 and ducks[0][0].xcor() + 10 >= cord1 \
                and ducks[0][0].ycor() + 10 >= cord2 and ducks[0][0].ycor() - 10 <= cord2:
            ducks[0][0].hideturtle()
            if ducks[0][1].isvisible():
                score = 100
                statement_printer = str(score)
                score_writer.clear()
                score_writer.write(statement_printer, move=False, align="right", font=("Arial", 20, "normal"))
            else:
                score += 100
                statement_printer = str(score)
                score_writer.clear()
                score_writer.write(statement_printer, move=False, align="right", font=("Arial", 20, "normal"))
        else:
            pass
    if ducks[0][1].isvisible():
        if crosshair.pos() == ducks[0][1].pos():
            ducks[0][1].hideturtle()
            if ducks[0][0].isvisible():
                score = 100
                statement_printer = str(score)
                score_writer.clear()
                score_writer.write(statement_printer, move=False, align="right", font=("Arial", 20, "normal"))
            else:
                score += 100
                statement_printer = str(score)
                score_writer.clear()
                score_writer.write(statement_printer, move=False, align="right", font=("Arial", 20, "normal"))
        elif ducks[0][1].xcor() - 10 <= cord1 and ducks[0][1].xcor() + 10 >= cord1 \
                and ducks[0][1].ycor() + 10 >= cord2 and ducks[0][1].ycor() - 10 <= cord2:
            ducks[0][1].hideturtle()
            if ducks[0][0].isvisible():
                score = 100
                statement_printer = str(score)
                score_writer.clear()
                score_writer.write(statement_printer, move=False, align="right", font=("Arial", 20, "normal"))
            else:
                score += 100
                statement_printer = str(score)
                score_writer.clear()
                score_writer.write(statement_printer, move=False, align="right", font=("Arial", 20, "normal"))
        else:
            pass
    # starts at 1 since a zero set was used first/above
    starter = 1
    while starter < 60:
        if ducks[starter][0].isvisible():
            if crosshair.pos() == ducks[starter][0].pos():
                ducks[starter][0].hideturtle()
                score += 100
                statement_printer = str(score)
                score_writer.clear()
                score_writer.write(statement_printer, move=False, align="right", font=("Arial", 20, "normal"))
            elif ducks[starter][0].xcor() - 10 <= cord1 and ducks[starter][0].xcor() + 10 >= cord1 \
                    and ducks[starter][0].ycor() + 10 >= cord2 and ducks[starter][0].ycor() - 10 <= cord2:
                ducks[starter][0].hideturtle()
                score += 100
                statement_printer = str(score)
                score_writer.clear()
                score_writer.write(statement_printer, move=False, align="right", font=("Arial", 20, "normal"))
            else:
                pass
        if ducks[starter][1].isvisible():
            if crosshair.pos() == ducks[starter][1].pos():
                ducks[starter][1].hideturtle()
                score += 100
                statement_printer = str(score)
                score_writer.clear()
                score_writer.write(statement_printer, move=False, align="right", font=("Arial", 20, "normal"))
            elif ducks[starter][1].xcor() - 10 <= cord1 and ducks[starter][1].xcor() + 10 >= cord1 \
                    and ducks[starter][1].ycor() + 10 >= cord2 and ducks[starter][1].ycor() - 10 <= cord2:
                ducks[starter][1].hideturtle()
                score += 100
                statement_printer = str(score)
                score_writer.clear()
                score_writer.write(statement_printer, move=False, align="right", font=("Arial", 20, "normal"))
            else:
                pass
        starter += 1


def move_duck(x, y, my_duck):
    if my_duck.xcor() < x and my_duck.ycor() < y:
        my_duck.shape(duck_right)
        if my_duck.xcor() < x - 5 and my_duck.ycor() < y - 5:
            my_duck.setposition(my_duck.xcor() + 5, my_duck.ycor() + 5)
        else:
            my_duck.setposition(my_duck.xcor() + 1, my_duck.ycor() + 1)
    elif my_duck.xcor() > x and my_duck.ycor() > y:
        my_duck.shape(duck_left)
        if my_duck.xcor() > x + 5 and my_duck.ycor() > y + 5:
            my_duck.setposition(my_duck.xcor() - 5, my_duck.ycor() - 5)
        else:
            my_duck.setposition(my_duck.xcor() - 1, my_duck.ycor() - 1)
    elif my_duck.xcor() < x and my_duck.ycor() > y:
        my_duck.shape(duck_right)
        if my_duck.xcor() < x - 5 and my_duck.ycor() > y + 5:
            my_duck.setposition(my_duck.xcor() + 5, my_duck.ycor() - 5)
        else:
            my_duck.setposition(my_duck.xcor() + 1, my_duck.ycor() - 1)
    elif my_duck.xcor() > x and my_duck.ycor() < y:
        my_duck.shape(duck_left)
        if my_duck.xcor() > x + 5 and my_duck.ycor() < y - 5:
            my_duck.setposition(my_duck.xcor() - 5, my_duck.ycor() + 5)
        else:
            my_duck.setposition(my_duck.xcor() - 1, my_duck.ycor() + 1)
    elif my_duck.xcor() < x:
        my_duck.shape(duck_right)
        if my_duck.xcor() < x - 5:
            my_duck.setposition(my_duck.xcor() + 5, my_duck.ycor())
        else:
            my_duck.setposition(my_duck.xcor() + 1, my_duck.ycor())
    elif my_duck.ycor() < y:
        if my_duck.ycor() < y - 5:
            my_duck.setposition(my_duck.xcor(), my_duck.ycor() + 5)
        else:
            my_duck.setposition(my_duck.xcor(), my_duck.ycor() + 1)
    elif my_duck.xcor() > x:
        my_duck.shape(duck_left)
        if my_duck.xcor() > x + 5:
            my_duck.setposition(my_duck.xcor() - 5, my_duck.ycor())
        else:
            my_duck.setposition(my_duck.xcor() - 1, my_duck.ycor())
    elif my_duck.ycor() > y:
        if my_duck.ycor() > y + 5:
            my_duck.setposition(my_duck.xcor(), my_duck.ycor() - 5)
        else:
            my_duck.setposition(my_duck.xcor(), my_duck.ycor() - 1)
    else:
        pass
    screen.onclick(my_handler, 1, None)
    print("The duck moved")
    return


def move(x, y):
    crosshair.goto(x, y)


def make_duck(shape, speed):
    duck = turtle.Turtle()
    duck.shape(shape)
    duck.speed(speed)
    duck.penup()
    duck.hideturtle()
    return duck


crosshair_image = "crosshair.gif"
duck_right = "duckpic.gif"
duck_left = "duckpic2.gif"
duck_wing_right = "duckwingright.gif"
duck_wing_left = "duckwingleft.gif"
screen = Screen()
screen.addshape(crosshair_image)
screen.addshape(duck_right)
screen.addshape(duck_left)
screen.addshape(duck_wing_right)
screen.addshape(duck_wing_left)

screen.title("Hunting Ducks")

screen.textinput("Tutorial to Hunting Ducks", "Shoot ducks by clicking them to gain points. \n"
                                        "The ducks speed up from hitting them. \n"
                                        "You have 60 seconds. \n"
                                        "Good luck! \n"
                                        "Hint: Try to stay ahead of them.")

global play_again
play_again = "restart"
while play_again == "restart":
    sc.bgcolor("light blue")
    backgroundnum = random.randint(1, 2)
    if backgroundnum == 1:
        sc.bgpic("backgrounddarkforduckgame.gif")
    else:
        sc.bgpic("backgroundforduckgame.gif")
    duck_shape = duck_right
    crosshair_shape = crosshair_image

    crosshair = turtle.Turtle()
    crosshair.penup()
    crosshair.shape(crosshair_shape)
    crosshair.speed("fastest")

    #score_writer is a score to screen writer
    score_writer = turtle.Turtle()
    turtletimer = turtle.Turtle()

    score = 0
    score_writer.hideturtle()
    score_writer.penup()
    score_writer.setpos(200, 200)
    score_writer.write("0", move=False, align="right", font=("Arial", 20, "normal"))

    turtletimer.hideturtle()
    turtletimer.penup()
    turtletimer.setpos(-200, 200)
    turtletimer.write("60", move=False, align="left", font=("Arial", 20, "normal"))

    amount = 0
    ducks = []
    while amount < 60:
        speed = 0
        ducks.append([make_duck(duck_shape, speed), make_duck(duck_shape, speed)])
        amount += 1

    screen.tracer(n=1, delay=2)

    timer = time.time()

    for duck_amount in range(len(ducks)):
        timer_check = 60
        beg_x = random.randint(-250, 250)
        beg_y = random.randint(-250, 250)
        beg_x1 = random.randint(-250, 250)
        beg_y1 = random.randint(-250, 250)
        ducks[duck_amount][0].speed("fastest")
        ducks[duck_amount][1].speed("fastest")
        ducks[duck_amount][0].setpos(beg_x, beg_y)
        ducks[duck_amount][1].setpos(beg_x1, beg_y1)
        if duck_amount < 2:
            speed = 1
        elif duck_amount < 4:
            speed = 2
        else:
            speed = 3
        ducks[duck_amount][0].speed(speed)
        ducks[duck_amount][1].speed(speed)
        print("fixing speed")
        ducks[duck_amount][0].showturtle()
        ducks[duck_amount][1].showturtle()
        not_destroyed = True
        not_destroyed1 = True
        timer_end = time.time()
        if (timer_end - timer) >= 60:
            not_destroyed = False
            not_destroyed1 = False
            ducks.clear()
            screen.clear()
            sc.bgcolor("dark red")
            # test: print to check that all the ducks are cleared
            print(ducks)
            break
        while not_destroyed or not_destroyed1:
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            print("random x:", x)
            print("random y:", y)
            x1 = random.randint(-250, 250)
            y1 = random.randint(-250, 250)
            timer_end = time.time()
            if (timer_end - timer) >= 60:
                break
            while (ducks[duck_amount][0].xcor() != x
                   and ducks[duck_amount][0].ycor() != y
                   and ducks[duck_amount][0].isvisible()) \
                    or \
                    (ducks[duck_amount][1].xcor() != x1
                     and ducks[duck_amount][1].ycor() != y1
                     and ducks[duck_amount][1].isvisible()):

                if ducks[duck_amount][0].isvisible():
                    if ducks[duck_amount][0].xcor() == x and ducks[duck_amount][0].ycor() == y:
                        x = random.randint(-250, 250)
                        y = random.randint(-250, 250)
                    move_duck(x, y, ducks[duck_amount][0])
                if ducks[duck_amount][1].isvisible():
                    if ducks[duck_amount][1].xcor() == x1 and ducks[duck_amount][1].ycor() == y1:
                        x1 = random.randint(-250, 250)
                        y1 = random.randint(-250, 250)
                    move_duck(x1, y1, ducks[duck_amount][1])

                timer_end = time.time()

                if int(timer_end - timer) != int(timer_check):
                    turtletimer.clear()
                    # + 1 since int rounds down at all times, counting 59.99999 as already 59,
                    # meaning 0 will show and the display will be 1 second ahead of game timer...
                    turtletimer.write(int(60 - (timer_end - timer)) + 1, move=False, align="left",
                                      font=("Arial", 20, "normal"))
                timer_check = timer_end - timer

                screen.update()

                if (int(timer_end - timer) % 2 == 0):
                    duck_right = "duckwingright.gif"
                    duck_left = "duckwingleft.gif"
                else:
                    duck_right = "duckpic.gif"
                    duck_left = "duckpic2.gif"

                print(timer_end - timer)
                if (timer_end - timer) >= 60:
                    print("HIDING")
                    break
            if ducks[duck_amount][0].isvisible():
                not_destroyed = True
                print("The duck is not_destroyed")
            else:
                print("The duck is hidden")
                not_destroyed = False
                print("The duck is destroyed")
            if ducks[duck_amount][1].isvisible():
                not_destroyed1 = True
                print("The duck is not_destroyed")
            else:
                print("The duck is hidden")
                not_destroyed1 = False
                print("The duck is destroyed")

    timer_end = time.time()

    while (timer_end - timer) < 60:
        print(timer_end - timer)
        timer_end = time.time()
    if (timer_end - timer) >= 60:
        crosshair = turtle.Turtle()
        crosshair.penup()
        crosshair.shape(crosshair_shape)
        crosshair.speed("fastest")
        screen.onclick(move)
        turtle.hideturtle()
        phrase = "Game Over! Score:"
        statement = phrase + " " + str(score)
        turtle.write(statement, move=False, align="center", font=("Arial", 20, "normal"))
        print("score:", score)
        textinput = screen.textinput("Play Again?",
                                     "Type restart if you want to play again or quit to be able to close safely!")
        while textinput != "restart" and textinput != "quit":
            textinput = screen.textinput("Play Again?",
                                         "Type restart if you want to play again or quit to be able to close safely!")
        if textinput == "restart":
            play_again = "restart"
            screen.clear()
        elif textinput == "quit":
            play_again = "quit"

turtle.mainloop()
