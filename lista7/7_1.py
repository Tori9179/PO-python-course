def switch_variables(first_variable, second_variable):
    tmp = first_variable
    first_variable = second_variable
    second_variable = tmp
    return first_variable, second_variable


first = input("Enter first variable: ")
second = input("Enter second variable: ")
print(f"Original variables:\n1 {first}\n2 {second}")
first, second = switch_variables(first, second)
print(f"Switched variables:\n1 {first}\n2 {second}")
