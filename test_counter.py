# test_counter.py
import pytest
from counter import Counter

def test_counter_initial_value_default():
    c = Counter()
    assert c.value() == 0

def test_counter_initial_value_custom():
    c = Counter(start=5)
    assert c.value() == 5

def test_counter_increment_decrement():
    c = Counter()
    c.increment()
    assert c.value() == 1
    c.increment(4)
    assert c.value() == 5
    c.decrement()
    assert c.value() == 4
    c.decrement(2)
    assert c.value() == 2

def test_counter_reset():
    c = Counter(10)
    c.reset()
    assert c.value() == 0

def test_counter_negative_steps_allowed():
    # depending on design, negative steps might be allowed; test current contract
    c = Counter()
    c.increment(-1)
    assert c.value() == -1