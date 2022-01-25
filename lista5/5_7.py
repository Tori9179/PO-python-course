import math
liczba = format(math.pi, ".50f")
lista = []
for i in liczba:
    if i != '.':
        lista.append(i)
lista.pop(0)
print(lista)
