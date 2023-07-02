"""
Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список.
"""

import random

balance = 0
transactions = []


def deposit(amount):
    global balance
    balance += amount
    transactions.append(f"Пополнение: +{amount} у.е.")


def withdraw(amount):
    global balance
    if balance >= amount:
        fee = max(30, min(0.015 * amount, 600))
        balance -= (amount + fee)
        transactions.append(f"Снятие: -{amount} у.е. (комиссия: {fee} у.е.)")
    else:
        print("Недостаточно средств на счете!")


def print_balance():
    global balance
    print(f"Текущий баланс: {balance} у.е.")


def tax_check():
    global balance
    if balance >= 5_000_000:
        tax = 0.1 * balance
        balance -= tax
        transactions.append(f"Налог на богатство: -{tax} у.е.")


def atm_program():
    operations_count = 0

    while True:
        print("Выберите действие:")
        print("1. Пополнить счет")
        print("2. Снять со счета")
        print("3. Выйти")
        choice = input("Введите номер действия: ")

        if choice == "1":
            amount = int(input("Введите сумму для пополнения (кратную 50): "))
            if amount % 50 == 0:
                deposit(amount)
                operations_count += 1
                if operations_count % 3 == 0:
                    balance *= 1.03
                tax_check()
            else:
                print("Сумма пополнения должна быть кратной 50!")
        elif choice == "2":
            amount = int(input("Введите сумму для снятия (кратную 50): "))
            if amount % 50 == 0:
                withdraw(amount)
                operations_count += 1
                if operations_count % 3 == 0:
                    balance *= 1.03
                tax_check()
            else:
                print("Сумма снятия должна быть кратной 50!")
        elif choice == "3":
            break
        else:
            print("Неверный выбор! Повторите попытку.")

        print_balance()


# Тестовый пример работы программы
atm_program()
print("История операций:")
for transaction in transactions:
    print(transaction)