# Lesson3
# Task 19
"""
Задача 19:
Напишите программу, которая принимает на вход пятизначное число и проверяет, является ли оно палиндромом.
14212 -> нет
12821 -> да
23432 -> да
"""
number = input('Enter a number: ')

if not number.isdigit():
    print('Please enter a number.')
else:
    if number == number[::-1]:
        print(f'{int(number)} - is a palindrome!')
    else:
        print(f'{int(number)} - is not a palindrome.')

# Task 21
"""
Задача 21:
Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 3D пространстве.
A (3,6,8); B (2,1,-7), -> 15.84
A (7,-5, 0); B (1,-1,9) -> 11.53
"""
a = [int(i) for i in input('Enter 3 coordinates of point A separated by a space: ').split()]
b = [int(i) for i in input('Enter 3 coordinates of point B separated by a space: ').split()]

if len(a) != 3 or len(b) != 3:
    print('Error in the number of points!')
else:
    distance = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2 + (b[2] - a[2]) ** 2) ** 0.5
    print(f'distance between points A and B in 3D space: {round(distance, 2)}')

# Task 23
"""
Задача 23:
Напишите программу, которая принимает на вход число (N) и выдаёт таблицу кубов чисел от 1 до N.
3 -> 1, 8, 27
5 -> 1, 8, 27, 64, 125
"""
cubes = [i ** 3 for i in range(1, int(input('Enter a number: ')) + 1)]

for i in range(1, len(cubes) + 1):
    print(f'{i} ** 3 = {cubes[i - 1]}')
