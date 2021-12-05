import math
# Task 1
# Write a function called oops that explicitly raises an IndexError exception when called. Then write another function
# that calls oops inside a try/except state­ment to catch the error. What happens if you change oops to raise KeyError
# instead of IndexError?

if __name__ == '__main__':
    def oops():
        raise IndexError()


    def my_function():  # Если генерируем ошибку KeyError то она отловлена не будет и программа выбросит ошибку типа
        # KeyError
        try:
            oops()
        except IndexError:
            print('Ошибка "IndexError" отловлена')


    my_function()

# Task 2
# Write a function that takes in two numbers from the user via input(), call the numbers a and b, and then returns the
# value of squared a divided by b, construct a try-except block which raises an exception if the two values given by the
# input function were not numbers, and if value b was zero (cannot divide by zero).

if __name__ == '__main__':
    def my_function(a, b):
        return int(a ** 2 / b)


    try:
        print(my_function(int(input('Введите число a = ')), int(input('Введите число b = '))))
    except ValueError:
        print('Вы ввели букву вместо цифры')
    except ZeroDivisionError:
        print('Делить на 0 нельзя')


# Task 3
# Write a function that will translate the age from Earth to Martian.
# There are 365 days on Earth in a year and 687 on Mars

if __name__ == '__main__':
    def mars_age(age: int) -> int:
        ratio = 687 / 365  # Наодим коэфициент 1.8821917808219177
        return math.trunc(age / ratio)


    assert mars_age(10) == 5
    assert mars_age(63) == 33
    assert mars_age(1000) == 531


# Task 4
# Напишите функцию greet принимающую имя name (type:str) м слово word (type:str).
# Если слово не передано то считать его " -" и возвращающую строку вида "[Имя] ты сегодня [слово]!"

if __name__ == '__main__':
    def greet(name: str, word: str = '-') -> str:
        new_word = f'{name.capitalize()} ты сегодня {word}!'
        return new_word


    assert greet("111", "2") == "111 ты сегодня 2!"
    assert greet("игорь", "молодец") == "Игорь ты сегодня молодец!"
    assert greet(name="ольга", word="супер") == "Ольга ты сегодня супер!"
    assert greet("николай") == "Николай ты сегодня -!"


# Task 5
# Напишите функцию joinA которая принимает неограниченное количество значений любого типа и возвращает строку где
# эти значения склеены через символ A
# Попробуйте написать с помощью компрехеншена одной строкой return ___magic___

if __name__ == '__main__':
    def joinA(*args):
        my_string = 'A'.join([str(value) for value in args])
        return my_string


    assert joinA("Привет", "мир", "!") == "ПриветAмирA!"
    assert joinA("Привет", 1, 2, 3, True) == "ПриветA1A2A3ATrue"
    assert joinA() == ""