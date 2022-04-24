input_list = ['инженер-конструктор Игорь',
            'главный бухгалтер МАРИНА',
            'токарь высшего разряда нИКОЛАй',
            'директор аэлита']
for i in input_list:
    correct_name = i.split()[-1].capitalize()
    print(f"Привет, {correct_name}!")