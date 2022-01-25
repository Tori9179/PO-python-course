def bubble_sort(my_list):
    for _ in range(len(my_list)):
        for j in range(0, len(my_list) - 1):
            if my_list[j].lower() > my_list[j + 1].lower():
                my_list[j + 1], my_list[j] = my_list[j], my_list[j + 1]
    return my_list


def bubble_sort_len(my_list):
    for _ in range(len(my_list)):
        for j in range(0, len(my_list) - 1):
            if len(my_list[j]) > len(my_list[j + 1]):
                my_list[j + 1], my_list[j] = my_list[j], my_list[j + 1]
    return my_list


statement = input("Enter statement: ")
statement_list = list(statement.split(" "))
print(statement_list)
print(bubble_sort(statement_list))
print(bubble_sort_len(statement_list))
