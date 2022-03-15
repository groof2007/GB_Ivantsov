nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

import random


def get_jokes(count:int):
    str_joke = []
    for i in range(count):
        str_joke.append(f' {random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}')
    return str_joke


print(get_jokes(3))