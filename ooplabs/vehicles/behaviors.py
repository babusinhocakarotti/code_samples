# ooplabs/vehicles/behaviors.py

"""
Drive behavior strategies demonstrating the Strategy Pattern.

Allows different types of vehicles to change their driving logic at runtime.
"""

from typing import Protocol  # Used for defining behavior interface (duck typing)
from ooplabs.utils.logging import get_logger  # Logger setup

logger = get_logger(__name__)

# ---------------------------------------------------------------------------
# Drive strategy protocol (acts like an interface)
# ---------------------------------------------------------------------------
class DriveBehavior(Protocol):
    """Defines a driving behavior protocol (duck typing)."""

    def drive(self, vehicle_name: str) -> str:
        """Perform a drive action and return a status message."""
        ...

# ---------------------------------------------------------------------------
# Concrete driving strategies
# ---------------------------------------------------------------------------
class NormalDrive:
    """Default driving behavior for most vehicles."""

    def drive(self, vehicle_name: str) -> str:
        message = f"{vehicle_name} is driving normally."
        logger.info(message)
        return message


class SportDrive:
    """Aggressive driving behavior (for sports cars)."""

    def drive(self, vehicle_name: str) -> str:
        message = f"{vehicle_name} is driving in SPORT mode! "
        logger.info(message)
        return message


class EcoDrive:
    """Energy-efficient driving behavior (for electric or hybrid vehicles)."""

    def drive(self, vehicle_name: str) -> str:
        message = f"{vehicle_name} is driving economically"
        logger.info(message)
        return message