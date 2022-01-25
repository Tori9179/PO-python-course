dict_christmas = {'reindeer': 'renifer', 'gingerbread': 'piernik', 'gift': 'prezent', 'sleigh': 'sanie'}
file = open('christmas.txt', 'w')
for key, value in dict_christmas.items():
    file.write(f"{key}:{value};")
file.close()
