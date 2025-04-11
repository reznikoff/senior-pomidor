# Задача 1: Анаграмма
def is_anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    return sorted(s1) == sorted(s2)

print(is_anagram("listen", "silent"))

# Задача 2: Палиндром
def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

print(is_palindrome("A man, a plan, a canal: Panama"))

# Задача 3: Самое длинное слово
# скип

# Задача 4: Форматирование номера телефона
#  скип

# Задача 5: Удаление дублирующих символов
def remove_duplicates(s):
    result = ""
    for char in s:
        if char not in result:
            result += char
    return result