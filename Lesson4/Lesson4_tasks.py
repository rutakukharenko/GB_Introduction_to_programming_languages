# Lesson4
import random

# Task 25
"""
Задача 25:
Напишите цикл, который принимает на вход два числа (A и B) и возводит число A в натуральную степень B.
"""
def exponentiation(number, exp):
    result = 1
    if type(number) is not float:
        print('Please enter a number.')
    if type(exp) is not int:
        print('The power of number must be a natural number!')
    else:
        for i in range(1, exp + 1):
            result *= number
        return result


number, exp = float(input('Enter a number: ')), int(input('Enter a natural number: '))
print(f'{number} ** {exp} = {exponentiation(number, exp)}')

# Task 27
"""
Задача 27:
Напишите программу, которая принимает на вход число и выдаёт сумму цифр в числе.
"""
def sum_of_digits(number):
    sum = 0
    if type(number) is not int:
        print('The number must be a natural number!')
    else:
        while number != 0:
            last_digit = number % 10
            sum += last_digit
            number = number // 10
        return sum


number = int(input('Enter a natural number: '))
print(f'Sum of digits in {number}: {sum_of_digits(number)}')

# Task 29
"""
Задача 29:
Напишите программу, которая задаёт массив из 8 элементов и выводит их на экран.
"""
def random_list(n, start, stop):
    if start > stop:
        print('The start of the range must be less than the end!')
    else:
        items = [random.randint(start, stop) for _ in range(n)]
        return items


n, start, stop = int(input('Enter amount of elements: ')), int(input('Enter a start of range: ')), int(
    input('Enter an end of range: '))
print(f'Generated random list: \n'
      f'{random_list(n, start, stop)}')
