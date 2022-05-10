class User(object):

    def __init__(self, login, email=None, password=None):
        self.username = login  # public
        self.__password = password  # private
        self.email = email

    # def __show_password(self):      # private method or
    def show_password(self):  # public method
        print(self.__password)

    def set_email(self, new_email):
        self.email = new_email

    def __str__(self):
        return f'User - {self.username}'


class Admin(User):

    def set_email(self, new_email):
        super().set_email(new_email=new_email)
        print('e-mail')

    def del_photo(self):
        print('Delete photo')

    def __str__(self):
        return f'Root - {self.username}'


class Number:

    def __init__(self, number):
        self.value = number

    def __add__(self, other):
        if isinstance(other, Number):
            return self.value + other.value
        else:
            return self.value + other

    def __sub__(self, other):
        if isinstance(other, Number):
            return self.value - other.value
        else:
            return self.value - other

    def __str__(self):
        return f'Number is - {str(self.value)}'

    def __call__(self, *args, **kwargs):
        return 'Call me!'


my_num = Number(5)
print(my_num + 3)

my_user = User('admin', 'admin@mail.ru', '12345')
other_user = User(login='root', email='root@mail.ru')
admin = Admin(login='administrator')

print(my_user.username)
# print(my_user.password)
print(my_user.show_password())
print(my_user.email)
print(my_user.set_email('admin@google.com'))
print(my_user.email)

print(other_user)
print(other_user.email)
other_user.show_password()
admin.del_photo()


class Shape:
    def __init__(self, color, param_1, param_2):
        self.__color = color
        self.param_1 = param_1
        self.param_2 = param_2

    def square(self):
        return self.param_1 * self.param_2


class Rectangle(Shape):
    def __init__(self, color, param_1, param_2, rectangle_p):
        super().__init__(color, param_1, param_2)
        self.rectangle_p = rectangle_p

    def get_r_p(self):
        return self.rectangle_p


class Triangle(Shape):
    def __init__(self, color, param_1, param_2, triangle_p):
        super().__init__(color, param_1, param_2)
        self.triangle_p = triangle_p

    def get_t_p(self):
        return self.triangle_p


r = Rectangle("white", 10, 20, True)
# print(r.color)
print(r.square())
print(r.get_r_p())
t = Triangle("red", 30, 40, False)
# print(t.color)
print(t.square())
print(t.get_t_p())


class ParentClass:
    def __init__(self):
        print('Constructor parent')

    def my_method(self):
        print('Method ParentsClass')


my_list = [30, 105.6, 'text', True]
for elem in my_list:
    print(elem)


class IterObj:
    def __init__(self, start, stop):
        self.start = start - 1
        self.stop = stop

    def __next__(self):
        self.start += 1
        if self.start < self.stop:
            return self.start
        else:
            raise StopIteration

    def __iter__(self):
        return self


for elem in IterObj(2, 9):
    print(elem)


class Auto:
    auto_color = 'red'

    @property
    def get_color(self):
        return self.auto_color


my_auto = Auto()
print(my_auto.auto_color)
print(my_auto.get_color)


class Auto:
    # конструктор класса Auto
    def __init__(self, year):
        # Инициализация свойств.
        self.year = year

    # создаем свойство года
    @property
    def year(self):
        return self.__year

    # сеттер для создания свойств
    @year.setter
    def year(self, year):
        if year < 2000:
            self.__year = 2000
        elif year > 2019:
            self.__year = 2019
        else:
            self.__year = year

    def get_auto_year(self):
        return f"Автомобиль выпущен в {str(self.year)} году"


a = Auto(2009)
print(a.get_auto_year())
