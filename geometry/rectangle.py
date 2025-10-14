# rectangle.py
from __future__ import annotations
from dataclasses import dataclass

class Rectangle:
    """A simple axis-aligned rectangle defined by width and height.

    The Rectangle stores width and height as floats. Both dimensions must be
    non-negative. The class provides methods to compute area and perimeter.
    """

    def __init__(self, width: float, height: float) -> None:
        """
        Initialize a Rectangle.

        :param width: non-negative width of the rectangle
        :param height: non-negative height of the rectangle
        :raises ValueError: if width or height is negative
        """
        if not isinstance(width, (int, float)):
            raise TypeError("width must be a number")
        if not isinstance(height, (int, float)):
            raise TypeError("height must be a number")

        if width < 0 or height < 0:
            raise ValueError("width and height must be non-negative")

        # store as floats for consistent numeric behavior
        self.width: float = float(width)
        self.height: float = float(height)

    def area(self) -> float:
        """Return the area (width * height)."""
        return self.width * self.height

    def perimeter(self) -> float:
        """Return the perimeter (2 * (width + height)). For zero dimensions returns 0."""
        # if either dimension is zero, perimeter is 2*(w+h) which may be 0
        return 2 * (self.width + self.height)

    def __repr__(self) -> str:
        """Unambiguous representation for debugging."""
        return f"Rectangle(width={self.width!r}, height={self.height!r})"

    def __str__(self) -> str:
        """User-friendly string representation."""
        return f"Rectangle(width={self.width}, height={self.height})"