"""A tiny calculator module -- intentionally has one seeded bug for practice."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def divide(a, b):
    # BUG: no check for division by zero -- this will crash with a raw
    # ZeroDivisionError instead of failing gracefully.
    return a / b


def average(numbers):
    total = sum(numbers)
    return total / len(numbers)
