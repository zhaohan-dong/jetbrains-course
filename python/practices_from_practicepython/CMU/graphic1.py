#!/usr/bin/python3


from graphics import *


def main1():
    win = GraphWin("Display Window", 200, 200)
    origin = Point(100, 100)
    circ1 = Circle(origin, 75)
    circ2 = Circle(origin, 50)
    circ3 = Circle(origin, 25)
    circ1.setFill("red")
    circ2.setFill("white")
    circ3.setFill("red")
    circ1.setOutline("black")
    circ2.setOutline("black")
    circ3.setOutline("black")
    circ1.setWidth(1)
    circ2.setWidth(1)
    circ3.setWidth(1)

    circ1.draw(win)
    circ2.draw(win)
    circ3.draw(win)
    input()
    win.close()

def main4():
    win = GraphWin("Checkerboard", 200, 200)
    for row in range(8):
        for column in range(8):
            a = Point(25*column, 25*row)
            b = Point(25*(column+1), 25*(row+1))
            rect = Rectangle(a, b)
            rect.setWidth(0)
            if row % 2 == column % 2:
                rect.setFill("white")
            else:
                rect.setFill("black")
            rect.draw(win)
    input()


if __name__ == '__main__':
    main4()