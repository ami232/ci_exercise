"""Simple calculator module for CI demonstration."""


def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Divide a by b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(
    base: float, exponent: float
) -> float:  # LINT ERROR: Missing type annotations (MyPy)
    """Raise base to the power of exponent."""
    result: float = base**exponent
    return result
