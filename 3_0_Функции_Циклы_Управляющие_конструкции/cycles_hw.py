# # Задача 1
# def sum_numbers(n):
#     total = 0
#     for i in range(1,n+1):
#         total += 1
#     return total
#
# result = sum_numbers(5)
# print(f"Сумма чисел от 1 до 5: {result}")
from random import random


# Задача 2
def find_min(numbers):
    minimum = numbers[0]
    for number in numbers:
        if number < minimum:
            minimum = number
    return minimum

my_list = [3, 1, 4, 1, 5]
result2 = find_min(my_list)
print(f"Минимальное число в списке {my_list}: {result2}")

# Задача 3
def count_vowels(string):
    vowels = "aeiou"
    count = 0
    for char in string.lower():
        if char in vowels:
            count += 1
    return count

text = "Hello world"
result = count_vowels(text)
print(f"Количество гласных в строке {text}: {result}")

# Задача 4 (скип)

# Задача 5
def countdown():
    for i in range(10, 0, -1):
        print(i)
    print("Старт!")
countdown()

# Задача 6
def countdown2():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Старт!")
countdown2()