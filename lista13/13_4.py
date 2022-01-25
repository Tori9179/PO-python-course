from graphics import *

win = GraphWin('zad_4', 640, 480)
win.setBackground('black')
o = Oval(Point(525, 200), Point(130, 400))
o.setOutline('green')
o.setFill('green')
o.draw(win)
r = Rectangle(Point(225, 360), Point(30, 200))
r.setOutline('blue')
r.setFill('blue')
r.draw(win)
win.getMouse()
win.close()
