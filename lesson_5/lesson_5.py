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
input_string = input('Введите строку ')

