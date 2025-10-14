# ooplabs/tests/test_car.py

"""
Pytest test module for Car class.
Covers:
    - Engine start/stop
    - Drive behaviors (Strategy Pattern)
    - Factory creation and InvalidOperationError handling
"""

import pytest  # Test framework
from ooplabs.vehicles.base import Engine                        # Engine component
from ooplabs.vehicles.vehicles import Car                       # Concrete vehicle
from ooplabs.vehicles.behaviors import SportDrive, NormalDrive  # Driving strategies
from ooplabs.vehicles.exceptions import InvalidOperationError   # Custom exception
from ooplabs.utils.logging import get_logger                    # Logger factory

logger = get_logger(__name__)


@pytest.fixture
def car() -> Car:
    """Fixture: provides a reusable Car instance for multiple tests."""
    return Car("Toyota", "Supra", 2023, Engine(320))


def test_car_start_and_drive(car):
    """Test that car starts, drives, and stops correctly."""
    car.start_engine()
    result = car.move()
    print(result)
    logger.info(result)
    car.stop_engine()
    assert "driving" in result


def test_drive_strategy_switch(car):
    """Test dynamic behavior mode switching (Strategy Pattern)."""
    car.start_engine()
    car.change_drive_mode(SportDrive())
    result = car.move()
    print(result)
    logger.info(result)
    car.change_drive_mode(NormalDrive())
    result2 = car.move()
    print(result2)
    logger.info(result2)
    car.stop_engine()
    assert "SPORT" in result


def test_invalid_drive_without_engine_start(car):
    """Attempt to drive without starting the engine, expecting an exception."""
    with pytest.raises(InvalidOperationError):
        car.move()