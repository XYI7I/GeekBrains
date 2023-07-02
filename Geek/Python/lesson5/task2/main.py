"""
Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного аргумента, а значение — имя аргумента.
Если ключ не хешируем, используйте его строковое представление.
"""


from collections.abc import Hashable

def create_argument_dict(**kwargs):
    argument_dict = {}
    for key, value in kwargs.items():
        key_hashable = str(key) if not isinstance(key, Hashable) else key
        argument_dict[value] = key_hashable
    return argument_dict

result = create_argument_dict(a=1, b=2, c=3)
print(result)