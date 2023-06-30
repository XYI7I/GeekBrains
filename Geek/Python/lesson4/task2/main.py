"""
Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
"""


def remove_duplicates(lst):
    # Создаем множество из списка, чтобы удалить дубликаты
    unique_set = set(lst)

    # Преобразуем множество обратно в список
    unique_list = list(unique_set)

    return unique_list


# Пример использования
input_list = [1, 2, 2, 3, 4, 4, 5]
result_list = remove_duplicates(input_list)

print("Исходный список:", input_list)
print("Результирующий список без дубликатов:", result_list)