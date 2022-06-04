﻿# [![GeekBrains](https://frontend-scripts.hb.bizmrg.com/unique-hf/svg/logo.svg)](https://gb.ru)

## Знакомство с языками программирования (семинары)

### Урок 8. Как не нужно писать код. Часть 2

> [Задача 53](https://github.com/XYI7I/GeekBrains/blob/main/Geek/C%23/lesson8/task1/Program.cs): Задайте двумерный массив. Напишите программу, которая поменяет местами первую и последнюю строку массива.

        Например, задан массив:
        1 4 7 2             5 2 6 7
        5 9 2 3     -->     5 9 2 3
        8 4 2 4             8 4 2 4
        5 2 6 7             1 4 7 2

> [Задача 55](https://github.com/XYI7I/GeekBrains/tree/main/Geek/C%23/lesson8/task2/Program.cs): Задайте двумерный массив. Напишите программу, которая заменяет строки на столбцы. В случае, если это невозможно, программа должна вывести сообщение для пользователя.

        m = 3, n = 4.
        
        0 1 2 3   ->    0 1 2
        1 2 3 4         1 2 3
        2 3 4 5         2 3 4
                        3 4 5

> [Задача 57](https://github.com/XYI7I/GeekBrains/tree/main/Geek/C%23/lesson8/task3/Program.cs): Составить частотный словарь элементов двумерного массива. Частотный словарь содержит информацию о том, сколько раз встречается элемент входных данных.

            Набор данных            Частотный массив
            
        { 1, 9, 9, 0, 2, 8, 0, 9 }  0 встречается 2 раза
                                    1 встречается 1 раз
                                    2 встречается 1 раз
                                    8 встречается 1 раз
                                    9 встречается 3 раза
        
        1 2 3                       1 встречается 3 раза
        4 6 1                       2 встречается 2 раз
        2 1 6                       3 встречается 1 раз
                                    4 встречается 1 раз
                                    6 встречается 2 раза
        
> [Задача 59](https://github.com/XYI7I/GeekBrains/tree/main/Geek/C%23/lesson8/task4/Program.cs): Задайте двумерный массив из целых чисел. Напишите программу, которая удалит строку и столбец, на пересечении которых расположен наименьший элемент массива.

        Например, задан массив:
        1 4 7 2
        5 9 2 3
        8 4 2 4
        5 2 6 7

        Наименьший элемент - 1, на выходе получим следующий массив:
        9 2 3
        4 2 4
        2 6 7