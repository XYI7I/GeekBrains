# Java: знакомство и как пользоваться базовым API (семинары)
## Урок 1.  Знакомство с языком программирования Java

> [Задача 1](https://github.com/XYI7I/GeekBrains/tree/main/Geek/JavaStart/lesson1/task1/task1/src/Main.java): Реализовать функцию возведения числа а в степень b. a, b ∈ Z. Сводя количество выполняемых действий к минимуму.

        Пример 1: а = 3, b = 2, ответ: 9
        Пример 2: а = 2, b = -2, ответ: 0.25
        Пример 3: а = 3, b = 0, ответ: 1
        Пример 4: а = 0, b = 0, ответ: не определено
        Пример 5
        входные данные находятся в файле input.txt в виде
        b 3
        a 10
        Результат нужно сохранить в файле output.txt
        1000


> [Задача 2](https://github.com/XYI7I/GeekBrains/tree/main/Geek/JavaStart/lesson1/task2/task2/src/Main.java): На вход некоторому исполнителю подаётся два числа (a, b). У исполнителя есть две команды

        команда 1 (к1): увеличить в с раза, а умножается на c
        команда 2 (к2): увеличить на d, к a прибавляется d
        написать программу, которая выдаёт набор команд, позволяющий число a превратить в число b или сообщить, что это невозможно
        Пример 1: а = 1, b = 7, c = 2, d = 1
        ответ: к2, к2, к2, к2, к2, к2, k2 или к1, к1, к2, к2, к2
        Можно начать с более простого – просто подсчёта общего количесвтва вариантов
        Пример 2: а = 11, b = 7, c = 2, d = 1
        ответ: нет решения.
        *Подумать над тем, как сделать минимальное количество команд

> [Задача](https://github.com/XYI7I/GeekBrains/tree/main/Geek/JavaStart/lesson1/task3/src/Main.java): Показать набор команд для превращения числа а в число b
Показать хотя бы один набор

        *Подумать над решением задачи 2 рекурсией