# решение к 1 семинару
# Задание 1
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

# Задание 2
n = 597

if 100 <= n <= 999:
    
    digit1 = n // 100  
    digit2 = (n // 10) % 10 
    digit3 = n % 10 

    res = digit1 + digit2 + digit3

    print(res)
else:
    print("Это не трехзначное число.")
           