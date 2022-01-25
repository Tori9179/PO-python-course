zakres = int(input("podaj zakres dokladnosci: "))
ln = 0
pi = 0
mianownik = 3
for i in range(1, zakres):
    if i % 2 == 1:
        ln += 1 / (1 + i)
    else:
        ln -= 1 / (1 + i)
print("wynik ln(2) to: ", 1 - ln)
for i in range(1, zakres):
    if i % 2 == 1:
        pi -= 1 / mianownik
        mianownik += 2
    else:
        pi += 1 / mianownik
        mianownik += 2
print("przyblizona wartosc liczby pi to: ", 4 * (1 + pi))
