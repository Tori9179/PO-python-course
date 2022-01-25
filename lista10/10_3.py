def no_repeat(my_dict):
    my_dict_values = list(my_dict.values())
    if len(my_dict_values) == len(set(my_dict_values)):
        return 1
    else:
        return 0


dict1 = {10: 20, 100: 17, 7: 8, 11: 46, 6: 81}
dict2 = {10: 20, 100: 20, 7: 8, 11: 8, 6: 81}
if no_repeat(dict1) == 1:
    print('no repeats')
else:
    print('repeats')
if no_repeat(dict2) == 1:
    print('no repeats')
else:
    print('repeats')
