lista = list('Alamakota')
print(f"Lista = {lista}")
print(f"indeks litery 'a': {lista.index('a')}")
print(f"indeks litery 'k': {lista.index('k')}")
print(f"indeks litery 'm': {lista.index('m')}")
print("Nie mozna wyswietlic indeksu dla znaku 's', bo nie ma go w liscie.")
print("Jesli jakis znak wystepuje wiecej niz jeden raz, to pokazywany jest tylko indeks pierwszego wystapienia.")
lista2 = []
for i in range(31):
    wynik = 3 ** i - 2 ** i
    lista2.append(wynik)
print(lista2)
print(f"Liczba 1161737179 występuje na pozycji {lista2.index(1161737179)} w liscie.")
