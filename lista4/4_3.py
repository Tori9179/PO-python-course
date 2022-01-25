zdanie = input("Podaj zdanie: ")
licznik = 0
for i in zdanie:
    if i != ' ':
        print(i, end='')
    else:
        print()
        licznik += 1
print()
print(f"liczba slow w zdaniu: {licznik + 1}")