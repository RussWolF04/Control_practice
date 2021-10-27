'''
                            Контрольная работа №_3

    Задание №_2
Напишите функцию, которая проверяет: является ли слово палиндромом
'''

print('Проверим солово на "Палиндромом"')
word = input("Введите слово: ")
reverse = word[::-1]


def palindrom(word):

    while True:
        if word[::1] == reverse:
            return f'Слово - {word} - это палиндром'

        else:
            return f'Слово - {word} - это не палиндром'


print(palindrom(word))