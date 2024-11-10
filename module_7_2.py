def custom_write(file_name, strings):
    result_strings = {}
    line = 0
    file = open(file_name, 'a', encoding='utf-8')
    for string in strings:
        line += 1
        teller = file.tell()
        file.write(str(string) + '\n')
        result_strings[(line, teller)] = string
    file.close()
    return result_strings

# Пример результата выполнения программы:

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
