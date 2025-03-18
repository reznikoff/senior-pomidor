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