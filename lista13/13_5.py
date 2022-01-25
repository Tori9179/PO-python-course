from graphics import *
from random import *

win = GraphWin('zad_5', 640, 480)
win.setBackground('black')
l = Line(Point(100, 100), Point(200, 200))
l.setOutline('green')
l.draw(win)
l = Line(Point(300, 150), Point(200, 200))
l.setOutline('green')
l.draw(win)
l = Line(Point(100, 100), Point(300, 150))
l.setOutline('green')
l.draw(win)
for i in range(10):
    if i == 0:
        pt = Point(randint(0, 640), randint(0, 480))
        first_pt = pt
        last_pt = pt
    if 0 < i < 9:
        pt_two = Point(randint(0, 640), randint(0, 480))
        l = Line(last_pt, pt_two)
        l.setOutline('blue')
        l.draw(win)
        last_pt = pt_two
    if i == 9:
        l = Line(first_pt, last_pt)
        l.setOutline('blue')
        l.draw(win)
win.getMouse()
win.close()
