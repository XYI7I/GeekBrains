# coding: utf-8

# Основы языка Python.
# Занятие 1. Знакомство с Python


import os
import sys
import shutil
import random
import psutil


print("Урок 1. Задание 1. Часть 1.")

numeric = 10
str = "Привет!"
print(numeric)
print(str)

print("Урок 1. Задание 1. Часть 2.")
time = input("Введите время в секундах: ")
time = int(time)
print(time)
print("Время:",time // 3600,":",time // 60 % 60,":",time % 60)

print("Урок 1. Задание 1. Часть 3.")
n = input("Введите число n: ")
sum = int(n) + int(n+n) + int(n+n+n)
print(sum)

print("Урок 1. Задание 1. Часть 4.")
n = input("Введите введите целое положительное число : ")

print("Урок 1. Задание 1. Часть 5.")
proceeds = input("Введите сумму выручки фирмы: ")
costs = input("Введите сумму издержек фирмы: ")

print("Урок 1. Задание 1. Часть 6.")
n = input("Введите введите целое положительное число : ")
