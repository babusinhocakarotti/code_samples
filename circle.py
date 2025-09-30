import math
from point import Point

class Circle:
    def __init__(self, center: Point, radius: float):
        if radius < 0:
            raise ValueError("radius must be non-negative")
        self.center = center
        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)

    def circumference(self) -> float:
        return 2 * math.pi * self.radius

    def contains(self, point: Point) -> bool:
        dx = point.x - self.center.x
        dy = point.y - self.center.y
        return dx*dx + dy*dy <= self.radius * self.radius
