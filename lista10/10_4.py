import warnings


def reverse_dict(my_dict):
    new_dict = {}
    my_dict_values = list(my_dict.values())
    if len(my_dict_values) == len(set(my_dict_values)): #nie ma
        for dict_key, dict_value in my_dict.items():
            new_dict[dict_value] = dict_key
        print(f'Your dictionary have been switched from:\n{my_dict}\nto:\n{new_dict}')
        return new_dict
    else: #są
        warnings.warn("There is a duplicate in your dictionary")


dict1 = {'present': 'prezent', 'candle': 'świeca', 'snowman': 'bałwan', 'sleigh': 'sanie', 'gift': 'prezent'}
dict2 = {'reindeer': 'renifer', 'gingerbread': 'piernik', 'star': 'gwiazda', 'carol': 'kolęda', 'christmas tree': 'choinka'}
reverse_dict(dict1)
reverse_dict(dict2)

