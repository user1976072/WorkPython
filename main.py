# решение к 1 семинару
# Задание 4 про шоколадку
"""
a = int(input("Введите ширину шоколадки a: "))
b = int(input("Введите высоту шоколадки b: "))
c = int(input("Введите количество долек c: "))

if (a == 1 and b == 1 and c != 1) or c > a * b:
    print("no")
else:
    if c % a == 0 or c % b == 0:
        print("yes")
    else:
        print("no")
"""

# Задание 1 сложить все цифры числа
"""
n = 597

if 100 <= n <= 999:
    
    digit1 = n // 100  
    digit2 = (n // 10) % 10 
    digit3 = n % 10 

    res = digit1 + digit2 + digit3

    print(res)
else:
    print("Это не трехзначное число.")

""" 
# Задание 2
#Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали n журавликов.
#Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
#Выведите кортеж из количества журавликов, сделанных Петей, Катей и Сережей.
"""
n = int(input("Введите количество журавликов: "))

if n % 6 == 0:
    x = n // 6
    ps = x
    k = 4 * x
    print((ps), (k), (ps))
else:
    print("Невозможно разделить журавликов равномерно.")     
"""

# Задание 3
#Вам требуется написать программу, которая проверяет счастливость билета с номером n и выводит на экран yes или no.

n = int(input("Введите 6 значное число: "))

a = n // 100000
b = n // 10000 % 10
c = n // 1000 % 10
d = n // 100 % 10
e = n // 10 % 10
f = n % 10

if a + b + c == d + e + f:
    print("yes")
else:
    print("no")
    