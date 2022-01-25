def reverse_list(my_list):
    return my_list.reverse()


arr = []
length = int(input("Enter list's length: "))
for i in range(length):
    x = input("Enter value: ")
    arr.append(x)
print(f"List before a func: {arr}")
reverse_list(arr)
print(f"List after a func: {arr}")
