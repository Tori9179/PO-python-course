def switch_variables(my_list):
    tmp = my_list[0]
    my_list[0] = my_list[1]
    my_list[1] = tmp
    return my_list


arr = []
for i in range(2):
    x = input("Enter value: ")
    arr.append(x)
print(f"List before a func: {arr}")
switch_variables(arr)
print(f"List after a func: {arr}")
