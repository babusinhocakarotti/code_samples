# ooplabs/tests/test_my_car.py

"""
Tests for ElectricCar subclass.
Validates overriding, polymorphism, and event emission.
"""

import pytest
from ooplabs.vehicles.base import Engine
from ooplabs.vehicles.vehicles import ElectricCar
from ooplabs.vehicles.exceptions import InvalidOperationError
from ooplabs.utils.events import EventBus
from ooplabs.utils.logging import get_logger

logger = get_logger(__name__)


@pytest.fixture
def electric_car() -> ElectricCar:
    """Fixture: Provides ElectricCar instance."""
    car = ElectricCar("Tesla", "Model S", 2024, Engine(500))
    return car


def test_electric_car_drive_and_stop(electric_car):
    """Start, drive and stop electric car."""
    EventBus.clear()  # To ensure clean state
    electric_car.start_engine()
    result = electric_car.move()
    print(result)
    electric_car.stop_engine()
    logger.info(result)
    assert "gliding silently" in result


def test_drive_without_battery(electric_car):
    """Expect exception when engine is not running."""
    with pytest.raises(InvalidOperationError):
        electric_car.move()