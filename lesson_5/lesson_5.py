#Task 1
#The Guessing Game.
#Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated.
# The result should be sent back to the user via a print statement.
print('\nTask 1')

import random
guesses = 3
random_number = random.randint(1, 10)
print('Введите число от 1 до 10\n У вас 3 попытки')
while guesses > 0:
    player_guess = input()

    if player_guess.isdigit() and guesses != 0:  # Проверка на валидность ввода
        guesses -= 1
        player_guess = int(player_guess)
        if player_guess == random_number:
            print('Вы угадали\n Конец игры!')
            break
        elif guesses == 0:
            print('Вы проиграли \n У вас 0 попыток')
        else:
            print(f'Не правильно\n У вас  осталось {guesses} попыток')

    else:
        print('Неправильный ввод. Пожалуйста введите число от 1 до 10')

#Task 2
#The birthday greeting program.
#Write a program that takes your name as input, and then your age as input and greets you with the following:
#“Hello <name>, on your next birthday you’ll be <age+1> years”
print('\nTask 2')

name = input('Type your name   ')
age = input('Type yore age   ')
if age.isdigit():

    print(f'Hello {name}, on your next birthday you’ll be {int(age) + 1} years')
else:
    print('Invalid type')

#Task 3

#Create a program that reads an input string and then creates and prints 5 random
# strings from characters of the input string.
#For example, the program obtained the word ‘hello’, so it should print 5 random strings(words)
# that combine characters ‘h’, ‘e’, ‘l’, ‘l’, ‘o’ -> ‘hlelo’, ‘olelh’, ‘loleh’ …

print('\nTask 3')

import random
word = input('Введите слово  ')
five_words = 0

while five_words < 5:  # повторяем для 5 слов
    char_list = list(word)  # разбиваем слово на список символов
    len_list = len(word) - 1
    new_word = ''

    while len_list >= 0:  # повторить раз на длину строки
        char_rand = random.randint(0, len_list)  # генерация рандомного символа строки
        new_word = new_word + char_list[char_rand]  # собираем слово по буквам
        char_list.remove(str(char_list[char_rand]))  # удаляем использованный символ из списка
        len_list -= 1

    five_words += 1
    print('Новое слово  = ', new_word)

#Task 4
#The math quiz program Write a program that asks the answer for a mathematical expression,
# checks whether the user is right or wrong, and then responds with a message accordingly.
print('\nTask 4')

print('Математическая викторина')
guesses = 3
count_question = 1
question_1 = """Вопрос №1
Решите пример:  1.36 + 2.8 * 0.7 = """
question_2 = """Вопрос №2
Чему равен х?   5 * (25 + x) = 1740 + 25 = """
question_3 = """Вопрос №2
Чему равен х?   5 * (25 + x) = 1740 + 25 = """

while guesses > 0 and count_question < 3:
    if count_question == 1 and guesses > 0:
        guess = input(question_1)
        if  guess == '3.32':
            print('Правильно!')
            count_question += 1
        else:
            print('Неправильно!')
            guesses -= 1

    elif count_question == 2 and guesses > 0:
        guess = input(question_2)
        if  guess == '328':
            print('Правильно!')
            print('Поздравляем, вы выиграли!!!')
            count_question += 1
        else:
            print('Неправильно!')
            guesses -= 1
    if guesses == 0:
        print('Вы проиграли, у вас закончились  попытки')
