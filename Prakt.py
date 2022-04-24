# print("кто есть тип, кто ты?")
# print(f"type (15 * 3) is {type (15 * 3)}")
# print(f"type (15 / 3) is {type (15 / 3)}")
# print(f"type (15 // 23) is {type (15 // 2)}")
# print(f"type (15 ** 2) is {type (15 ** 2)}")


# cord = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# print(type (cord))
#
# from copy import deepcopy
#
# new_cord = deepcopy(cord)
# length_of_cord:int = len(new_cord)
# new_cord_id = id(new_cord)
#
# print(f"id до {new_cord_id}")
# for i in range(length_of_cord):
#     elem = new_cord.pop(0)
#     if elem.isdigit():
#         new_cord.append(f'{int(elem):02d}')# Распишите подробнее, что тут происходит, особеноо 02d!
#     else:
#         new_cord.append(elem)
# print(' '.join(new_cord))
# print(f"id после {id(new_cord)}")



# # input_word = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# for string in input_word:
#     corect_word = string.split(" ")[-1].capitalize()
#     print(f"HEllO, {corect_word}")