#Задача №37.Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.

def reverse(n: int) -> None:
    if n == 0:
        return print('')
    print("Введите число ")
    k = int(input())
    reverse(n - 1)
    return print(k)
print("Введите общее количество чисел")
n = int (input())
reverse(n)

#Задача №35. Решение в группах
#Напишите функцию, которая принимает одно число и проверяет, является ли оно простым Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)

def is_prime(a):
    if a % 2 == 0:
        return a == 2
    x = 3
    while x * x <= a and a % x != 0:
        x += 2
    return x * x > a

print(is_prime(int(input("Введите число: "))))
