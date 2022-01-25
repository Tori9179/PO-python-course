from graphics import *
from random import *
from math import *

win = GraphWin('zad 4', 640, 480)
win.setBackground('black')
c = Circle(Point(320, 240), 30)
c.setWidth(10)
c.setOutline('green')
c.setFill('green')
c.draw(win)
alfa = 0
while win.isOpen():
    alfa = alfa + 50 if randint(0, 1) == 0 else alfa - 50
    c.move(20 * cos(alfa), 20 * sin(alfa))
    time.sleep(1/10)
win.getMouse()
win.close()
