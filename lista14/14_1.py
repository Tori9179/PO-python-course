from graphics import *
from time import sleep

win = GraphWin('zad 1', 640, 480)
win.setBackground('black')
o = Oval(Point(325, 200), Point(130, 250))
o.setOutline('green')
o.setFill('green')
o.draw(win)
c = Circle(Point(90, 90), 60)
c.setWidth(10)
c.setOutline('yellow')
c.setFill('yellow')
c.draw(win)
r = Rectangle(Point(300, 400), Point(530, 300))
r.setOutline('blue')
r.setFill('blue')
r.draw(win)
for i in range(13):
    c.move(20, 20)
    sleep(1 / 10)
win.getMouse()
win.close()
