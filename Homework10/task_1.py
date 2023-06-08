# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random


# Здесь пишем код
def generate_random_name():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    while True:
        word1 = ''
        word2 = ''
        for i in range(int(random.random() * 15 + 1)):
            word1 += random.choice(alphabet)

        for i in range(int(random.random() * 15 + 1)):
            word2 += random.choice(alphabet)
        yield "{} {}".format(word1, word2)


gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
