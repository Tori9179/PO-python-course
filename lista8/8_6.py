f = open("p.txt", "r")
f_all = f.read()
f_all2 = f_all.replace(' ', '*')
f2 = open("p2.txt", "w")
f2.write(f_all2)
