def add(x, y):
    """Performs addition"""
    return x + y


def subtract(x, y):
    """Performs subtraction"""
    return x - y


def multiply(x, y):
    """Performs multiplication"""
    return x * y


def divide(x, y):
    """Performs division"""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y
