#Task 1
#The Guessing Game.
#Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated.
# The result should be sent back to the user via a print statement.

import random
guesses = 3
random_number = random.randint(1, 10)
print(random_number)
print('Введите число от 1 до 10\n У вас 3 попытки')
while guesses > 0:
    player_guess = input()

    if player_guess.isdigit() and guesses != 0:
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

