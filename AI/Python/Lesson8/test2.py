class Auto:
    color = 'red'

    def get_color(self):
        return self.color

    @staticmethod
    def get_info(arg1, arg2):
        print(f'Info about auto {arg1}, {arg2}')

    @classmethod
    def change_color(cls, new_color):
        cls.color = new_color


auto = Auto()
new_auto = Auto()
print(auto.color)

auto.change_color('black')
print(auto.color)
print(new_auto.color)