def switch_variables(first_variable, second_variable):
    tmp = first_variable
    first_variable = second_variable
    second_variable = tmp
    print(f"Variables in a function:\n1 {first_variable}\n2 {second_variable}")


first = input("Enter first variable: ")
second = input("Enter second variable: ")
print(f"Original variables:\n1 {first}\n2 {second}")
switch_variables(first, second)
print(f"Variables after calling function:\n1 {first}\n2 {second}")
