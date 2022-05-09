# coding: utf-8

# Основы языка Python.
# Занятие 6. Объектно-ориентированное программирование

# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.
from distlib.compat import raw_input

print(
    "Урок 6. Задание 1.\n\nСоздать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и "
    "метод running (запуск).\nАтрибут реализовать как приватный. В рамках метода реализовать переключение светофора в "
    "режимы: красный, желтый, зеленый.\nПродолжительность первого состояния (красный) составляет 7 секунд, "
    "второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.\nПереключение между режимами должно "
    "осуществляться только в указанном порядке (красный, желтый, зеленый).\nПроверить работу примера, "
    "создав экземпляр и вызвав описанный метод.\nЗадачу можно усложнить, реализовав проверку порядка режимов, "
    "и при его нарушении выводить соответствующее сообщение и завершать скрипт.\n")

from time import sleep
import msvcrt, os, sys, click, keyboard


# from threading import Thread
# from pynput.keyboard import Key, Controller
# from pynput import keyboard

class TrafficLight:
    """
    Traffic light.

    """
    __color = ['Красный', 'Желтый', 'Зеленый']

    def run(self):
        """
        Traffic lights run.

        """
        # The event listener will be running in this block

        i = 0

        print('Для завершения программы нажмите "Ctrl+C" или "Del"\n')
        print('Светофор работает\n')

        try:
            i = 1

            while True:
                print(f'{TrafficLight.__color[i % 3]}\n')

                if i % 3 == 0:
                    sleep(2)
                elif i % 3 == 1:
                    sleep(1)
                elif i % 3 == 2:
                    sleep(2)
                i += 1

        except KeyboardInterrupt:
            print('exit')

TrafficLight = TrafficLight()
TrafficLight.run()

print('***')

# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
# атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод
# расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина * ширина *
# масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см толщины полотна. Проверить
# работу метода. Например: 20м * 5000м * 25кг * 5см = 12500 т
print("Урок 6. Задание 2.")


class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width


class RoadLoad(Road):
    def __init__(self, _length, _width, _mass, _thickness):
        super().__init__(_length, _width)
        self.volume = _mass * _thickness

    def load(self):
        return self._length * self._width * self.volume


r = RoadLoad(5000, 20, 25, 5)
print(f'Масса асфальта, необходимого для покрытия всего дорожного полотна: {int(r.load() / 1000)} т')

print('***')

# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и
# премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В
# классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (
# get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).
print("Урок 6. Задание 3.")


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, lastname, position, wage, bonus):
        super().__init__(name, lastname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')
        # return f'{sum(self._income.values())}'


pers = Position('Elon', 'Reeve Musk', 'Industrial designer', 1000000, 250000)
print(pers.get_full_name())
print(pers.position)
print(f'Итоговая выплата $: {pers.get_total_income()}')

print('***')

# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
# булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
print("Урок 6. Задание 4.")


class Car:
    # atributes
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула на право'

    def turn_left(self):
        return f'{self.name} повернула на лево'

    def show_speed(self):
        return f'Текущая скорость {self.name}: {self.speed} км/ч'

    def police(self):
        if self.is_police:
            return f'{self.name} - этот транспорт принадлежит полицейскому департаменту'
        else:
            return f'{self.name} - гражданское транспортное средство'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость городской машины: {self.name} {self.speed} км/ч.')

        if self.speed > 60:
            return f'Скорость {self.name} выше разрешенной для городского автомобиля.'
        else:
            return f'Скорсть {self.name} в пределах нормы для городского автомобиля.'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость комерческого транспорта {self.name}: {self.speed} км/ч.')

        if self.speed > 40:
            return f'Скорость {self.name} выше разрешенной для комерческого транспорта.'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


audi = SportCar(100, 'красный', 'Audi', False)
zaz = TownCar(30, 'желтый', 'ЗАЗ', False)
gazel = WorkCar(70, 'фиолетовый', 'GazEl', False)
bmw = PoliceCar(110, 'черный', 'BMW', True)

print(f' {zaz.turn_right()}, {audi.stop()}')
print(zaz.show_speed())
print(gazel.turn_left())
print(f'{gazel.go()} со скоростью: {gazel.speed} км/ч. {gazel.show_speed()}')
print(f'{gazel.name} цвет {gazel.color}')
print(f'{audi.name} полицейская машина? {audi.police()}')
print(audi.show_speed())
print(f'{bmw.name}  полицейская машина? {bmw.police()}')
print(bmw.police())
print(bmw.show_speed())

print('***')

# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш),
# Handle (маркер). В каждом из классов реализовать
# переопределение метода draw. Для каждого из классов
# методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет
# описанный метод для каждого экземпляра.

print("Урок 6. Задание 5.")


class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки ручкой'


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки карандашом'


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Вы взяли {self.title}. Запуск отрисовки маркером'


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
print(pen.draw())
print(pencil.draw())
print(handle.draw())

print('Задание выполнено!')
