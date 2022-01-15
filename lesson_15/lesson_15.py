from functools import wraps
# Task 1
# Write a decorator that prints a function with arguments passed to it.
# NOTE! It should print the function, not the result of its execution!

if __name__ == '__main__':
    def logger(func):
        @wraps(func)
        def inner(*args, **kwargs):
            return f'Function name = {func.__name__}, has variable {args}'
        return inner


    @logger
    def add(x, y):
        return x + y


    @logger
    def square_all(*args):
        return [arg ** 2 for arg in args]


    print(add(2,3))
    print(square_all(2,3))

# Task 2
# Write a decorator that takes a list of stop words and replaces them with * inside the decorated function

if __name__ == '__main__':
    def stop_words(words: list):
        def decorator(func):
            @wraps(func)
            def inner(*args, **kwargs):
                string = func(*args, **kwargs)
                for value in words:
                    string = string[:string.find(value)] + '*' + string[string.find(value) + len(value):]
                return string
            return inner
        return decorator


    @stop_words(['pepsi', 'BMW'])
    def create_slogan(name: str) -> str:
        return f"{name} drinks pepsi in his brand new BMW!"

    assert create_slogan("Steve") == "Steve drinks * in his brand new *!"