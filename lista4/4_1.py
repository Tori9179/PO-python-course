for i in "To jest zdanie":
    print(i, end='*')
print()
zdanie = input("Podaj zdanie: ")
licznik = 0
dlugosc = len(zdanie)
dlugosc_stringa = 0
for i in zdanie:
    dlugosc_stringa += 1
    if dlugosc_stringa != dlugosc:
        if i != ' ':
            print(i, end=' ')
            licznik += 1
    else:
        print(i)
        licznik += 1
print()
print(f"liczba znakow: {2 * licznik - 1}")