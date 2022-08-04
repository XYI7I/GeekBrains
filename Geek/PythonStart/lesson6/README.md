# Знакомство с языком Python (семинары)
## Урок 6. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension. Продолжение

> [Задача 1](https://github.com/XYI7I/GeekBrains/tree/main/Geek/PythonStart/lesson6/task1/main.py): Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.

    *Пример:*

    2+2 => 4;

    1+2*3 => 7;

    1-2*3 => -5;

    Добавьте возможность использования скобок, меняющих приоритет операций.

        *Пример:*

        1+2*3
         => 7;

        (1+2)*3 => 9; 

> [Задача 2](https://github.com/XYI7I/GeekBrains/tree/main/Geek/PythonStart/lesson6/task2/main.py): Задача: предложить улучшения кода для уже решённых задач с помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

    Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
    Пример:
    
    [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
    
    Найти сумму чисел списка стоящих на нечетной позиции
    
    Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
    Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
