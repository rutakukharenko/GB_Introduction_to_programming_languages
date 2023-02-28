# Lesson2
# Task 10
"""
Задача 10:
Напишите программу, которая принимает на вход трёхзначное число и на выходе показывает вторую цифру этого числа.
"""
number = int(input('Enter a number: '))
entered_number = number
number_list = []

if 100 <= number <= 999:
    while number != 0:
        last_digit = number % 10
        number_list.append(last_digit)
        number = number // 10
    print(f'{number_list[1]} - is second digit from number {entered_number}.')
else:
    print(f'{entered_number} - is not a three-digit number. Please enter a three-digit number.')

# Task 13
"""
Задача 13:
Напишите программу, которая выводит третью цифру заданного числа или сообщает, что третьей цифры нет.
"""
number = int(input('Enter a number: '))

if 100 <= number <= 999:
    last_digit = number % 10
    print(f'{last_digit} - is the last digit from number {number}.')
else:
    print(f'{number} - is not a three-digit number. Please enter a three-digit number.')

# Task 15
"""
Задача 15:
Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
"""
day_week_number = int(input('Enter a digit: '))
day_week_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

if 1 <= day_week_number <= 7:
    if day_week_number == 6 or day_week_list == 7:
        print(f'This day of the week is a weekend day! It\'s {day_week_list[day_week_number - 1]}.')
    else:
        print(f'This day of the week is a week day! It\'s {day_week_list[day_week_number - 1]}.')
else:
    print(f'The entered number {day_week_number} does not belong to the interval: [1, 7].')
