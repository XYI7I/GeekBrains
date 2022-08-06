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


def dataframe_from_readline_file(file_name, numofvar, encod='utf-8'):
    """
    :param file_name: path of data file - string: 'folder_name/file_name'
    :param numofvar:
    """
    file = open(file_name, 'r', encoding=encod)
    list_of_data = []
    lines = file.readlines()
    file.close()
    for line in lines:
        list_of_data.append(line.strip())
    # print(list_of_data)
    dict_df = {}
    for i in range(numofvar):
        key = input('Input name of value: ')
        dict_df[key] = list_of_data[i::numofvar]

    # print(dict_df)
    data_frame = pd.DataFrame.from_dict(dict_df)
    return data_frame


def add_data_df(data_frame):
    """

    :param data_frame:
    """
    list = []
    for i in range(len(data_frame.columns)):
        list.append(input(f'Input {data_frame.columns[i]}: '))
    data_frame.loc[len(data_frame)] = list
    print(data_frame)


def convert_to_txt(data_frame):
    """

    :param data_frame:
    """
    print('test')



df = pd.read_csv('data.csv', ';', encoding='windows-1251')
data_val = df.loc[df['name'] == 'Имя_1']['phone']
print(data_val)
print(df['phone'])

df1 = dataframe_from_readline_file('data', 4)
add_data_df(df1)
# df.to_csv('data.csv')
