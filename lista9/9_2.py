f = open("liczby.txt", "r")
s = ''
numbers_list = []
number = ''
check = ''
while True:
    check = f.read(1)
    if check == '':
        break
    elif check != ' ':
        number += check
    elif check == ' ':
        numbers_list.append(number)
        number = ''
print(numbers_list)
