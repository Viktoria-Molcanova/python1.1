//Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

a1 = int(input())
d = int(input())
n = int(input())
for i in range(n):
print(a1 + i * d)

//Задача 32:Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
  
from random import randint
Array=[]
for i in range(20):
    Array.append(randint(0, 5))
print(Array)
print("Введите минимальное число: ")
min_number = int(input())
print("Введите максимальное число: ")
max_number = int(input())
for i in range(len(Array)):
    if min_number <= Array[i] <= max_number:
        print(i)
