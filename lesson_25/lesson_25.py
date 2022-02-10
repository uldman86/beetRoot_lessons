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
