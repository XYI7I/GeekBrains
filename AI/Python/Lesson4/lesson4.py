# Основы языка Python
# Урок 4. Полезные инструменты

# import module.module

from sys import argv

from Lesson4 import module

# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
# необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных
# значений необходимо запускать скрипт с параметрами.

if len(argv) == 6:
    skript_name, name_file, employee, works_hours, salary_per_hour, premium = argv
    File_object = open(name_file, 'a')
    salary = int(works_hours) * int(salary_per_hour) + int(premium)
    File_object.write(employee + ': ' + str(salary) + ' RUR\n')
    File_object.close()


# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего
# элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка
# использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123]
print('Task 2\n')

N = int(input('N = '))
list = module.gen_randint_list(N)
new_list = module.compare(list)

print(list)
print(new_list)

print('\n')
# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.
print('Task 3\n')

print([el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0])

print('\n')
# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел,
# соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения задания
# обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]



# 5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти
# четные числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов
# списка.
# Подсказка: использовать функцию reduce().



# 6. Реализовать два небольших скрипта: а) итератор, генерирующий целые числа, начиная с указанного, б) итератор,
# повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл
# не должен быть бесконечным. Необходимо предусмотреть условие его завершения. Например, в первом задании
# выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. Во втором также необходимо
# предусмотреть условие, при котором повторение элементов списка будет прекращено.



# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом:
# for el in fact(n). Функция отвечает за получение факториала числа, а в цикле необходимо выводить только
# первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n.
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

