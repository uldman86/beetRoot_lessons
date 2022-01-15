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

# Task 3
# Write a decorator `arg_rules` that validates arguments passed to the function.
# A decorator should take 3 arguments:
# max_length: 15
# type_: str
# contains: [] - list of symbols that an argument should contain
# If some of the rules' checks returns False, the function should return False and print the reason it failed;
# otherwise, return the result.

if __name__ == '__main__':
    def arg_rules(type_: type, max_length: int, contains: list):
        def decorator(func):
            def inner(*args, **kwargs):
                if isinstance(*args, type_):
                    if len(*args) < max_length:
                        string_name = args[0]
                        for val in contains:
                            if string_name.find(val) > -1:
                                return func(*args,**kwargs)
                        print(f'Передаваемая строка не содержит значения {contains}')
                        return False
                    else:
                        print(f'Длина строки превышает допустимое значение {max_length}')
                        return False
                else:
                    print(f'Неподходящий тип, ожидаемы тип {type_}')
                    return False
            return inner
        return decorator


    @arg_rules(type_=str, max_length=15, contains=['05', '@'])
    def create_slogan(name: str) -> str:
        return f"{name} drinks pepsi in his brand new BMW!"


    assert create_slogan('johndoe05@gmail.com') is False

    assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
