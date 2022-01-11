from functools import wraps
# Task 1
# Write a decorator that prints a function with arguments passed to it.
# NOTE! It should print the function, not the result of its execution!

if __name__ == '__main__':
    def logger(func):
        @wraps(func)
        def inner(*args, **kwargs):
            print(f'Start function {func.__name__}')
            result = func(*args, **kwargs)
            return result

        return inner


    @logger
    def add(x, y):
        return x + y


    @logger
    def square_all(*args):
        return [arg ** 2 for arg in args]


    print(f'result func {add.__name__} = {add(2, 3)}')
    print(f'result func {square_all.__name__} = {square_all(2, 3)}')