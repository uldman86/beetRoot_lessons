def count_lines(file):
    counter_lines = 0

    for row in file:
        counter_lines += 1
    file.seek(0)
    return counter_lines


def count_chars(file):
    counter_chars = 0
    for row in file:
        counter_chars += len(row)
    return counter_chars


def test(name):
    with open(name, 'r') as file:
        return f'lines = {count_lines(file)}, chars = {count_chars(file)}'

try:
    print(test(input('Какой документ вы хотите проверить?   ')))
except FileNotFoundError:
    print('Файл не найден')

