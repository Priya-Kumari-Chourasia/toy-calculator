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
    total = sum(numbers)
    return total / len(numbers)