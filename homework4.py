####################################################################
#                            2024-05-28                            #
#################### The homework code is below ####################

TASK_STR_LEFT_INDENT = 3                # Indent for task strings with results
task_str_first_column_width = 35        # Text width in task explanation
def e_print(message, result_value):     # Extended print with output format
    print(f'{' ': >{TASK_STR_LEFT_INDENT}}{message: <{task_str_first_column_width}}{result_value}')

my_string = input('Input some text: ')
if len(my_string) > 35:     # 35 is optimal for comments in task, but my_string length can be greater
    task_str_first_column_width = len(my_string) + 5

print('\nTask 2. Organize the program')
e_print('Text length by len() function is:', len(my_string))
e_print('Text length by count method is:', my_string.count('') - 1)
e_print('Text length by rfind method is:', my_string.rfind(''))
e_print('Text length by rindex method is:', my_string.rindex(''))

print('\nTask 3. Applying string methods.')
e_print(my_string.upper(), 'This is upper case.')           # Выведите строку my_string в верхнем регистре.
e_print(my_string.lower(), 'This is lower case.')           # Выведите строку my_string в нижнем регистре.
e_print(my_string.replace(' ',''), 'Spaces removed.')       # Измените строку my_string, удалив все пробелы.
e_print(my_string[0], 'First symbol here.')                 # Выведите первый символ строки my_string.
e_print(my_string[-1], 'Last symbol here')                  # Выведите последний символ строки my_string.

##################### End of the homework code #####################

"""
=========================================================================================
=================================== HOMEWORK CONTENTS ===================================
=========================================================================================
2024-05-28

2023/09/24 00:00|Практическая работа по уроку "Организация программ и методы строк."
Практическая работа по уроку "Организация программ и методы строк."

Цель: Написать программу на языке Python с использованием Pycharm для работы с методами строк и организации программ.

1. В проекте, где вы решаете домашние задания, создайте модуль 'homework4.py' и напишите весь код в нём.

2. Организуйте программу:

    Создайте переменную my_string и присвойте ей значение строки с произвольным текстом (функция input()).
    Вывести длину символов введённого текста

3. Работа с методами строк:
Используя методы строк, выполните следующие действия:

    Выведите строку my_string в верхнем регистре.
    Выведите строку my_string в нижнем регистре.
    Измените строку my_string, удалив все пробелы.
    Выведите первый символ строки my_string.
    Выведите последний символ строки my_string.

Примечания:

    Для вывода значений на экран используйте функцию print().
    Для вызова методов строк используйте операцию точки ..
    Дополнительно о всех методах строк можно узнать здесь.

Пример результата выполнения программы:

Код:
name = input()
print(name.upper())

Ввод в консоль:
Urban

Вывод на консоль:
URBAN

Файл с кодом (homework4.py) прикрепите к домашнему заданию.

Успехов!
"""