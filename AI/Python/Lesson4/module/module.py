def div():
    quo = int(input('Введите число которое надо разделить: '))
    divider = int(input('Введите число на которое надо разделить: '))
    while divider == 0:
        print('Деление на 0 не возмлжно')
        divider = int(input('Введите число на которое надо разделить: '))
    ans = quo / divider
    return ans

def personal_data():
    name = input('Введите Имя: ')
    lastname = input('Введите Фамилию: ')
    year = input('Введите год рождения: ')
    city = input('Введите город проживания: ')
    email = input('Введите e-mail: ')
    phone = input('Введите телефон: ')
    print(name.title(), lastname.title(), year, city.title(), email, phone)