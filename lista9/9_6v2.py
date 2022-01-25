from random import randint

x1 = randint(0, 49)
y1 = randint(0, 49)
x2 = randint(0, 49)
y2 = randint(0, 49)

file = open('stars2.txt', 'w')

if x1 == x2:
    for i in range(50):
        for j in range(50):
            if x1 == j and (min(y1, y2) <= i <= max(y1, y2)):
                file.write('*')
            else:
                file.write(' ')
        file.write('\n')
else:
    if x1 > x2:
        tmp = x1
        x1 = x2
        x2 = tmp
        tmp = y1
        y1 = y2
        y2 = tmp
    for i in range(50):
        for j in range(50):
            if x1 <= j <= x2 and abs(((y2 - y1) / (x2 - x1) * (j - x1) + y1) - i) < 0.5:
                file.write('*')
            else:
                file.write(' ')
        file.write('\n')
file.close()
