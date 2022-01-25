f = open("p.txt", "r")
while 1:
    s = f.read(3)
    print(s)
    if s == '':
        break
