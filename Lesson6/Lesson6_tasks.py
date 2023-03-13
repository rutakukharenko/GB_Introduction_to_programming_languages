# Lesson6


def coordinates_of_intersection(b1, k1, b2, k2):
    if k1 == k2:
        print('Lines are parallel!')
    else:
        x = (b2 - b1) / (k1 - k2)
        y = k1 * x + b1
        return x, y


# # Task 41
"""
Задача 41:
Пользователь вводит с клавиатуры M чисел. Посчитайте, сколько чисел больше 0 ввёл пользователь.
0, 7, 8, -2, -2 -> 2
1, -7, 567, 89, 223-> 4
"""
numbers = [int(i) for i in input('Enter numbers separated by spaces: ').split()]
count = 0

for number in numbers:
    if number > 0:
        count += 1

print(f'You entered {count} numbers greater than zero in list: \n'
      f'{numbers}.')

# Task 43
"""
Задача 43:
Напишите программу, которая найдёт точку пересечения двух прямых, заданных уравнениями:
y1 = k1 * x + b1, y2 = k2 * x + b2; 
значения b1, k1, b2 и k2 задаются пользователем.
b1 = 2, k1 = 5, b2 = 4, k2 = 9 -> (-0,5; -0,5)
"""
print('Enter coefficients for 2 lines.')
b1, k1, b2, k2 = int(input('Enter b1: ')), int(input('Enter k1: ')), int(input('Enter b2: ')), int(input('Enter k2: '))

print(f'1st line: y1 = {k1} * x + {b1}. \n'
      f'2nd line: y2 = {k2} * x + {b2}. \n'
      f'Result of intersection: {coordinates_of_intersection(b1, k1, b2, k2)}.')
