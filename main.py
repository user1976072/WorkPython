import os

NAME_FILE = "Телефонный справочник.txt"


def main():

    """если есть файл, то его считать, если нет, то пустой список
    вывести меню и меню обработать в цикле"""
    data = {}
    if os.path.exists(NAME_FILE):
        with open(NAME_FILE) as f:
            for line in f.readlines():
                if line:
                    #print(line.split("\t"))
                    name, num = line.split("\t")
                    data[name] = num
    else:
        with open(NAME_FILE, "w") as f:
            pass

    while True:
        while True:
        
            print("1. Ввести данные")
            print("2. Поиск")
            print("3. Выход")
            user_choice = input("Введите: ") 
            if user_choice not in ["1", "2", "3"]:
                print("Ошибка")
            else: 
                break
        match user_choice: 
            case "1":
                data = input_data(data)
            case "2":
                search_data(data)
            case "3":
                print("Выход")
                if not data: 
                    return
                with open(NAME_FILE, "w") as f:
                    for name in data:
                        print(f"{name}\t{data[name]}", file=f)
                return
            

def input_data(data):
    name = input("Введите ФИО: ")
    if name and len(name.split() ) == 3: 
        num = input("Введите номер телефона: ")

        if num and num.isdigit():

            data[name.replace("\t"," ")] = num
            return data
    print("Неверный ввод данных")
    return data

def search_data(data):
    user_input = input("Ввести данные для поиска: ")
    while True:
        
            print("1. Найти фамилию")
            print("2. Найти имя")
            print("3. Найти отчество")
            print("4. Найти номер телефона")
            print("5. Вернуться в меню")
            user_choice = input("Введите: ") 
            if user_choice not in ["1", "2", "3", "4", "5"]:
                print("Ошибка")
            else: 
                break
    match user_choice: 
            case "1":
                for key in data:
                    name1, name2, name3 = key.split()
                    if name1 == user_input:
                        print(f"{key} {data[key]}")
                    
            case "2":
               for key in data:
                    name1, name2, name3 = key.split()
                    if name2 == user_input:
                        print(f"{key} {data[key]}")
            case "3":
               for key in data:
                    name1, name2, name3 = key.split()
                    if name3 == user_input:
                        print(f"{key} {data[key]}")
            case "4":
               for key, value in data.items():
                   if value == user_input:
                      print(f"{key} {data[key]}") 
              
            case "5":
                print("Выход")
                
                return    

if __name__ == "__main__":
    main()

    



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
#Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество 
# элементов массива, больших предыдущего (элемента с предыдущим номером) 

#Input: [0, -1, 5, 2, 3]

#Output: 2 (-1 < 5, 2 < 3)
"""
data = [int(i) for i in input ("Введите числа: ").split()]
k = 0
for i in range(1,len(data)):
    if data[i] > data[i-1]:
        k += 1
print(k)
"""
# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# sp = input("enter symbols: ").split()
# d ={}
# for letter in sp:
#     if letter not in d:
#         count = 0
#         d[letter] = count
#         print(letter, end = ' ')
        
#     else:
#         d[letter] +=1
#         print("{}_{}" .format(letter, d[letter]), end=" ")
# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells

# Output: 13
# string = ''' She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells'''.lower().replace("."," ")
# spl = string.split()
# f = set(spl)
# print(f)
# print(len(f))


# listq = [7, 15, 5, 63, 89]
# listq.sort()
# #list2 = sorted(listq, reverse = True)
# print(listq)

# рекурсия фибоначи
# def fib(n):
    
#     if n <= 1:
#         return 1
#     return fib(n-1)+fib(n-2)


# print(fib(7))

# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
#a = []
# n = int(input())
# for i in range(n):
#     a.append(int(input()))
# print(a)

# x = max(a)
# y = min(a)
# for i in range(len(a)):
#     if a[i] == x:
#         a[i] = y

# print(a)
# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

# Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число)

# Input: 5
# def is_prime(n, delt =2):
#     if n%delt ==0:
#         return False
#     if delt> n//2:
#         return True
    
#     return is_prime(n, delt + 1)


# print(is_prime(18))
# Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).

# Input:    2 -> 3 4

# def rev(m, nums):
#     if m < 0:
#         return
#     else:
#         if m == len(nums):
#             m = m-1
#         print(nums[m], end = ' ')
#         rev(m-1, nums)


# n = 3
# numbers = input()
# rev(n, numbers)
# Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве. Пользователь вводит  число N - количество элементов в первом массиве, затем N чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива
# a = [int(i) for i in input("введите а : ").split() ]
# b = [int(i) for i in input("введите b : ").split()]
# c = []
# for j in a:
#     if j not in b:
#         c.append(j)
# print(c)



# m = set(a)
# n = set(b)
# s = m-n
# v = []
# print(s)
# for k in a:
#     if k in s:
#         v.append(k)
# print(v)

#Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала вводится число N — количество элементов в массиве  Далее записаны N чисел — элементы массива. Массив состоит из целых чисел. 
# a = []
# c = []
# count = 0
# for i in range(int(input())):
#     a.append(int(input()))
# for j in range(1, len(a)-1):
#     if a[j] > a[j-1] and a [j] > a[j+1]:
#         c.append(a[j])
#         count+=1
# print(c)
# print(count)

# # Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. Вводится список чисел. Все числа списка находятся на разных строках.
# a = []
# for k in range(int(input())):
#     a.append(int(input()))
# d = {}
# for i in a:
#     if i not in d:
#         d[i] = 0
#     d[i] +=1
# print(d)
# count = 0
# for value in d.values():
#     count+= value // 2
# print(count)


# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа получает на вход одно натуральное число k, не превосходящее 105. Программа должна вывести  все пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).
# def get_sum(n):
#     s = 1
#     for i in range(2,int(n**0.5)+1):
#         if n%i == 0:
#             s+=i
#             s+= n//i
#     return s

# k = 1000
# result = []
# for i in range(1,k+1):
#     if i not in result:
#         a = get_sum(i)
#         if i != a and a <= k and get_sum(a) == i:
#             result.append(i)
#             result.append(a)
# print(result)

# Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.
# Пример ввода и вывода данных представлены на следующем слайде


# values = [1, 23, 42, ‘asdfg’]
# transformed_values = list(map(trasformation, values))
# if values == transformed_values:
#     print(‘ok’)
# else:
#     print(‘fail’)

# Вывод: 
# ok

# transformation = lambda x: x
# values = [1, 23, 42, "asdfg"]
# transformed_values = list(map(transformation, values))
# if values == transformed_values:
#     print("ok")
# else:
#     print("fail")

# def transformation(x):
#     return x
# values = [1, 23, 42, "asdfg"]
# transformed_values = list(map(transformation, values))
# print(transformed_values)

# Задача про орбиты 
# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна

# import math

# def find_farthest_orbit(orbits):
#     max_area = max([math.pi * a * b for a, b in orbits if a != b])
#     #
#     # max_area = 0
#     # a_max, b_max = 0, 0
#     # for a, b in orbits:
#     #     area = math.pi * a * b
#     #     if area > max_area and a != b:
#     #         max_area = area
#     #         a_max, b_max = a, b
#     #return a_max, b_max
#     return [(a, b) for a, b in orbits if math.pi * a * b == max_area]

# #orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

def same_by(characteristic, objects):
    # if not objects:  # if objects == []
    #     return True
    # s0 = characteristic(objects[0])
    # for object in objects[1:]:
    #     s = characteristic(object)
    #     if s != s0:
    #         return False
    #all([True, True, True]) = True
    #all(True, False, True) = False
    return all([s == characteristic(objects[0]) if objects else True for s in map(characteristic, objects)])
    #return True