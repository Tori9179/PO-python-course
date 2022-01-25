from random import randint


file = open("stars.txt", "w")
# for _ in range(50):
#     file.write(50 * '*' + '\n')
for _ in range(50):
    for i in range(51):
        random_num = randint(1, 5)
        if random_num == 1:
            file.write('*')
        else:
            file.write(' ')
        if i == 50:
            file.write('\n')
file.close()
