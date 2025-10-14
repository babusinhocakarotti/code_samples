# test_circle.py
import math
import pytest
from point import Point
from circle import Circle

def test_circle_constructor_negative_radius_raises():
    with pytest.raises(ValueError):
        Circle(Point(0,0), -1.0)

def test_circle_area_and_circumference():
    c = Circle(Point(0,0), 1.0)
    assert math.isclose(c.area(), math.pi, rel_tol=1e-9)
    assert math.isclose(c.circumference(), 2 * math.pi, rel_tol=1e-9)

def test_circle_contains_inside_outside():
    c = Circle(Point(1, 1), 2.0)
    # point inside
    assert c.contains(Point(2,1)) is True
    # point on boundary -> depending on implementation contains may return True (<=)
    assert c.contains(Point(3,1)) is True
    # point outside
    assert c.contains(Point(4,1)) is False

def test_circle_contains_with_same_center():
    c = Circle(Point(0,0), 0.5)
    assert c.contains(Point(0,0)) is True