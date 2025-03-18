# Задача 1: Оценка по шкале
from random import random


def check_grade(score=85):
    if 90 <= score <= 100:
        return ("Отлично")
    elif 75 <= score <= 89:
        return ("Хорошо")
    elif 50 <= score <= 74:
        return ("Удовлетворительно")
    else:
        return ("Неудовлетворительно")

def is_even(number):
    return "чётным" if number % 2 == 0 else "нечётным"

num1 = 4
print(f"Число {num1} является {is_even(num1)}")

# Задача 3: Максимальное из двух чисел**
def find_max(a,b):
    if a > b:
        return a
    else:
        return b

number1 = 10
number2 = 20
print(f"Максимальное из чисел {number1} и {number2}: {find_max(number1,number2)}")

# Задача 4: Проверка числа на положительность и чётность**
def check_number(number):
    if number > 0:
        if number % 2 == 0:
            return f"Число {number} положительное и чётное."
        else:
            return f"Число {number} положительное, но нечётное"
    else:
        return f"Число {number} отрицательное."

print(check_number(5))

#Задача 5: Проверка длины строки**

# Напишите функцию **`check_string_length(string, length)`**, которая принимает строку и число.
# Если длина строки больше указанного числа, выведите **`"Длина строки достаточная"`**, иначе – **`"Строка слишком короткая"`**.
# Используйте **`if-else`**.
#
# **Требования:**
#
# - Функция должна принимать два аргумента: строку **`string`** и число **`length`**.
# - Используйте **`if-else`** для сравнения длины строки с числом.
# - Верните результат из функции.
# - Выведите результат с помощью функции **`print()`**.
#
# **Пример:**
#
# Если вызвать функцию **`check_string_length("Python", 5)`**, то она должна вернуть:
#
# **`"Длина строки достаточная"`**
#
# Если вызвать функцию **`check_string_length("Hi", 5)`**, то она должна вернуть:
#
# **`"Строка слишком короткая"`**
#
# **Вывод результата:**
#
# Длина строки "Python" достаточная.
# Строка "Hi" слишком короткая.

def check_string_length(string, length):
    if len(string) > length:
        return f'Длина строки "{string}" достаточная.'
    else:
        return f'Длина строки "{string}" слишком короткая.'

print(check_string_length("Hi", 5))

