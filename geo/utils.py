import math

def circle_area(radius):
    """Calculate the area of a circle."""
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return math.pi * radius ** 2
