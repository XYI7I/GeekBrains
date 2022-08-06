"""
1: Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.

под форматами понимаем структуру файлов, например:в файле на одной строке хранится одна часть записи, пустая строка - разделитель
Фамилия_1
Имя_1
Телефон_1
Описание_1
Фамилия_2
Имя_2
Телефон_2
Описание_2
и т.д.в файле на одной строке хранится все записи, символ разделитель - ;**
Фамилия_1,Имя_1,Телефон_1,Описание_1
Фамилия_2,Имя_2,Телефон_2,Описание_2
и т.д.
Предполагается возможность вывода всех контактов, поиска контакта по имени, добавления и удаления контакта

"""

import pandas as pd


def dataframe_from_readline_file(filename, encod='windows-1251'):
    """

    :param filename: path of data file - string: 'folder_name/file_name'
    :param encod: encoding format of data file - string: 'windows-1251', 'utf-8' e.t.c
    """
    file = open(filename, 'r', encoding=encod)

    while True:
        # считываем строку
        line = file.readline()
        # прерываем цикл, если строка пустая
        if not line:
            break
        # выводим строку
        print(line.strip())

    # закрываем файл
    file.close


df = pd.read_csv('data.csv', ';', encoding='windows-1251')

print(df.loc[df['name'] == 'Имя_1']['phone'])

# df.to_csv('data.csv')
