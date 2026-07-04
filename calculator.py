"""A tiny calculator module -- intentionally has one seeded bug for practice."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def average(numbers):
    if len(numbers) == 0:
        raise ValueError("Cannot calculate average of an empty list")
    total = sum(numbers)
    return total / len(numbers)