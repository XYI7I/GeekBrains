"""
Задача: предложить улучшения кода для уже решённых задач с помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
Пример:

[1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

Найти сумму чисел списка стоящих на нечетной позиции

Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
"""

def find_uniq_el(list):
    max_elem = max(list) + 1
    count = [0] * max_elem

    for element in list:
        count[element] += 1

    result = []
    for element in list:
        if count[element] == 1:
            result.append(element)
    return result




list_num = [1, 2, 3, 5, 1, 5, 3, 10]
list_unq1 = [el for el in list_num if list_num.count(el) == 1]
print(list_num)
list_unq = find_uniq_el(list_num)
print(list_unq)
print(list_unq1)



