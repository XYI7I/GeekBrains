"""
Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота

b) Подумайте как наделить бота ""интеллектом""
"""

from random import randint

# candy = 2021
candy = 280 # для удобства и минимзации кол-ва ходов

print(
    'Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход '
    'определяется жеребьёвкой.\nЗа один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются '
    'сделавшему последний ход.')
query = randint(1, 7) % 2
turn_candy = 28

while candy > 28:
    # print(randint(1,3))
    if query == 0:
        print('The first player\'s turn')
        query += 1
        turn_candy = 29
        while turn_candy > 28 or turn_candy < 1:
            turn_candy = int(input('take candies in range(1:28) - '))
    else:
        # print(candy//28, candy//29)
        if candy % 29 != 0:
            turn_candy = candy % 29
        else:
            turn_candy = randint(1, 28)

        print(f'The bot turn - {turn_candy} candies')
        query -= 1

    candy -= turn_candy
    print(f"{candy} - candies left.")

if query == 0:
    print('You win the leather bag of bones!')
else:
    print('The bot player win!')
