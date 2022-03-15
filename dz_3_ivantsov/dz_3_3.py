def thesaurus (*args):
    dict_names = {}
    for name in args:
        key = name[0].capitalize()
        if key not in dict_names:
            dict_names[key] = []
        dict_names[key].append(name)
    return dict_names

print(thesaurus("Иван", "Мария", "Петр", "Илья"))