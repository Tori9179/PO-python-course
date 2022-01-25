from graphics import *

win = GraphWin('zad 2', 640, 480)
win.setBackground('black')
c = Circle(Point(90, 90), 60)
c.setWidth(10)
c.setOutline('yellow')
c.setFill('yellow')
c.draw(win)
while True:
    k = win.getKey()
    if k == 'w':
        c.move(0, -50)
    if k == 's':
        c.move(0, 50)
    if k == 'a':
        c.move(-50, 0)
    if k == 'd':
        c.move(50, 0)
    if k == 'q':
        win.close()
