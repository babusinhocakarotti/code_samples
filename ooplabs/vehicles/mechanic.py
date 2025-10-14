# ooplabs/vehicles/mechanic.py

"""
Mechanic and VehicleFactory modules.
Demonstrates Factory and Observer patterns.
"""

from ooplabs.vehicles.base import Engine                            # Composition component
from ooplabs.vehicles.vehicles import Car, Bicycle, ElectricCar     # Concrete vehicles
from ooplabs.vehicles.exceptions import MaintenanceError            # Custom exception
from ooplabs.utils.logging import get_logger                        # Logger configuration
from ooplabs.utils.events import EventBus                           # To listen to events

logger = get_logger(__name__)

# ---------------------------------------------------------------------------
# Factory Pattern Implementation
# ---------------------------------------------------------------------------
class VehicleFactory:
    """Factory pattern: creates vehicle instances dynamically."""

    @staticmethod
    def create_vehicle(type_name: str, **kwargs):
        """
        Factory method to instantiate specific vehicle types.
        """
        mapping = {
            "car": Car,
            "bicycle": Bicycle,
            "electric": ElectricCar,
        }

        cls = mapping.get(type_name.lower())
        if not cls:
            raise ValueError(f"Unknown vehicle type: {type_name}")

        logger.info(f"Factory creating new vehicle: {cls.__name__}")
        return cls(**kwargs)

# ---------------------------------------------------------------------------
# Mechanic class observing and repairing vehicles
# ---------------------------------------------------------------------------
class Mechanic:
    """Mechanic observes vehicle events and can repair vehicles."""

    def __init__(self, name: str):
        self.name = name
        EventBus.subscribe("engine_started", self.on_engine_started)
        EventBus.subscribe("engine_stopped", self.on_engine_stopped)
        logger.info(f"Mechanic {self.name} ready for duty.")

    def on_engine_started(self, vehicle):
        logger.info(f"{self.name} noticed {vehicle.model}'s engine started.")

    def on_engine_stopped(self, vehicle):
        logger.info(f"{self.name} noticed {vehicle.model}'s engine stopped.")

    def repair(self, vehicle):
        """Simulates repair logic with exception safety."""
        try:
            logger.info(f"{self.name} is repairing {vehicle.model}...")
            if not vehicle.engine:
                raise MaintenanceError("No engine to repair.")
            vehicle.engine.is_running = False
            logger.info(f"{vehicle.model} repaired successfully by {self.name}.")
            return True
        except Exception as e:
            logger.error(f"Repair failed: {e}")
            return False