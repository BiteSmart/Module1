################################################################################
#                                                                              #
#                                  2024-05-29                                  #
#     2023/09/25 00:00|Практическое задание по теме: "Словари и множества"     #
#                                                                              #
#       https://urban-university.ru/members/courses/course999421818026/        #
#  20230925-0000prakticeskoe-zadanie-po-teme-slovari-i-mnozestva-709499863120  #
#                                                                              #
########################## The homework code is below ##########################

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
    print('')

def e_print(message, result_value):  # Extended print with output format
    print(f'{' ': >{TASK_STR_LEFT_INDENT}}{message: <{task_str_first_column_width}}{result_value}\n')


print('\nTask 2. Working with dictionaries.')
my_dict = {'Oleg': 1983, 'Dmitry': 1965, 'Alex': 2000}
e_print('We have created dictionary:', my_dict)

print_paragraph_with_value(string_to_paragraph('Now we want to output value for existing key \'Dmitry\''), my_dict['Dmitry'])

print_paragraph_with_value(string_to_paragraph('And let\'s try handle error on output absent key \'Rammstein\' in dictionary' ), my_dict.get('Rammstein', 'Error: No such key...'))

my_dict['Rammstein'] = 1994
print_paragraph_with_value(string_to_paragraph('New key was added by specifying it with value:'),my_dict)

my_dict.update({'Dmitry': 1985, 'Ann': 1998})
print_paragraph_with_value(string_to_paragraph('Key \'Dmitry\' was updated to 1985 simultaneously with addition of the new key \'Ann\':'),my_dict)

deleted_value = my_dict.pop('Alex')
e_print('We have removed item \'Alex\' with value:', deleted_value)

e_print('Our dictionary now is: ', my_dict)

print('\nTask 3. Working with sets.')
my_set = {1, 2, 3, 4, 5, 4, 3, 2, 'Str', True, True, 'Str', (1, 2, 3), (1, 2, 3)}
print_paragraph_with_value(string_to_paragraph('We have defined the set with duplicated values. As we can see, there are only unique values in the result and boolean values didn\'t added!'), my_set)

my_set.update({6, '7'})
print_paragraph_with_value(string_to_paragraph('We have added values \'6\' and \'7\' to the set by update method: '), my_set)

my_set |= {'Piped1', 'Piped2'}
e_print('Let\'s add Piped[x] elements by pipe: ', my_set)

my_set.pop()
e_print('A random element was removed by pop(): ', my_set)

my_set.remove('Piped2')
print_paragraph_with_value(string_to_paragraph('\'Piped2\' element was removed by remove() method: '), my_set)

my_set.discard((1, 2, 3))
print_paragraph_with_value(string_to_paragraph('Tuple \'(1, 2, 3)\'  was removed by discard() method: '), my_set)


##################### End of the homework code #####################




"""
=========================================================================================
=================================== HOMEWORK CONTENTS ===================================
=========================================================================================
2024-05-29

2023/09/25 00:00|Практическое задание по теме: "Словари и множества"
Практическое задание по теме: "Словари и множества"

Цель: Написать программу на языке Python, используя Pycharm, для работы с словарями и множествами.

1. В проекте, где вы решаете домашние задания, создайте модуль 'homework6.py' и напишите весь код в нём.

2. Работа со словарями:
  - Создайте переменную my_dict и присвойте ей словарь из нескольких пар ключ-значение.
Например: Имя(str)-Год рождения(int).
  - Выведите на экран словарь my_dict.
  - Выведите на экран одно значение по существующему ключу, одно по отсутствуещему из словаря my_dict без ошибки.
  - Добавьте ещё две произвольные пары того же формата в словарь my_dict.
 - Удалите одну из пар в словаре по существующему ключу из словаря my_dict и выведите значение из этой пары на экран.
  - Выведите на экран словарь my_dict.

3. Работа с множествами:
  - Создайте переменную my_set и присвойте ей множество, состоящее из разных типов данных с повторяющимися значениями.
  - Выведите на экран множество my_set (должны отобразиться только уникальныые значения).
  - Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
  - Удалите один любой элемент из множества my_set.
  - Выведите на экран измененное множество my_set.

Примечания:
- Для вывода значений на экран используйте функцию print().
- Помните, что словарь и множество - неупорядоченные коллекции.
- Больше о методах словарей тут, множеств тут.

Пример результата выполнения программы:
Dict: {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
Existing value: 2002
Not existing value: None
Deleted value: 1999
Modified dictionary: {'Vasya': 1975, 'Kamila': 1981, 'Artem': 1915, 'Masha': 2002}

Set: {1, 'Яблоко', 42.314}
Modified set: {'Яблоко', 42.314, 13, (5, 6, 1.6)}

Файл с кодом (homework6.py) прикрепите к домашнему заданию.

Успехов!

=========================================================================================
"""