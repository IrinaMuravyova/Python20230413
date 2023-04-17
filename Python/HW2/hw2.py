"""Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
а некоторые – гербом. Определите минимальное число монеток, которые нужно 
перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть """

"""
n = int(input("Input count of coins: "))
eagle = int(input("Input count of coins, that lie on table eagle up: "))
if eagle < (n - eagle):
    print(f"You need to flip {eagle} coins")
else: print(f"You need to flip {n-eagle} coins")
"""

"""
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y 
(X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
 Он называет сумму этих чисел S и их произведение P. 
 Помогите Кате отгадать задуманные Петей числа. """

"""
sum = int(input("Input sum of x and y: "))
mult = int(input("Input multiplication of x and y: "))
for x in range(1001):
    for y in range(1001):
        if x + y == sum and x * y == mult:
            print(f"x = {x}, y = {y}")
            break
"""

"""
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
не превосходящие числа N. """

"""
n = int(input("Input whole number: "))
k = 1
while 2**k < n:
    print(f"{2**k} ")
    k+=1 
"""