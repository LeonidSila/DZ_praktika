# nums = { "zero": "ноль",
#     "one": "один",
#     "two": "два",
#     "three": "три",
#     "four": "четире",
#     "five": "пять",
#     "six": "шесть",
#     "seven": "семь",
#     "eight": "восемь",
#     "nine": "девять",}
# def num_translate (new_world):
#     return nums.get("new_world")
#     if to_key:
#         return to_key.capitalize() \
#             if num_word[0].isupper() \
#     else to_key
#     return None
# for key,value in nums.items():
#     print(key,':',value)


print('Решение задания №1')


def num_translate(number):
    """
    check entering 'number' in dict 'numbers',
    if found, return translate from eng on rus,
    if not found, return 'None'
    """
    numbers = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'tree': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }

    print(numbers.get(number.lower(), None))


num_translate(number=input('Введите число прописью по английски от 0 до 10: '))