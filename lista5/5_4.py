import math
lista = []
ilosc = int(input("podaj ilosc liczb: "))
for i in range(1, ilosc + 1):
    liczba = math.sin(i)
    lista.append(liczba)
print(f"wartosc max: {max(lista)}\n wartosc min: {min(lista)}")
print("Wartosc najmniejsza bedzie dazyc do -1, a najwieksza do 1.")
