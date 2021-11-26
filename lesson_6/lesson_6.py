import random

# Task 1
# The greatest number Write a Python program to get the largest number from a list of
# random numbers with the length of 10
# Constraints: use only while loop and random module to generate numbers

if __name__ == '__main__':
    print('Task 1')
    integer_list = []
    iterator = 0
    while iterator < 10:
        integer_list.append(round(random.random(), 5))  # Генерация рандомного числа от 0 до 1 и добавление в список
        iterator += 1
    print(f' Список случайных чисел = {integer_list}\n'
          f' Самым большим числом является = {max(integer_list)}')

# Task 2
# Generate 2 lists with the length of 10 with random integers from 1 to 10,
# and make a third list containing the common integers between the 2 initial lists without any duplicates.
# Constraints: use only while loop and random module to generate numbers

if __name__ == '__main__':
    print('\nTask 2')
    list_1 = []
    list_2 = []
    new_list = []
    iterator = 10
    while iterator > 0:
        list_1.append(random.randint(1, 10))  # Генерация числа для первого списка
        list_2.append(random.randint(1, 10))  # Генерация числа для второго списка
        iterator -= 1

    while iterator < 10:
        if list_1[iterator] in list_2 and list_1[iterator] not in new_list:  # Сравниваем элементы в двух списках
            new_list.append(list_1[iterator])  # Если элементы совпадают и не содержатся в новом списке то добовляем его
        iterator += 1
    print(f' list_1 = {list_1}\n list_2 = {list_2}\n Одинаковые значения {new_list}')

# Task 3
# Extracting numbers.
# Make a list that contains all integers from 1 to 100,
# then find all integers from the list that are divisible by 7 but not a multiple of 5,
# and store them in a separate list. Finally, print the list.
# Constraint: use only while loop for iteration

if __name__ == '__main__':
    print('\nTask 3')
    integer_list = range(1, 101)
    iterator = 0
    new_list = []
    while iterator < 100:
        if integer_list[iterator] % 7 == 0 and integer_list[iterator] % 5 != 0:
            new_list.append(integer_list[iterator])
        iterator += 1
    print(f'Список чисел которые делятся на 7 но не делятся на 5 {new_list}')

# Доп. задание 1
# Заполните лист 10ю рандомными значениями в промежутке 1-100.
# (Испольуя метод randint модуля random) Пока длинна листа меньше 10ти добавляйте к листу элемент.
# Пройдитесь циклом и найдите минимальное и максимальное значение Не используя встроенные методы.
# Выведете минимальное и максимальное значение списка используя встроенные методы.

if __name__ == '__main__':
    print('\n Доп. задание 1')
    integer_list = []
    iterator = 0
    max_int = 0
    min_int = 100

    while iterator < 10:
        integer_list.append(random.randint(1, 101))  # Генерация рандомного числа от 0 до 100 и добавление в список
        iterator += 1

    iterator = 0
    while iterator < 10:
        if integer_list[iterator] > max_int:  # Находим максимальное число в списке
            max_int = integer_list[iterator]

        if integer_list[iterator] < min_int:  # Находим минимальное число в списке
            min_int = integer_list[iterator]
        iterator += 1

    print(f' Создаём массив случайных чисел в диапазоне от 1 до 100 {integer_list}\n '
          f'Минимальное число = {min_int}\n '
          f'Максимальное число = {max_int}')

# Доп. задание 2
# Превратите полученную от пользователя строку в тапл. Выведите строку содержащую только буквы на четных позициях.

if __name__ == '__main__':
    exmpl = tuple("Привіт")
    var1 = ''.join(exmpl[::2])
    assert var1 == "Пиі"

# Доп. задание 3
# В цикле пока пользователь не введет Q запрашивайте Фамилии игроков. Сложите их в лист.
# Отсортируйте лист используя втсроенную функцию. Выведите на экран получившийся список.
# Теперь пройдитесь циклом по списку и выведите
# Абрам играет с Яков
# Борис играет м Эдик
# (первый с последним, второй с предпоследним)

if __name__ == '__main__':
    print('\n Доп. задание 3')
    surnames = []

    while True:  # Запрашиваем фамилии и сохраняем в список пока пользователь не нажмет Q
        user_type = input('Введите фамилию игрока ')
        if user_type == 'Q':
            break
        surnames.append(user_type)

    surnames.sort()
    iterator = 0

    if len(surnames) % 2 == 0:  # Проверка на чётное кол-во игроков
        while iterator < (len(surnames) / 2):  # Проходим половину списка
            print(
                f'{surnames[iterator]} играет с  {surnames[-iterator - 1]}')  # Проходим список с двух сторон к середине
            iterator += 1
    else:
        print('Список должен содержать чётное кол-во игроков')

# Доп. задание 4
# Создайте лист длинной 10 с подряд идущими значениями. Используя цикл переверните лист.
# (для этого надо поменять первый с последним, второй с предпоследним и так далее)

if __name__ == '__main__':
    print('\n Доп. задание 4')
    integer_list = list(range(0, 10))
    iterator = -2

    while iterator > -11:
        integer_list.append(integer_list.pop(iterator))  # Начиная -2 индекса перекидываем значение в конец списка
        iterator -= 1

    print(integer_list)
