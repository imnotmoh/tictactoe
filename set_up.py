import random
import turtle
from turtle import Turtle,Screen
import time

class Set_up(Turtle):
    def __init__(self):
        self.xscor = 0
        self.oscor = 0
        super().__init__()
        self.hideturtle()
        self.penup()

        self.pensize(width=5)
        self.pencolor("White")
    def draw_lines(self):
        for i in range(-50, 100, 100):
            self.goto(x=i,y=150)
            self.setheading(270)
            self.draw()

        for i in range(-50, 100,100):
            print(i)
            self.goto(x=150,y=i)
            self.setheading(180)
            self.draw()


    def draw(self):
        self.pendown()
        self.forward(300)
        self.penup()


class Tictaks(Turtle):
    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.pencolor("White")
        self.pensize(width=5)





class Indicator(Turtle):
    def __init__(self):
        super().__init__()
        self.win = None
        self.turn = random.randint(1,2)
        self.color("White")
        self.penup()
        self.goto(y=250,x=0)
        self.write(arg=" TicTacToe", move=False, align="center", font=("Arial", 50, 'normal'))
        self.tictakcor = [(-100.0, 100.0), (0.0, 100.0), (100.0, 100.0), (-100.0, 0.0), (-0.0, -0.0), (100.0, -0.0), (-100.0, -100.0), (-0.0, -100.0), (100.0, -100.0)]
        self.wincor = [self.tictakcor[:3],self.tictakcor[3:6],self.tictakcor[6:],[(-100.0, 100.0), (-100.0, -0.0), (-100.0, -100.0)], [(-0.0, 100.0), (-0.0, -0.0), (0.0, -100.0)],[(100.0, 100.0), (100.0, -0.0), (100.0, -100.0)],[(100.0, 100.0), (0.0, -0.0), (-100.0, -100.0)],[(-100.0, 100.0), (-0.0, -0.0), (100.0, -100.0)]]
        self.corx = []
        self.coro = []

        self.hideturtle()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(4)

    def click(self,x,y):
        if 150 > x > -150:
            if 150 > y > -150:
                self.goto(round(x,-2),round(y,-2))
                if self.turn % 2 == 0:
                    if (self.xcor(),self.ycor()) not in self.coro and (self.xcor(),self.ycor()) not in self.corx:
                        self.coro.append((self.xcor(), self.ycor()))
                        self.o()
                        self.turnsym="X"
                        self.turn += 1
                        self.goto(0,200)






                elif self.turn % 2 == 1:
                    if (self.xcor(),self.ycor()) not in self.coro and (self.xcor(),self.ycor()) not in self.corx:
                        self.corx.append((self.xcor(),self.ycor()))
                        self.x()
                        self.turn += 1




    def o(self):
        self.setheading(0)
        self.goto(self.xcor(),self.ycor()-30)
        self.pendown()
        self.pensize(5)
        self.circle(30,steps=180)
        self.penup()



    def x(self):
        self.pendown()
        self.pensize(5)
        self.setheading(60)
        self.back(25)
        self.forward(50)
        self.penup()
        self.goto(y=self.ycor(), x=self.xcor()-(23))
        self.setheading(300)
        self.pendown()
        self.forward(50)
        self.penup()







    def check_win(self):

        for wins in self.wincor:
            wino = 0
            for cor in wins:
                for i in self.coro:
                    if i == cor:
                        wino += 1
            if wino > 2:
                self.goto(wins[0])
                self.pendown()
                self.goto(wins[2])
                self.penup()
                self.win = 0
                return True

            # else:
            #     return [False]

        for wins in self.wincor:
            winx = 0
            for cor in wins:
                for i in self.corx:
                    if i == cor:
                        winx += 1
            if winx > 2:
                self.goto(wins[0])
                self.pendown()
                self.goto(wins[2])
                self.penup()
                self.win=1
                return True
            # else:
            #     return [False]





    def computer_ai(self):
        pass

    # def blink(self):
    #     self.hideturtle()
    #     time.sleep(0.5)
    #     self.showturtle()
    #     time.sleep(0.5)

    def max_plays(self):
        if len(self.coro) + len(self.corx) == 9:
            return True

class Score(Turtle):
    def __init__(self,):
        super().__init__()
        self.color("White")
        self.hideturtle()
        self.penup()
    def update_score(self,xscor,yscor):
        self.clear()

        self.goto(y=200,x=150)
        self.write(arg=f"X:{xscor}", move=False, align="center", font=("Arial", 30, 'normal'))
        self.goto(y=200,x=-150)
        self.write(arg=f"O:{yscor}", move=False, align="center", font=("Arial", 30, 'normal'))

class Turn(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("White")
    def update_turn(self,turn):
        self.clear()
        if turn%2 == 0:
            self.turnsym = "O"
            print(turn)
        else:
            self.turnsym = "X"
            print(turn)
        self.goto(0,200)
        self.write(arg=f"{self.turnsym}", move=False, align="center", font=("Arial", 30, 'normal'))

