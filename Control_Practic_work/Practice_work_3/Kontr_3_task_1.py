'''
                            Контрольная работа №_3

    Задание №_1
Напишите функцию, которая будет принимать номер кредитной карты и
показывать только последние 4 цифры. Остальные цифры должны заменяться
звездочками
'''


def card_hide(card):
    return '*' * len(card[:-4]) + card[-4:]


card = input('Введите номер кредитной карты: ')
print(card_hide(card))
