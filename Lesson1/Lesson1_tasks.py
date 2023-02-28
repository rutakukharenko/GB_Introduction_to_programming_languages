# Lesson 1
# Task 2
"""
Задача 2:
Напишите программу, которая на вход принимает два числа и выдаёт, какое число большее, а какое меньшее.
"""
num1, num2 = float(input('Input first number: ')), float(input('Input second number: '))
if num1 == num2:
    print(f'The entered numbers are equal: {num1}.')
else:
    print(f'Minimum: {min(num1, num2)}.')
    print(f'Maximum: {max(num1, num2)}.')

# Task 4
"""
Задача 4:
Напишите программу, которая принимает на вход три числа и выдаёт максимальное из этих чисел.
"""
numbers = [float(input('Input the number: ')) for _ in range(3)]
print(f'Maximum: {max(numbers)}.')

# Task 6
"""
Задача 6:
Напишите программу, которая на вход принимает число и выдаёт, 
является ли число чётным (делится ли оно на два без остатка).
"""
number = int(input('Input the number: '))

if number % 2 == 0:
    print(f'Entered number {number} - is even.')
else:
    print(f'Entered number {number} - is odd.')


# Task 8
"""
Задача 8:
Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.
"""
number = int(input('Input the number: '))

for i in range(1, number + 1):
    if i % 2 == 0:
        print(i, end=' ')