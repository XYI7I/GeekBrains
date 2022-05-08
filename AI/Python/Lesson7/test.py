class User(object):

    def __init__(self, login, email=None):
        self.username = login  # public
        self.__password = 'abc'  # private
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
        self.value += other
        return self.value

    def __sub__(self, other):
        self.value -= other
        return self.value

    def __str__(self):
        return str(self.value)


my_num = Number(5)
print(my_num + 3)

my_user = User(login='admin', email='admin@mail.ru')
other_user = User(login='root', email='root@mail.ru')
admin = Admin(login='administrator')

print(my_user.username)
print(my_user.email)
print(my_user.set_email('admin@google.com'))
print(my_user.email)

print(other_user)
print(other_user.email)
other_user.show_password()
admin.del_photo()