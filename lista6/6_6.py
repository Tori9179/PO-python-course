from math import *
lista = [1 / i for i in range(1, 101)]
print(lista)
print(f"suma = {sum(lista)}\nmin = {min(lista)}\nmax = {max(lista)}")
print()
n = factorial(1000)
s2 = str(n)
lista2 = list(s2)
print(f"Suma cyfr 1000! = {sum(map(int, lista2))}")
