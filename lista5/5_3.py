lista = []
ilosc = int(input("podaj ilosc liczb: "))
for i in range(ilosc):
    liczba = float(input('podaj liczbe '))
    lista.append(liczba)
print(f"wartosc max: {max(lista)}\n wartosc min: {min(lista)}")
