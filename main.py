import time
import turtle
from turtle import Screen
from set_up import Set_up,Indicator,Score,Turn
myscreen=Screen()
myscreen.tracer(0)

myscreen.bgcolor("Black")
myscreen.update()
setup=Set_up()
setup.draw_lines()


game_on = True
tom=Indicator()
turn = 0
score = Score()
score.update_score(setup.xscor,setup.oscor)
turn =Turn()
turn.update_turn(tom.turn)
while game_on:

    turtle.update()
    myscreen.listen()
    myscreen.onscreenclick(tom.click)
    turn.update_turn(tom.turn)

    if tom.check_win() or tom.max_plays():
        turtle.update()

        if tom.check_win():
            if tom.win == 0:
                setup.oscor += 1
            else:
                setup.xscor +=1
            time.sleep(2)
            score.update_score(setup.xscor,setup.oscor)
            tom.clear()
            tom.__init__()

        else:

            tom.clear()
            tom.__init__()


myscreen.exitonclick()
