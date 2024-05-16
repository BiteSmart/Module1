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