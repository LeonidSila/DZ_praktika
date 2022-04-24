list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
l_list:int = len(list)
list_id = id(list)
print(f"id before {list_id}")
for i in range(l_list):
    elem = list.pop(0)
    if elem.isdigit():
        list.append(f'"{int(elem):02d}"')
    elif elem[0] == "+" and elem[1].isdigit():
        list.append(f'"+{int(elem):02d}"')
    else:
        list.append(elem)
print(' '.join(list))
print(f"id after {id(list)}")