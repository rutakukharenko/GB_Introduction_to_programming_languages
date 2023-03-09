# Lesson5
import random


def random_list_int(n, start, stop):
    if start > stop:
        print('The start of the range must be less than the end!')
    else:
        items = [random.randint(start, stop) for _ in range(n)]
        return items


def random_list_float(n):
    items = [round(random.random() * 100, 2) for _ in range(n)]
    return items


# Task 34
"""
Задача 34:
Задайте массив, заполненный случайными, положительными, трёхзначными числами. 
Напишите программу, которая покажет количество чётных чисел в массиве.
[345, 897, 568, 234] -> 2
"""
n, start, stop = int(input('Enter amount of elements: ')), int(
    input('Enter a start of range 100 <= start <= 999: ')), int(
    input('Enter an end of range 100 <= stop <= 999: '))

if (not 100 <= start <= 999) or (not 100 <= stop <= 999):
    print('Start and stop numbers must be in range: range 100 <= start/stop <= 999!')
else:
    random_list = random_list_int(n, start, stop)
    count = 0

    for i in random_list:
        if i % 2 == 0:
            count += 1

    print(f'Generated list: {random_list}.')
    print(f'Number of even elements: {count}.')

# Task 36
"""
Задача 36:
Задайте одномерный массив, заполненный случайными числами. 
Найдите сумму элементов, стоящих на нечётных позициях.
[3, 7, 23, 12] -> 19
[-4, -6, 89, 6] -> 0
"""
n, start, stop = int(input('Enter amount of elements: ')), int(
    input('Enter a start of range: ')), int(
    input('Enter an end of range: '))

random_list = random_list_int(n, start, stop)
sum = 0

for i in range(len(random_list)):
    if i % 2 != 0:
        sum += random_list[i]

print(f'Generated list: {random_list}.')
print(f'Sum of elements in odd positions: {sum}.')

# Task 38
"""
Задача 38:
Задайте массив вещественных чисел. 
Найдите разницу между максимальным и минимальным элементов массива.
"""
n = int(input('Enter amount of elements: '))

random_list = random_list_float(n)

print(f'Generated list: {random_list}.')
print(f'Difference between the maximum and minimum of elements: {round(max(random_list) - min(random_list), 2)}.')

# Task 37
"""
Задача 37:
Найдите произведение пар чисел в одномерном массиве. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
Результат запишите в новом массиве.
[1, 2, 3, 4, 5] -> [5, 8, 3]
[6, 7, 3, 6] -> [36, 21]
"""
n, start, stop = int(input('Enter amount of elements: ')), int(
    input('Enter a start of range: ')), int(
    input('Enter an end of range: '))

random_list = random_list_int(n, start, stop)
product_of_pairs_list = []

if len(random_list) % 2 == 0:
    for i in range(len(random_list) // 2):
        product_of_pairs_list.append(random_list[i] * random_list[len(random_list) - i - 1])
else:
    for i in range(len(random_list) // 2 + 1):
        if i == len(random_list) // 2:
            product_of_pairs_list.append(random_list[i])
        else:
            product_of_pairs_list.append(random_list[i] * random_list[len(random_list) - i - 1])

print(f'Generated list: {random_list}.')
print(f'Product of pairs list: {product_of_pairs_list}.')