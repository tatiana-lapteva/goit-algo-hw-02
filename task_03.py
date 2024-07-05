"""
Завдання 3
У багатьох мовах програмування ми маємо справу з виразами, виділеними символами-розділювачами, 
такими як круглі ( ), квадратні [ ] або фігурні дужки { }.
Напишіть програму, яка читає рядок з послідовністю символів-розділювачів, наприклад, 
( ) { [ ] ( ) ( ) { } } }, і надає відповідне повідомлення, коли розділювачі симетричні, 
несиметричні, наприклад ( ( ( ) , або коли розділювачі різних видів стоять у парі, як-от ( }.
Використовуйте стек, щоб запам'ятати відкриті в даний момент символи-розділювачі.
 """


def is_matching_pair(opening, closing):
    pairs = {'(': ')', '{': '}', '[': ']'}
    return pairs.get(opening) == closing


def check_delimiters(expression):
    stack = []
    for char in expression:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack:
                return "Несиметрично"
            top = stack.pop()
            if not is_matching_pair(top, char):
                return f"Несиметрично"
    if stack:
        return "Несиметрично"

    return "Cиметрично"


expressions = ["( ){[ 1 ]( 1 + 3 )( ){ }}",
               "( 23 ( 2 - 3);",
               "( 11 }"]

for exp in expressions:
    result = check_delimiters(exp)
    print(f"{exp}': {result}")
