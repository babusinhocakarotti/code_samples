# test_rectangle.py
import math
import pytest
from rectangle import Rectangle

def test_rectangle_valid_construction_and_repr():
    r = Rectangle(3.0, 4.0)
    assert r.width == 3.0 and r.height == 4.0
    assert "Rectangle" in repr(r) or "Rectangle" in str(r)

def test_rectangle_area_perimeter():
    r = Rectangle(5.0, 2.0)
    assert math.isclose(r.area(), 10.0, rel_tol=1e-9)
    assert math.isclose(r.perimeter(), 14.0, rel_tol=1e-9)

def test_rectangle_zero_dimensions():
    r = Rectangle(0.0, 0.0)
    assert r.area() == 0.0
    assert r.perimeter() == 0.0

def test_rectangle_negative_dimensions_raise():
    with pytest.raises(ValueError):
        Rectangle(-1.0, 2.0)
    with pytest.raises(ValueError):
        Rectangle(1.0, -2.0)
    with pytest.raises(ValueError):
        Rectangle(-1.0, -2.0)