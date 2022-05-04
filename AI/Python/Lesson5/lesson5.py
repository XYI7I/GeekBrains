#  coding: utf-8

# Основы языка Python.
# Занятие 5. Работа с файлами

# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
print("Урок 5. Задание 1.")

str_data = '!'
with open("my_data.txt", 'w', encoding="utf-8") as f_obj:
    while str_data != '':
        str_data = input('Введите данные: ')
        f_obj.writelines(str_data + '\n')

f_obj.close()

print('***')

# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
print("Урок 5. Задание 2.")

i = 0
with open("text.txt", 'r', encoding="utf-8") as f_obj:
    for line in f_obj:
        word = line.split()
        print(f'количества слов в строке: {len(word)}')
        i += 1
    print('количества строк =', i)

f_obj.close()

print('***')

# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
print("Урок 5. Задание 3.")

Sum_w = 0
i = 0
with open("staff.txt", 'r', encoding="utf-8") as f_obj:
    for line in f_obj:
        pers = line.split()
        Sum_w = Sum_w +  int(pers[1])
        i += 1
        if int(pers[1]) < 20000:
            print(f'сотрудник {pers[0]} имеет оклад менее 20 тыс')
    print(f'Средняя величина дохода сотрудников: {Sum_w / i}')

f_obj.close()

print('***')

# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
print("Урок 5. Задание 4.")

num_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_line = []
with open("numerals.txt", 'r', encoding="utf-8") as f_obj:
    for line in f_obj:
        line = line.split()
        new_line.append(num_dict[line[0]] + ' ' + line[1] + ' ' + line[2] + '\n')
        with open("numerals_new.txt", 'w', encoding="utf-8") as f_obj_new:
            f_obj_new.writelines(new_line)

print('***')

# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
print("Урок 5. Задание 5.")

with open("my_data_num.txt", 'w', encoding="utf-8") as f_obj:
    num_data = input('Введите набор чисел, разделенных пробелами: ')
    f_obj.write(num_data)

print('Фаил создан')

with open("my_data_num.txt", 'r', encoding="utf-8") as f_obj:
    res = 0
    number = f_obj.readline().split()
    for el in range(len(number)):
        res = res + int(number[el])
with open("my_data_num.txt", 'a', encoding="utf-8") as f_obj:
    f_obj.write("\nСумма: " + str(res))
    print(f'Сумма всех чисел: {res}')

print('***')

# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —

# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
print("Урок 5. Задание 6.")

subj = {}
with open("lessons.txt", 'r', encoding="utf-8") as f_obj:
    for line in f_obj:
        subject, lecture, practice, lab = line.split()
        subj[subject] = int(lecture) + int(practice) + int(lab)
        print(f'Общее количество часов по предмету {subject} {subj[subject]}')

print(subj)
print('***')


# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

# Подсказка: использовать менеджеры контекста.
print("Урок 5. Задание 7.")

import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('firm.txt', 'r', encoding="utf-8") as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя - {prof_aver:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    pr = {'средняя прибыль': round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль каждой компании - {profit}')

with open('firm.json', 'w', encoding="utf-8") as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')

print('Задание выполнено!')