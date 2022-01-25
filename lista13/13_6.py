from graphics import *
from math import *

N = int(input('Enter number of sides of the regular polygon: '))
r = 100
win = GraphWin('zad_6', 640, 480)
win.setBackground('black')
for n in range(0, N + 1):
    x = r * cos(2 * pi * n / N) + 320
    y = r * sin(2 * pi * n / N) + 240
    if n == 0:
        last_point = Point(x, y)
    else:
        p = Point(x, y)
        l = Line(p, last_point)
        l.setOutline('blue')
        l.draw(win)
        last_point = p
win.getMouse()
win.close()
