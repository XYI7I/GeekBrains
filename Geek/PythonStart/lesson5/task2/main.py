"""
Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота

b) Подумайте как наделить бота ""интеллектом""
"""

from random import randint

# candy = 2021
candy = 280 # для удобства и минимзации кол-ва ходов
print('Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход '
      'определяется жеребьёвкой.\nЗа один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются '
      'сделавшему последний ход.')
query = randint(1, 7) % 2
turn_candy = 28

while candy > 28:
    # print(randint(1,3))
    print(f"{candy} - candies left.")
    turn_candy = 29
    if query == 0:
        print('The first player\'s turn')
        query += 1
        while turn_candy > 28 or turn_candy < 1:
            turn_candy = int(input('take candies in range(1:28) - '))
    else:
        print('The second player\'s turn')
        query -= 1
        while turn_candy > 28 or turn_candy < 1:
            turn_candy = int(input('take candies in range(1:28) - '))


    candy -= turn_candy


if query == 0:
    print('The first player win!')
else:
    print('The second player win!')


