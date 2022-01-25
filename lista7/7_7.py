from random import randint, choice


def bubble_sort(my_list):
    for _ in range(len(my_list)):
        for j in range(0, len(my_list) - 1):
            if my_list[j] > my_list[j + 1]:
                my_list[j + 1], my_list[j] = my_list[j], my_list[j + 1]
    return my_list


arr = []
word = ''
for i in range(10):
    for j in range(randint(3, 8)):
        word += chr(randint(97, 122))
    arr.append(word)
    word = ''
print(arr)
print(bubble_sort(arr))

vowels = ['a', 'e', 'i', 'o', 'u', 'y']
vowels_num = [97, 101, 105, 111, 117, 121]
arr2 = []
word2 = ''
for _ in range(10):
    for i in range(randint(3, 8)):
        if i % 3 == 0:
            word2 += choice(vowels)
        else:
            letter = chr(choice([k for k in range(97, 122) if k not in vowels_num and ord(word2[-1])]))
            word2 += letter
    arr2.append(word2)
    word2 = ''
print(arr2)
print(bubble_sort(arr2))
