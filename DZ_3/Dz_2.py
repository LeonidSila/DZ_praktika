def thesaurus(*names):
    out_dict = {}
    for name in names:
        key = name[0].capitalize()
        if key not in out_dict:
            out_dict[key] = []
        out_dict[key].append(name)

    return out_dict
print(thesaurus("Иван", "Мария", "Петр", "Илья"))
