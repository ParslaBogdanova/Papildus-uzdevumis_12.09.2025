import math


def add(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Both arguments must be numbers.")
    return num1 + num2


def subtract(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Both arguments must be numbers.")
    return num1 - num2


def multiply(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Both arguments must be numbers.")
    return num1 * num2


def divide(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Both arguments must be numbers.")
    if num2 == 0:
        raise ValueError("Cannot divide by zero.")
    return num1 / num2


def power(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Both arguments must be numbers.")
    return num1 ** num2


def modulus(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Both arguments must be numbers.")
    if num2 == 0:
        raise ValueError("Cannot divide by zero.")
    return num1 % num2


def floor_divide(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise ValueError("Both arguments must be numbers.")
    if num2 == 0:
        raise ValueError("Cannot perform floor division by zero.")
    return num1 // num2


print(add(5, 3))
print(subtract(5, 3))
print(multiply(5, 3))
print(divide(5, 2))
print(power(2, 3))
print(modulus(5, 3))
print(floor_divide(5, 2))
