from graphics import *
from random import *
from time import sleep

win = GraphWin('zad 3', 640, 480)
win.setBackground('black')
p = Point(100, 100)
p.setOutline('yellow')
p.draw(win)
step = 10
while True:
    direction = randint(1, 4)
    if direction == 1:
        p.move(0, -step)
    if direction == 2:
        p.move(0, step)
    if direction == 3:
        p.move(-step, 0)
    if direction == 4:
        p.move(step, 0)
    sleep(1 / 10)
# while True:
#     direction = randint(0, 3)  # [0]gora, [1]prawo, [2]dol, [3]lewo
#     if randint(0, 4) == 0:  # zmieniam kierunek jesli zero
#         direction = (direction + randint(1, 3)) % 4
#     if direction == 0:
#         p.move(0, -step)
#     if direction == 1:
#         p.move(step, 0)
#     if direction == 2:
#         p.move(0, step)
#     if direction == 3:
#         p.move(-step, 0)
#     sleep(1 / 10)
win.getMouse()
win.close()
