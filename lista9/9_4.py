file = open('pierwsze.txt', 'w')
for liczba in range(1, 101):
    dzielniki = 0
    for i in range(1, liczba + 1):
        if(liczba % i == 0):
            dzielniki += 1
    if dzielniki == 2:
        file.write(str(liczba) + ' ')
file.close()