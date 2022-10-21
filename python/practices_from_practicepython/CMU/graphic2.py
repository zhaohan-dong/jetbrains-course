#!/usr/bin/python3


from graphics import *

def main1():
    win = GraphWin("Clock", 200, 200)
    face = Circle(Point(100, 100), 75)
    face.setFill("yellow")
    face.setWidth(1)
    face.setOutline("black")
    face.draw(win)
    XII = Text(Point(100, 40), "12")
    III = Text(Point(160, 100), "3")
    VI = Text(Point(100, 160), "6")
    XI = Text(Point(40, 100), "9")
    for elem in [XII, III, VI, XI]:
        elem.setFace("helvetica")
        elem.setSize(18)
        elem.setStyle("normal")
        elem.setTextColor("black")
        elem.draw(win)
    hour = Line(Point(100, 100), Point(120, 120))
    minute = Line(Point(100, 100), Point(100, 150))
    hour.setFill("black")
    minute.setFill("black")
    hour.draw(win)
    minute.draw(win)
    input()



if __name__ == '__main__':
    main1()