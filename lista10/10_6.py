file = open('christmas.txt', 'r')
christmas_str = file.read()
christmas_dict = {}
for x in christmas_str.split(';')[:-1]:
    items = x.split(':')
    christmas_dict[items[0]] = items[1]
print(christmas_dict)
