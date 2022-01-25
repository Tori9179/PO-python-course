word = input("Enter word to check it: ")
line_number = "Word hasn't been found"
f = open("p.txt", "r")
for number, line in enumerate(f):
    if word in line:
        line_number = number
        break
f.close()
print(line_number)
