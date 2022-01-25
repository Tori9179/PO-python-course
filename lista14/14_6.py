from graphics import *
from math import *

x_center, y_center = 320, 240
win = GraphWin('zad 6', 640, 480)
win.setBackground('black')
c1 = Circle(Point(320, 240), 30)
c1.setWidth(10)
c1.setOutline('green')
c1.setFill('green')
c1.draw(win)
while win.isOpen():
    alfa = 0
    r = 100
    while True:
        c2 = Circle(Point(320, 240), 30)
        c2.setWidth(10)
        c2.setOutline('blue')
        c2.setFill('blue')
        x = r * cos(alfa)
        y = r * sin(alfa)
        c2.move(x, y)
        c2.draw(win)
        alfa += 0.1
        time.sleep(1/10)
        c2.undraw()
win.getMouse()
win.close()
