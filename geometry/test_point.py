# test_point.py
import math
import pytest
from point import Point

def test_point_default_constructor():
    p = Point()
    assert p.x == 0.0
    assert p.y == 0.0
    assert repr(p).startswith("Point(")

def test_point_custom_constructor_and_move():
    p = Point(3.0, 4.0)
    assert p.x == 3.0 and p.y == 4.0
    p.move(-1.0, 2.0)
    assert p.x == 2.0 and p.y == 6.0

def test_distance_to_origin():
    p = Point(3.0, 4.0)
    assert math.isclose(p.distance_to_origin(), 5.0, rel_tol=1e-9)
    print("p :",p)
    

