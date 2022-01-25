from random import randint


def bubble_sort(my_list):
    for _ in range(len(my_list)):
        for j in range(0, len(my_list) - 1):
            if my_list[j] > my_list[j + 1]:
                my_list[j + 1], my_list[j] = my_list[j], my_list[j + 1]
    return my_list


arr = []
for i in range(10):
    arr.append(randint(1, 100))
print(arr)
print(bubble_sort(arr))
arr2 = ["ultraviolence", "lolita", "ride", "cola", "dealer", "carmen"]
print(arr2)
print(bubble_sort(arr2))
