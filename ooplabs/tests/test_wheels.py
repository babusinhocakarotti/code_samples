# ooplabs/tests/test_wheels.py

"""
Integration test for Mechanic and VehicleFactory classes.
Demonstrates Factory Pattern + Observer Pattern.
"""

from ooplabs.vehicles.mechanic import VehicleFactory, Mechanic
from ooplabs.vehicles.base import Engine
from ooplabs.utils.logging import get_logger

logger = get_logger(__name__)


def test_factory_and_mechanic_flow():
    """Full integration test with event flow."""
    # Register a mechanic listener
    mechanic = Mechanic("Alex")

    # Use factory to create a new car
    car = VehicleFactory.create_vehicle(
        "car", brand="Subaru", model="Impreza", year=2021, engine=Engine(250)
    )

    # Start engine (will trigger EventBus notification)
    car.start_engine()

    # Move and stop car
    drive_msg = car.move()
    stop_msg = car.stop()
    car.stop_engine()

    print(drive_msg)
    print(stop_msg)
    logger.info(drive_msg)
    logger.info(stop_msg)

    assert "driving" in drive_msg