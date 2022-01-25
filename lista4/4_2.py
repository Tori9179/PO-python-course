zdanie = input("Podaj zdanie: ")
licznik = 0
for i in zdanie:
    if i == 'a':
        licznik += 1
print()
print(f"liczba 'a' w zdaniu: {licznik}")