
# Практическое задание №1

print ("Задание №1")

one_minute = 60

one_hour = 3600

one_day = 86400

one_week = 604800

one_month = 2629743

one_year = 31556926
user_input = []
user_input = int (input("Укажите колличество секунд"))

if user_input <= one_minute:
    print ("{} сек".format (user_input))
elif one_minute <= user_input and one_hour > user_input:
    out_minute = user_input // one_minute
    # print(out_minute)
    out_second = user_input % one_minute
    # print(out_second)
    print ("{} min {} сек".format (out_minute,out_second));
elif user_input >= one_hour and user_input < one_day:
    out_hour = user_input // one_hour
    user_input = user_input % one_hour
    out_minute = user_input // one_minute
    out_second = user_input % one_minute
    print("{} час {} мин {} сек".format (out_hour,out_minute,out_second));
elif user_input >= one_day and user_input < one_week:
    out_day = user_input // one_day
    user_input = user_input % one_day
    out_hour = user_input // one_hour
    user_input = user_input % one_hour
    out_minut = user_input // one_minute
    out_second = user_input % one_minute
    print("{} дн {} час {} мин {} сек ".format (out_day,out_hour,out_minut,out_second));
elif user_input >= one_month and user_input < one_year:
    out_week = user_input // one_week
    user_input =user_input % one_week
    out_day = user_input // one_day
    user_input = user_input % one_day
    out_hour = user_input // one_hour
    user_input = user_input % one_hour
    out_minute = user_input // one_minute
    out_second = user_input % one_minute
    print('{} нед {} дн {} час {} мин {} сек'.format (out_week, out_day, out_hour, out_minute, out_second));
elif user_input >= one_year:
    out_year=user_input//one_year
    user_input = user_input % one_year
    out_week = user_input//one_week
    user_input = user_input%one_week
    out_day = user_input // one_day
    user_input = user_input % one_day
    out_hour = user_input // one_hour
    user_input = user_input % one_hour
    out_minute = user_input // one_minute
    out_second = user_input % one_minute
    print('{} годиков {} неде {} дн {} час {} мин {} сек'.format (out_year, out_week, out_day, out_hour, out_minute, out_second));




