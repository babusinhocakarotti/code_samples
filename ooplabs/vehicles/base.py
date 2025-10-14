# ooplabs/vehicles/base.py

"""
Base abstract classes and interfaces for all vehicle types.
Demonstrates abstraction, encapsulation, and inheritance.
"""

from abc import ABC, abstractmethod             # Import ABC base for abstraction
from dataclasses import dataclass               # To define simple data structures
from typing import Optional                     # For type hinting optional values
from ooplabs.utils.logging import get_logger    # Shared logger
from ooplabs.utils.events import EventBus  # Event handling
from ooplabs.vehicles.exceptions import EngineFailure

# Create a logger instance for this module
logger = get_logger(__name__)

# ---------------------------------------------------------------------------
# Engine class demonstrating composition and encapsulation
# ---------------------------------------------------------------------------
@dataclass
class Engine:
    """A simple class representing a vehicle engine."""

    horsepower: int  # Engine power rating
    is_running: bool = False  # Engine state (encapsulated flag)

    def start(self):
        """Start the engine if not already running."""
        if self.is_running:
            logger.debug("Engine is already running.")
            return
        logger.info(f"Starting engine ({self.horsepower} HP)")
        self.is_running = True

    def stop(self):
        """Stop the engine."""
        if not self.is_running:
            logger.warning("Attempt to stop an engine that isn't running.")
        self.is_running = False
        logger.info("Engine stopped.")

# ---------------------------------------------------------------------------
# Abstract Vehicle class
# ---------------------------------------------------------------------------
class Vehicle(ABC):
    """
    Abstract base class for all vehicle types.
    Demonstrates:
        - Abstract methods (abstraction)
        - Protected attributes (encapsulation)
        - Common shared behavior
    """

    def __init__(self, brand: str, model: str, year: int, engine: Optional[Engine] = None):
        # Encapsulated attributes (by convention, underscore prefix)
        self._brand = brand
        self._model = model
        self._year = year
        self._engine = engine
        logger.info(f"Created Vehicle -> {self._brand} {self._model} ({self._year})")

    # --- Properties for encapsulation ---
    @property
    def brand(self) -> str:
        """Get vehicle brand."""
        return self._brand

    @property
    def model(self) -> str:
        """Get vehicle model."""
        return self._model

    @property
    def engine(self) -> Optional[Engine]:
        """Get the vehicle engine (composition)."""
        return self._engine

    # --- Abstract methods for polymorphism ---
    @abstractmethod
    def move(self):
        """Move the vehicle (must be implemented by child classes)."""
        pass

    @abstractmethod
    def stop(self):
        """Stop the vehicle."""
        pass

    def start_engine(self):
        """Safely attempt to start the vehicle engine."""
        if self._engine is None:
            raise EngineFailure("No engine installed!")
        self._engine.start()
        # Emit event for engine start
        EventBus.emit("engine_started", vehicle=self)

    def stop_engine(self):
        """Stop the engine safely."""
        if self._engine:
            self._engine.stop()
            EventBus.emit("engine_stopped", vehicle=self)