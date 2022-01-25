from random import randint

x1 = randint(0, 49)
y1 = randint(0, 49)
x2 = randint(0, 49)
y2 = randint(0, 49)

iterator = -1 if x1 > x2 else 1
file = open('stars2.txt', 'w')

dx = x2 - x1
dy = y2 - y1
points_list = []

if x1 == x2 and y1 == y2:
    points_list.append((x1, y1))
elif x1 == x2:
    iterator = -1 if y1 > y2 else 1
    for y in range(y1, y2 + iterator, iterator):
        x = int(x1 + dx * (y - y1) / dy)
        points_list.append((x, y))
elif y1 == y2:
    for x in range(x1, x2 + iterator, iterator):
        y = int(y1 + dy * (x - x1) / dx)
        points_list.append((x, y))
else:
    for x in range(x1, x2 + iterator, iterator):
        y = int(y1 + dy * (x - x1) / dx)
        points_list.append((x, y))

for i in range(51):
    for j in range(51):
        if (j, i) in points_list:
            file.write('*')
        else:
            file.write(' ')
    file.write('\n')
file.close()
