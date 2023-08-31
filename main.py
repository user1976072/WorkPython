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
    
  n = 5
i = 2
a = 1
while i <= n:
    a = a * i
    i = i + 1
print(a)
Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

Input:     5

Output:  6
a = 5
fib1 = 0
fib2 = 1
n = 2
while fib2 < a:
    n = n + 1
    # fib1, fib2 = fib2, fib1 + fib2
    temp = fib2
    fib2 = fib1 + fib2
    fib1 = temp
if fib2 == a:
    print(n)
else:
    print(-1)


    Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю наблюдений за погодой. Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель. Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую синоптикам в работе.
Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках располагается N целых чисел. 
Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в диапазоне от –50 до 50

Input:    6 -> -20 30 -40 50 10 -10
Output: 2
data = [int(i) for i in input("Введите данные: ").split()]
a = 0
m = 0
for i in data:
    if i > 0:
        a += 1
    else:
        if a > m:
            m = a
        a = 0
if a > m:
    m = a
print(m)

"""
"""
data = [int(i) for i in input("Введите данные по арбузам: ").split()]
m1 = data[0]
m2 = data[0]
for mel in data:
    if mel > m1:
        m1 = mel
    elif mel < m2:
        m2 = mel
print(f"Самый большой арбуз {m1}, самый маленький арбуз {m2}")
"""
#Дан список чисел. Определите, сколько в нем встречается различных чисел.

#Input: [1, 1, 2, 0, -1, 3, 4, 4]

#Output: 6
"""
data = [int(i) for i in input ("Введите числа: ").split()]
print(data)

print(len(set(data)))

d = {}
for i in data:
    if i not in d:
        d[i] = 0
    d[i] +=1
print(len(d.keys()))  

"""
#Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо,  K – положительное число.

#Input:   [1, 2, 3, 4, 5] k = 2

#Output:  [4, 5, 1, 2, 3]

#Примечание: Пользователь может вводить значения списка или список задан изначально.
"""
data = [int(i) for i in input ("Введите числа: ").split()]
k = int(input("Введите к:  "))
print(data[-k:] + data[:-k]) 

"""
#Напишите программу для печати всех уникальных значений в словаре. 

#Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}] 

#Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
"""
d = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
s = set()
for data in d:
    for value in data.values():
        s.add(value.strip())
print(s)
"""
#Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим номером) 

#Input: [0, -1, 5, 2, 3]

#Output: 2 (-1 < 5, 2 < 3)

data = [int(i) for i in input ("Введите числа: ").split()]
k = 0
for i in range(1,len(data)):
    if data[i] > data[i-1]:
        k += 1
print(k)
