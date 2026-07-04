"""A tiny calculator module -- intentionally has one seeded bug for practice."""

def add(a, b):
    return a + b

def subtract(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments to subtract must be numbers (int or float)")
    return a - b

def multiply(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments to multiply must be numbers (int or float)")
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def average(numbers):
    if len(numbers) == 0:
        raise ValueError("Cannot calculate average of an empty list")
    total = sum(numbers)
    return total / len(numbers)