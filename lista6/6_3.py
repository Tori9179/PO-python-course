from math import *
i = 321
s = str(i)
lista = list(s)
n = factorial(1000)
s2 = str(n)
lista2 = list(s2)
for i in range(10):
    ile = lista2.count(str(i))
    print(f"liczba cyfr {i} w silni wynosi: {ile}")
print("mozna zauwazyc, ze zera mniej wiecej dwa razy czesciej wystepuja niz pozostale cyfry ktorych jest zblizona ilosc")
