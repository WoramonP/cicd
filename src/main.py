"""
Multiply-by-two calculator. Only works when the input is a positive integer.
Author: Woramon P.
"""


def multiply_by_two(num: int) -> bool:
    """Return the number multiplied by two."""
    return num * 2


def multiply_by_two_str(num: str) -> str:
    """Return a string indicating the result of the number multiplied by two."""
    if num.isnumeric():
        return f"{num} x 2 equals to {multiply_by_two(int(num))}."
    else:
        return "Please enter a positive integer."
