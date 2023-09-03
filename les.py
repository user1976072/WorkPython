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

engl = {
    'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
    'D': 2, 'G': 2,
    'B': 3, 'C': 3, 'M': 3, 'P': 3,
    'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
    'K': 5,
    'J': 8, 'X': 8,
    'Q': 10, 'Z': 10
}
russ = {
    'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
    'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
    'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
    'Й': 4, 'Ы': 4,
    'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
    'Ш': 8, 'Э': 8, 'Ю': 8,
    'Ф': 10, 'Щ': 10, 'Ъ': 10
}
word = input("Введите слово: ")
word = word.upper()
sum = 0
for i in word:
    if i in engl:
        sum += engl[i]
    elif i in russ:
        sum += russ[i]      
print(f"Стоймость слова '{word}' составляет {sum} очков.")