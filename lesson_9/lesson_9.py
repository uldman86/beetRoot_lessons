#Task 1
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

