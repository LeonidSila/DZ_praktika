
import pyjokes

from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
list_1 = []
joke = pyjokes.get_joke(language="en", category='all')

def get_jokes(n, flag=False):
    for i in range(n):
        random_index = choice(nouns)
        random_index_1 = choice(adverbs)
        random_index_2 = choice(adjectives)
        jokes = "{} {} {}".format(random_index, random_index_1, random_index_2)
        print(jokes)
        list_2 = []
        if flag == True:
            list_2 = jokes.split()
            print(jokes)
        if joke != range(n):
            print(joke)
            for i in range(len(nouns)):
                for fun in list_2:
                    if nouns[i] == fun:
                        nouns.pop(i)

get_jokes(1)