print("Задание №2")

cub = [x ** 3 for x in range (100) if x%2 != 0 ]
print("cписок кубов нечётных чисел {}".format(cub))
my_number = 0
my_number_list=[]

for a in range(len(cub)):

    my_str = str(cub[a])
    my_list = list(my_str)

    for a in range(len(my_list)):
        my_list[a] = int(my_list[a])

    for a in range(len(my_list)):
        my_number = my_number + my_list[a]

    if my_number % 7 == 0:
        print("Cумму чисел, делящихся на 7 : ",my_number)
        my_number_list.append(my_number)

print("делящихся на 7: ",my_number_list)

cub = [(x**3)+17 for x in range(100) if x%2 == 0]
print("Cписок кубов нечётных чисел {}".format(cub))

print ("Я не совсем понимаю, что делать дальше надо")

