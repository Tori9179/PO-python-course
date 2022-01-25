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
step_cos = 10 * cos(alfa)
time.sleep(1/10)
while win.isOpen():
    pc = c.getCenter()
    step_cos = 10 * cos(alfa)
    step_sin = 10 * sin(alfa)
    alfa = alfa + 50 if randint(0, 1) == 0 else alfa - 50
    if 0 < pc.x + step_cos < 460 and 0 < pc.y + step_sin < 480:
        c.move(step_cos, step_sin)
    time.sleep(1 / 10)
win.getMouse()
win.close()
