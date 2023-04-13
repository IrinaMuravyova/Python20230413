"""
Задача 2: Найдите сумму цифр трехзначного числа.
*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |
"""

"""
num = int(input("Input three-digit number: "))
#sum = int(num/100)+int(num/10)%10+num%10
print(f'Sum of digits = {int(num/100)+int(num/10)%10+int(num%10)}')
"""

"""
Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
Вместе они сделали S журавликов. 
Сколько журавликов сделал каждый ребенок, если известно, 
что Петя и Сережа сделали одинаковое количество журавликов, 
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
*Пример:*

6 -> 1  4  1
24 -> 4  16  4
60 -> 10  40  10
"""

"""
sum = int(input("Input common count of crane:"))
k = int(sum/6)
print(f"Petr made {k} cranes, Kate made {4*k} cranes, Serg made {k} cranes.")
"""

"""
Задача 6: Вы пользуетесь общественным транспортом? 
Вероятно, вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, 
где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
Вам требуется написать программу, которая проверяет счастливость билета.
*Пример:*

385916 -> yes
123456 -> no
"""

"""
ticketNumber = int(input("Input number of ticket: "))
if  len(str(ticketNumber)) != 6:
    print("Number is wrong. Enter six digit's number.")
elif int(ticketNumber/100000)+int(ticketNumber/10000%10)+int(ticketNumber/1000%10) == int(ticketNumber%1000/100)+int(ticketNumber%100/10)+int(ticketNumber%10):
        print(f'{ticketNumber} -> yes')
else: 
    print(f'{ticketNumber} -> no')
"""

"""
Задача 8: Требуется определить, можно ли от шоколадки 
размером n × m долек отломить k долек, 
если разрешается сделать один разлом по прямой между дольками 
(то есть разломить шоколадку на два прямоугольника).
*Пример:*

3 2 4 -> yes
3 2 1 -> no
"""
"""
print("Input below size of chocolate n x m.")
n = int(input("n = "))
m = int(input("m = "))
k = int(input("Input count of parts, that you need: "))
if k < m*n and (k%m==0 or k%n==0):
    print(f"{n} {m} {k} -> yes")
else: print(f"{n} {m} {k} -> no")
"""