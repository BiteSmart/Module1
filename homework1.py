# 2024-05-28
### The homework code is below ###

example = input('Input any string: ')           # В переменную example запишите любую строку.
if (len(example) == 0):
    print("You didn't enter any text")
    exit()
print(f'The first symbol is: {example[0]}')     # Выведите на экран(в консоль) первый символ этой строки.
print(f'The last symbol is: {example[-1]}')     # Выведите на экран(в консоль) последний символ этой строки (используя отрицательный индекс).

# Выведите на экран(в консоль) вторую половину этой строки (С нечётным количеством символов: 'Urban' -> 'ban').
if (len(example) == 1):
    print("String consists of the one symbol. This can't have a second part")
else:
    print('The second part of the string is:', end = " ")
    if (len(example) == 3):
        print(example[-1])
    elif ((len(example) - len(example) // 2) % 2 == 1):
        print(example[len(example) // 2:])
    else:
        print(example[(len(example) // 2) - 1:])
# End: Выведите на экран(в консоль) вторую половину этой строки (С нечётным количеством символов: 'Urban' -> 'ban').

print(f'Reverse of the string is: {example[::-1]}')          # Выведите на экран(в консоль) это слово наоборот.
print(f'Every second string symbol is: {example[1::2]}')     # Выведите на экран(в консоль) каждый второй символ этой строки. (Пример: 'Тапинамбур'->'аиабр')
### End of the homework code ###




"""
=========================================================================================
=================================== HOMEWORK CONTENTS ===================================
=========================================================================================
2024-05-28

2023/09/21 00:00|Практическое задание по уроку "Строки и индексация строк"
Практическое задание по уроку "Строки и индексация строк"

Цель: Научиться работать со строками и индексацией строк в Python.
Задача:
Выполните следущие действия в PyCharm:

    В переменную example запишите любую строку.
    Выведите на экран(в консоль) первый символ этой строки.
    Выведите на экран(в консоль) последний символ этой строки (используя отрицательный индекс).
    Выведите на экран(в консоль) вторую половину этой строки (С нечётным количеством символов: 'Urban' -> 'ban').
    Выведите на экран(в консоль) это слово наоборот.
    Выведите на экран(в консоль) каждый второй символ этой строки. (Пример: 'Тапинамбур'->'аиабр')

Пример результата работы вашего кода:
=== The picture is here ===

Вводные данные:
example = 'Тапинамбур'
Вывод на экран(в консоль):
Т
р
амбур
рубманипаТ
аиабр
Примечания:

    Для вывода значений на экран используйте функцию print()
    Для доступа к символу строки по индексу используйте квадратные скобки и индекс символа ('Urban'[3] -  четвёртый символ строки 'Urban' - 'a')
    Индексация начинается с нуля.



Файл с кодом (homework1.py) прикрепите к домашнему заданию.

Успехов!

=========================================================================================
"""