lista = [3, 7, 11, 33, 77, 6, 10, 20, 100, 14]
print(f"Pierwotna lista: {lista}")
lista2 = lista[1:] + [lista[0]]
lista3 = [lista[-1]] + lista[:-1]
lista4 = lista[::-1]
lista5 = [liczba for liczba in lista if liczba % 2 == 0]
lista6 = [lista[i] for i in range(len(lista)) if lista[i] % 2 == 1 and i % 2 == 0]
print(f"Pierwszy element na koniec listy: {lista2}")
print(f"Ostatni element na poczatek listy: {lista3}")
print(f"Ostatni element na poczatek listy: {lista4}")
print(f"Tylko parzyste elementy: {lista5}")
print(f"Tylko parzyste indeksy z nieparzystymi elementami: {lista6}")
