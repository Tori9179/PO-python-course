list = []
for i in range(1, 11):
    list = list + [i**2]
print(list)
for i in range(len(list)):
    if i % 2 == 1:
        list[i] = -list[i]
print(list)
