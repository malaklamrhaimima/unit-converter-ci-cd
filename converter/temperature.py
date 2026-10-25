ABSOLUTE_ZERO_C = -273.15


def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit. Raises ValueError below absolute zero."""
    if c < ABSOLUTE_ZERO_C:
        raise ValueError("Temperature below absolute zero")
    return c * 9 / 5 + 32


def fahrenheit_to_celsius(f):
    """Convert Fahrenheit to Celsius. Raises ValueError below absolute zero."""
    c = (f - 32) * 5 / 9
    if c < ABSOLUTE_ZERO_C:
        raise ValueError("Temperature below absolute zero")
    return c
