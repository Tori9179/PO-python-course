f = open("p.txt", "r")
f_all = f.read()
# f_all2 = f_all.replace(' ', '*')
f_all2 = ''
for j in(f_all):
    if j.isupper():
        j = j.lower()
    else:
        j = j.upper()
    f_all2 += j
f2 = open("p3.txt", "w")
f2.write(f_all2)
