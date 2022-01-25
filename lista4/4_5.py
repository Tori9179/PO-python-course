lista = []
ilosc = int(input("podaj ilosc liczb: "))
for i in range(ilosc):
    liczba = int(input('podaj liczbe '))
    lista.append(liczba)
srednia = sum(lista)/ilosc
print(f"srednia podanych liczb wynosi: {srednia}")
