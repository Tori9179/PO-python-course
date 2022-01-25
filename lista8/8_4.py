f = open("p.txt", "r")
f_all = f.read()
for _ in range(len(f_all)):
    amount = f_all.count('a')
print(f"The number of occurrences of the letter 'a': {amount}")
