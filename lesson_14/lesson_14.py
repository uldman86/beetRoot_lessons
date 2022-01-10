# Task 1
# Write a Python program to detect the number of local variables declared in a function.

if __name__ == '__main__':
    # Task 1
    # Write a Python program to detect the number of local variables declared in a function.

    def var_info(func):
        return func.__code__.co_nlocals


    def fun1(x=5):
        a = 10
        b = 'A'
        c = 0


    print(f'function has {var_info(fun1)} variables')

# Task 2
# Write a Python program to access a function inside a function (Tips: use function, which returns another function)
if __name__ == '__main__':
    def my_func(name, age):
        def func1():
            return f'Name - {name}, age - {age}'
        return func1

    print_name = my_func('Sergey', 28)

# Task 3
# Write a function called `choose_func` which takes a list of nums and 2 callback functions.
# If all nums inside the list are positive, execute the first function on that list and return the result of it.
# Otherwise, return the result of the second one

if __name__ == '__main__':
    def choose_func(nums: list, func1, func2):
        status = is_positive(nums)
        if status:
            return func1(nums)
        else:
            return func2(nums)


    def is_positive(nums):
        for item in nums:
            if item < 0:
                return False
        return True


    # Assertions
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [1, -2, 3, -4, 5]


    def square_nums(nums):
        return [num ** 2 for num in nums]


    def remove_negatives(nums):
        return [num for num in nums if num > 0]


    #print(choose_func(nums2, square_nums, remove_negatives))
    assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
    assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]