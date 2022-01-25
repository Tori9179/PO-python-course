a = -1
b = 0
for i in range(1000):
    c = (a + b) / 2
    if (c ** 5 + c + 1) * (a ** 5 + a + 1) > 0:
        a = c
    else:
        b = c
print(f"c jako przyblizona wartosc zera wielomianu wynosi:\n{c ** 5 + c + 1}")
