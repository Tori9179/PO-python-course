from math import factorial
silnia = str(factorial(1000))
for i in range(10):
    for j in range(10):
        para = str(i) + str(j)
        print(f"{para} wystepuje {silnia.count(para)}")
