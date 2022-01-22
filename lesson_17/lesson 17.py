# Task 1

# Create your own implementation of a built-in function enumerate, named `with_index`, which takes two parameters:
# `iterable` and `start`, default is 0. Tips: see the documentation for the enumerate function

if __name__ == '__main__':
    def with_index(iterable, start=0):
        index = start
        for value in iterable:
            yield (index, value)
            index += 1


    x = [2, 5, 7, 10, 12, 14, 18]
    y = range(1, 12)
    for val in with_index(x, 2):
        print(val)

    for val in enumerate(x, 2):
        print(val)

# Task 2
# Create your own implementation of a built-in function range, named in_range(), which takes three parameters:
# `start`, `end`, and optional step. Tips: See the documentation for `range` function

if __name__ == '__main__':
    def cool_gen(func):
        def inner(*args, **kwargs):
            result = []
            for val in func(*args, **kwargs):
                result.append(val)
            return result

        return inner


    @cool_gen
    def in_range(start, end, step=1):
        n = start
        while True:
            if n >= end:
                break
            yield n
            n += + step

    print(in_range(1, 16, 4))


# Task 3
# Create your own implementation of an iterable, which could be used inside for-in loop.
# Also, add logic for retrieving elements using square brackets syntax.

if __name__ == '__main__':
    class Cards:
        def __init__(self, start, end, step):
            self.start = start -1
            self.end = end - step
            self.step = step
            self.log_list = []

        def __iter__(self):
            return self

        def __next__(self):
            if self.start < self.end:
                self.start += self.step
                self.log_list.append(self.start)
                return self.start
            else:
                raise StopIteration


    c = Cards(1, 20, 4)
    for val in c:
        print(val, end='  ')
        print(c.log_list)