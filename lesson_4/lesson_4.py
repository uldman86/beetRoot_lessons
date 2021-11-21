# Task 1
# String manipulation
# Write a Python program to get a string made of the first 2 and the
# last 2 chars from a given string. If the string length is less than 2,
# return instead of the empty string.
print('Task 1')

my_strings = ['helloworld', 'my', 'x']
for x in my_strings:
    if len(x) > 2:
        print(x[0:2] + x[len(x) - 2:])
    elif len(x) == 2:
        print(x * 2)
    else:
        print('')

# Task 2
# The valid phone number program.
# Make a program that checks if a string is in the right format for a phone number.
# The program should check that the string contains only numerical characters and is only 10 characters long.
# Print a suitable message depending on the outcome of the string evaluation.
print('\nTask 2')

phone_number = '0999111222'  # Корректный ввод
# phone_number = 'a999111222'    #Символ в номере
# phone_number = '111222'        #Короткий номер
# phone_number = 'a111222'       #Короткий номер и символ

if phone_number.isdigit() and len(phone_number) == 10:
    print(f'Вы ввели номер {phone_number}')
else:
    if len(phone_number) != 10: print('Неправельный ввод, пожалуйста введите 10 цифр вашего телефона')
    if not phone_number.isdigit(): print('Ваш номер не должен содержать буквы и символы')

# Task 3
# Write a program that has a variable with your name stored (in lowercase) and then asks for your name as input.
# The program should check if your input is equal to the stored name even if the given name has another case, e.g.,
# if your input is “Anton” and the stored name is “anton”, it should return True.
print('\nTask 3')

my_name = 'sergey'
if my_name == input().lower():
    print(True)
else:
    print('Пользователь не найден')
