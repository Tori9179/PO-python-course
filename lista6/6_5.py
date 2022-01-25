lista = []
for i in range(31):
    wynik = 3 ** i - 2 ** i
    lista.append(wynik)
lista2 = []
for i in range(len(lista)):
    element = lista[i] % 19
    lista2.append(element)
print(lista2)
print(10 in lista2)
print(11 in lista2)
sprawdz = int(input("podaj liczbe do sprawdzenia z zakresu od 0 do 18: "))
if sprawdz in lista2:
    print(f"Twoja liczba wystepuje w liście {lista2.count(sprawdz)} razy.")
else:
    print("Wybrana liczba nie istnieje w liscie.")
