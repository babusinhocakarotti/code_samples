import math
import pytest
from point import Point
from circle import Circle

def test_circle_area():
    c = Circle(Point(0,0), 1)
    assert abs(c.area() - math.pi) < 1e-9

def test_contains():
    c = Circle(Point(1,1), 2)
    assert c.contains(Point(2,1)) is True
    assert c.contains(Point(4,1)) is False
