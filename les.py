# Решение ДЗ к 4 семинару

# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))

a = set()
for i in range(n):
    d = int(input(f"Введите элемент {i + 1} первого множества: "))
    a.add(d)

b = set()
for i in range(m):
    d = int(input(f"Введите элемент {i + 1} второго множества: "))
    b.add(d)
intersection = a.intersection(b)
s = sorted(list(intersection))
print("Числа, которые встречаются в обоих множествах:", s)

# Задача 24
# В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

# n = int(input("Введите количество кустов: "))

# a = []
# for i in range(n):
#     d = int(input(f"Введите урожайность для куста {i + 1}: "))
#     a.append(d)
# max_d = 0
# for i in range(n):
#     c = 0  
#     c = a[i] + a[(i + 1) % n] + a[(i + 2) % n]
#     if c > max_d:
#         max_d = c

# print("Максимальная урожайность:", max_d)

# Решение заданий ко 2 семинару
# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, 
# которые нужно перевернуть
"""
monet = input("Введите монеты где ноль это решка и единицы это герб: ")

zero = 0
one = 0

for digit in monet:
    if digit == '0':
        zero += 1
    elif digit == '1':
        one += 1

mincount = min(zero, one)

print(f"Минимальное количество монет, которые нужно перевернуть: {mincount}")
"""
# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
"""
s = int(input("Введите cумму чисел < 2000: "))
p = int(input("Введите произведение чисел < 1000000: "))

x = 1
y = s - x

while x <= s // 2 and x * y != p:
    x += 1
    y = s - x

if x * y == p:
    print(f"Найдены натуральные числа X и Y: X = {x}, Y = {y}")
else:
    print("Невозможно найти подходящие натуральные числа X и Y для заданных S и P.")


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
"""
"""
n = int(input("Введите число N: "))
stepen = 1

while stepen <= n:
    print(stepen, end=' ')
    stepen *= 2
"""
# Решение задач к 3 семинару (автопроверка)
# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
# Найдите количество и выведите его.
"""
list_1 = [int(i) for i in input ("Введите числа: ").split()]
k = 3
print(list_1.count(k))
"""
# Требуется найти в массиве 
# list_1 самый близкий по величине элемент к заданному числу k и вывести его.
"""
list_1 = [int(i) for i in input ("Введите числа: ").split()]
k = 6
closest = list_1[0]
min_d = abs(list_1[0] - k)
for num in list_1:
    d = abs(num - k)
    if d < min_d:
        min_d = d
        closest = num
print(f"Самый близкий элемент к {k} в массиве: {closest}")  
"""
# Определить стоимость слова

# engl = {
#     'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
#     'D': 2, 'G': 2,
#     'B': 3, 'C': 3, 'M': 3, 'P': 3,
#     'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
#     'K': 5,
#     'J': 8, 'X': 8,
#     'Q': 10, 'Z': 10
# }
# russ = {
#     'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
#     'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
#     'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
#     'Й': 4, 'Ы': 4,
#     'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
#     'Ш': 8, 'Э': 8, 'Ю': 8,
#     'Ф': 10, 'Щ': 10, 'Ъ': 10
# }
# word = input("Введите слово: ")
# word = word.upper()
# sum = 0
# for i in word:
#     if i in engl:
#         sum += engl[i]
#     elif i in russ:
#         sum += russ[i]      
# print(f"Стоймость слова '{word}' составляет {sum} очков.")
# 