from random import randint

numbers = ''
for _ in range(20):
    numbers += str(randint(1, 100)) + ' '
f = open("liczby.txt", "w")
f.write(numbers)
f.close()