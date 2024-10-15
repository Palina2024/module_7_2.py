import io

def custom_write(file_name, strings):
    file_name = 'test.txt'
    strings_positions = {}

    file = open(file_name, 'w', encoding='utf-8')
    number_line = 1
    for string in strings:
        byte_pos = file.tell()
        strings_positions[(number_line, byte_pos)] = string
        file.write(string + '\n')
        number_line += 1

    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)

