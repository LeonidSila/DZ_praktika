from sys import getsizeof
users = ['Иван', 'Анастасия', 'Петр', 'Сергей','Дмитрий', 'Борис', 'Елена']
klass = ['9А', '7В', '9Б', '9В', '8Б']
def my_zip_gen():
    len_klass = len(klass)
    return ((urs, klass[i]) if i < len_klass else (urs, None)
            for i, urs in enumerate(users))
if __name__ == '__main__':
    gen = my_zip_gen()
    print(type(gen))
    print(getsizeof(gen))
    print(*gen)