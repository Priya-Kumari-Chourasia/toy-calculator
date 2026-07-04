"""A tiny calculator module -- intentionally has one seeded bug for practice."""


def add(a, b):
    return a + b


def subtract(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments to subtract must be numbers (int or float)")
    return a - b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def average(numbers):
    total = sum(numbers)
    return total / len(numbers)