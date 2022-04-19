print("Задание №3")

a = range(100)

for a in range(100):
    new_str=str(a+1)
    new_list = list(new_str)
    if int(new_list[-1])==1 and a+1!=11:
        print('{} процент'.format(a + 1))
    elif int(new_list[-1])>1 and int(new_list[-1])<= 4:
        if  a+1> 10 and a+1<= 14:
            print('{} процентов'.format(a + 1))
        else:
            print('{} процента'.format(a + 1))
    else:
        print('{} процентов'.format(a + 1))