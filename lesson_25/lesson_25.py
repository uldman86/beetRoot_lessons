from typing import Optional

if __name__ == '__main__':
    #Task 1

    # from typing import Optional
    #
    #
    # def to_power(x: Optional[int, float], exp: int) -> Optional[int, float]:
    #     """
    #     Returns  x ^ exp
    #
    #     >>> to_power(2, 3) == 8
    #     True
    #
    #     >>> to_power(3.5, 2) == 12.25
    #     True
    #
    #     >>> to_power(2, -1)
    #     ValueError: This function works only with exp > 0.
    #     """


    def to_power(x: int | float, exp: int) -> Optional[int | float]:
        if exp < 0:
            raise ValueError('This function works only with exp > 0')
        elif exp == 0:
            return 0
        elif exp == 1:
            return x
        return x * to_power(x, exp - 1)

    assert to_power(2, 3) == 8
    assert to_power(3.5, 2) == 12.25
    #to_power(2, -1)


    # Task 2
    # from typing import Optional
    #
    #
    # def is_palindrome(looking_str: str, index: int = 0) -> bool:
    #     """
    #     Checks if input string is Palindrome
    #     >>> is_palindrome('mom')
    #     True
    #
    #     >>> is_palindrome('sassas')
    #     True
    #
    #     >>> is_palindrome('o')
    #     True
    #     """
    #     pass

    from typing import Optional


    def is_palindrome(looking_str: str, index: int = 0) -> bool:
        if index > len(looking_str) or len(looking_str) == 1:
            return True
        elif not looking_str:
            return False
        elif looking_str[index] == looking_str[-1 - index] and index < len(looking_str) / 2:
            index += 1
            is_palindrome(looking_str, index)
            return True
        else:
            return False


    assert is_palindrome('mom')
    assert is_palindrome('sassas')
    assert is_palindrome('o')
    assert is_palindrome('') == False


    # Task 3


    # from typing import Optional
    # def mult(a: int, n: int) -> int:
    #     """
    #     This function works only with positive integers
    #
    #     >>> mult(2, 4) == 8
    #     True
    #
    #     >>> mult(2, 0) == 0
    #     True
    #
    #     >>> mult(2, -4)
    #     ValueError("This function works only with postive integers")
    #     """
    from typing import Optional


    def mult(a: int, n: int) -> int:
        if n < 0:
            raise ValueError('This function works only with postive integers')
        if n == 0:
            return 0
        if n == 1:
            return a
        return a + mult(a, n - 1)


    assert mult(2, 4) == 8
    assert mult(2, 0) == 0
    # mult(2, -4)

    #  Task 4
    # def reverse(input_str: str) -> str:
    #     """
    #     Function returns reversed input string
    #     >>> reverse("hello") == "olleh"
    #     True
    #     >>> reverse("o") == "o"
    #     True
    #     """

    def reverse(input_str: str) -> str:
        if not input_str:
            raise ValueError('Пустая строка')
        if len(input_str) == 1:
            return input_str[0]

        return input_str[-1] + reverse(input_str[:-1])


    assert reverse('hello') == 'olleh'
    assert reverse('o') == 'o'


