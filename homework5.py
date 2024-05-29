#####################################################################################################
#                                                                                                   #
#                                            2024-05-29                                             #
#    2023/09/24 00:00|Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи"    #
#                                                                                                   #
#                  https://urban-university.ru/members/courses/course999421818026/                  #
#  20230924-0000prakticeskoe-zadanie-po-teme-neizmenaemye-i-izmenaemye-obekty-kortezi-646436406568  #
#                                                                                                   #
#################################### The homework code is below #####################################

TASK_STR_LEFT_INDENT = 3  # Indent for task strings with results
PARAGRAPH_RIGHT_INDENT = 2  # Right indent before value of paragraph
task_str_first_column_width = 40  # String length for comment in homework tasks (left part of output)
PARAGRAPH_STR_LENGTH = task_str_first_column_width - PARAGRAPH_RIGHT_INDENT  # Addition space for multistring comment for task (right space of paragraph before its value)


def string_to_paragraph(input_string):  # Return substring with defined length containing full words and without trailing spaces
    result = []  # Redefine empty result list
    if len(input_string) <= PARAGRAPH_STR_LENGTH:  # Return only one string equal to input_string if its length is less than paragraph string length
        result.append(input_string)
    else:
        # Define first word index
        first_word_index = last_cutoff_word_index = 0
        while first_word_index + PARAGRAPH_STR_LENGTH < len(input_string):
            first_word_index = last_cutoff_word_index
            # Define last word to cut it
            last_cutoff_word_index = len((input_string[:first_word_index + PARAGRAPH_STR_LENGTH]).rsplit(" ", 1)[0])

            result.append((input_string[first_word_index:last_cutoff_word_index]).strip())

        # Check if there is something else
        if last_cutoff_word_index < len(input_string):
            if len(result[len(result) - 1] + input_string[last_cutoff_word_index:]) <= PARAGRAPH_STR_LENGTH:
                result[len(result) - 1] += input_string[last_cutoff_word_index:]
            else:
                result.append(input_string[last_cutoff_word_index:])
        result[len(result) - 1] = result[len(result) - 1].strip()

    return result


def print_paragraph_with_value(paragraph, value):
    for x in range(0, len(paragraph)):
        if x == 0:
            print(f'{' ': >{TASK_STR_LEFT_INDENT}}{paragraph[x]: <{task_str_first_column_width}}{value}')
        else:
            print(f'{' ': >{TASK_STR_LEFT_INDENT}}{paragraph[x]}')


def e_print(message, result_value):  # Extended print with output format
    print(f'{' ': >{TASK_STR_LEFT_INDENT}}{message: <{task_str_first_column_width}}{result_value}')


print('\nTask 2. Define variables with different data type.')
immutable_var = (1, '1', True, [1, "0"])
e_print('This is defined tuple: ', immutable_var)

print('\nTask 3. Changing variable values.')
immutable_var[3][1] = 'Changed value here'
print_paragraph_with_value(string_to_paragraph("We can't change tuple item values but we can do it if some value, for example, is a list:"), immutable_var)

print('\nTask 4. Creating changeable data structures.')
mutable_list = [0, '1', False]
e_print('We have created "mutable_list": ', mutable_list)
mutable_list = ['2', 1, True]
e_print('And have changed everything in it: ', mutable_list)

##################### End of the homework code #####################


"""
=========================================================================================
=================================== HOMEWORK CONTENTS ===================================
=========================================================================================
2024-05-28

2023/09/24 00:00|Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи"
Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи и списки"

Цель:
Написать программу на языке Python, используя Pycharm, для работы с неизменяемыми и изменяемыми объектами.

1. В проекте, где вы решаете домашние задания, создайте модуль 'homework5.py' и напишите весь код в нём.

2. Задайте переменные разных типов данных:
  - Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных.
  - Выполните операции вывода кортежа immutable_var на экран.

3. Изменение значений переменных:
  - Попытайтесь изменить элементы кортежа immutable_var. Объясните, почему нельзя изменить значения элементов кортежа.

4. Создание изменяемых структур данных:
  - Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
  - Измените элементы списка mutable_list.
  - Выведите на экран измененный список mutable_list.

Примечания:
- Для вывода значений на экран используйте функцию print().
- Обратите внимание на особенности изменяемых и неизменяемых объектов в Python.

Пример результата выполнения программы:
Immutable tuple: (1, 2, 'a', 'b')
Mutable list: [1, 2, 'a', 'b', 'Modified']

Файл с кодом (homework5.py) прикрепите к домашнему заданию.

Успехов!

=========================================================================================
"""
