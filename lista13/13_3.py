from graphics import *
from random import *
from time import sleep

color = ['blue', 'yellow', 'red', 'green', 'orange', 'pink', 'purple']

win = GraphWin('zad_3', 640, 480)
win.setBackground('black')
# for x in range(3):
#     c = Circle(Point(randint(0, 640), randint(0, 480)), randint(10, 50))
#     c.setWidth(10)
#     if x == 0:
#         c.setOutline('red')
#         c.setFill('green')
#     if x == 1:
#         c.setOutline('grey')
#         c.setFill('blue')
#     if x == 2:
#         c.setOutline('pink')
#         c.setFill('yellow')
#     c.draw(win)
for x in range(50):
    c = Circle(Point(randint(0, 640), randint(0, 480)), randint(10, 30))
    c.setWidth(10)
    c.setOutline(choice(color))
    c.setFill(choice(color))
    c.draw(win)
    sleep(1/10)
win.getMouse()
win.close()
