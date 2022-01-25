file = open('pierwsze.txt', 'r')
prime_num = file.read()
list_prime_num = list(prime_num.split(" "))
del list_prime_num[-1]
last_prime = int(list_prime_num[-1])
print(f"Ostatnia liczba pierwsza: {last_prime}")
file.close()
file = open('pierwsze.txt', 'a')
hundred = int(last_prime / 100 % 10)
first = (1 + hundred) * 100
last = first + 100
for liczba in range(first, last):
    dzielniki = 0
    for i in range(1, liczba + 1):
        if(liczba % i == 0):
            dzielniki += 1
    if dzielniki == 2:
        file.write(str(liczba) + ' ')
file.close()
