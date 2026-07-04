"""A tiny calculator module"""


def add(a, b):
    """
    Adds two numbers.

    Args:
        a (int or float): The first number to add.
        b (int or float): The second number to add.

    Returns:
        int or float: The sum of a and b.

    Raises:
        TypeError: If either a or b is not a number (int or float).
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments to add must be numbers (int or float)")
    return a + b


def subtract(a, b):
    """
    Subtracts one number from another.

    Args:
        a (int or float): The number to subtract from.
        b (int or float): The number to subtract.

    Returns:
        int or float: The difference between a and b.

    Raises:
        TypeError: If either a or b is not a number (int or float).
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments to subtract must be numbers (int or float)")
    return a - b


def divide(a, b):
    """
    Divides one number by another.

    Args:
        a (int or float): The dividend.
        b (int or float): The divisor.

    Returns:
        int or float: The quotient of a and b.

    Raises:
        TypeError: If either a or b is not a number (int or float).
        ValueError: If b is zero.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments to divide must be numbers (int or float)")
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def average(numbers):
    """
    Calculates the average of a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        int or float: The average of the numbers in the list.

    Raises:
        TypeError: If the input is not a list or if the list contains non-numeric values.
        ValueError: If the input list is empty.
    """
    if not isinstance(numbers, list):
        raise TypeError("The 'numbers' argument to average must be a list")
    if len(numbers) == 0:
        raise ValueError("Cannot calculate average of an empty list")
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise TypeError("All elements in the list must be numbers (int or float)")
    total = sum(numbers)
    return total / len(numbers)


def multiply_list(numbers):
    if len(numbers) == 0:
        raise ValueError("Cannot calculate product of an empty list")
    product = 1
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise TypeError("All elements in the list must be numbers (int or float)")
        product *= num
    return product