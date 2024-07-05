"""
Завдання 2
Необхідно розробити функцію, яка приймає рядок як вхідний параметр, додає всі його символи до двосторонньої черги
(deque з модуля collections в Python), а потім порівнює символи з обох кінців черги, щоб визначити, чи є рядок
паліндромом. Програма повинна правильно враховувати як рядки з парною, так і з непарною кількістю символів,
а також бути нечутливою до регістру та пробілів.
"""

from collections import deque

def check_palindrome(string: str) -> bool:
    """ check whether string is a palindrome """
    str_deque = deque()

    for ch in string.replace(" ", "").casefold():
        str_deque.append(ch)

    while len(str_deque) > 1:
        first = str_deque.popleft()
        last = str_deque.pop()
        if first != last:
            return False

    return True

print(check_palindrome("Hello"))
print(check_palindrome("Rad Ar"))
print(check_palindrome("LevEl"))