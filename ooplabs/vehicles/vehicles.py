# ooplabs/vehicles/vehicles.py

"""
Concrete vehicle implementations using inheritance and polymorphism.
"""

from ooplabs.vehicles.base import Vehicle, Engine                   # Base class and composition object
from ooplabs.vehicles.behaviors import DriveBehavior, NormalDrive   # Strategy pattern
from ooplabs.vehicles.exceptions import InvalidOperationError       # Custom errors
from ooplabs.utils.logging import get_logger                        # Logging
from ooplabs.utils.events import EventBus                           # Event handling

logger = get_logger(__name__)

# ---------------------------------------------------------------------------
# Car class definition
# ---------------------------------------------------------------------------
class Car(Vehicle):
    """Car implementation with support for drive behavior strategy."""

    def __init__(self, brand: str, model: str, year: int, engine: Engine, drive_behavior: DriveBehavior = None):
        super().__init__(brand, model, year, engine)
        self._drive_behavior = drive_behavior or NormalDrive()
        EventBus.emit("vehicle_created", vehicle=self)
        logger.debug(f"Car `{self.model}` initialized with strategy `{type(self._drive_behavior).__name__}`")

    def move(self):
        """Drive the car using its behavior strategy."""
        if self.engine is None or not self.engine.is_running:
            raise InvalidOperationError("Engine must be running to move the car.")
        return self._drive_behavior.drive(f"{self.brand} {self.model}")

    def stop(self):
        """Stop the car."""
        logger.info(f"{self.brand} {self.model} has stopped.")
        return f"{self.brand} {self.model} stopped."

    def change_drive_mode(self, new_behavior: DriveBehavior):
        """Dynamically switch the vehicle's drive strategy."""
        logger.info(f"Changing {self.model}'s drive mode to {type(new_behavior).__name__}")
        self._drive_behavior = new_behavior


# ---------------------------------------------------------------------------
# Bicycle class (no engine, pure polymorphism)
# ---------------------------------------------------------------------------
class Bicycle(Vehicle):
    """Bicycle implementation without an engine."""

    def __init__(self, brand: str, model: str, year: int):
        super().__init__(brand, model, year)
        EventBus.emit("vehicle_created", vehicle=self)

    def move(self):
        """Pedal the bicycle."""
        msg = f"{self.brand} {self.model} is pedaling 🌀"
        logger.info(msg)
        return msg

    def stop(self):
        """Stop the bicycle."""
        msg = f"{self.brand} {self.model} stopped safely."
        logger.info(msg)
        return msg


# ---------------------------------------------------------------------------
# ElectricCar subclass demonstrating method overriding
# ---------------------------------------------------------------------------
class ElectricCar(Car):
    """Electric car demonstrates method overriding and reusability."""

    def move(self):
        """Override move to show eco-drive handling."""
        if self.engine and not self.engine.is_running:
            raise InvalidOperationError("Battery must be active to move the electric car.")
        msg = f"{self.brand} {self.model} is gliding silently ⚡"
        logger.info(msg)
        return msg