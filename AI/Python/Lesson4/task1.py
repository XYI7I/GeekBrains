# Основы языка Python
# Урок 4. Полезные инструменты

from sys import argv

# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
# необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных
# значений необходимо запускать скрипт с параметрами.


if len(argv) == 6:
    skript_name, name_file, employee, works_hours, salary_per_hour, premium = argv
    File_object = open(name_file, 'a')
    salary = int(works_hours) * int(salary_per_hour) + int(premium)
    File_object.write(employee + ': ' + str(salary) + ' RUR\n')
    File_object.close()



