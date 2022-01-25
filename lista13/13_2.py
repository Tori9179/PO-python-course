from graphics import *
from random import *

color = ['blue', 'yellow', 'red']

win = GraphWin('zad_2', 640, 480)
win.setBackground('black')
pt = Point(125, 140)
pt.setOutline('blue')
pt.draw(win)
pt = Point(175, 300)
pt.setOutline('yellow')
pt.draw(win)
pt = Point(25, 40)
pt.setOutline('red')
pt.draw(win)
for _ in range(1000):
    pt = Point(randint(0, 640), randint(0, 480))
    pt.setOutline(choice(color))
    pt.draw(win)
win.getMouse()
win.close()
