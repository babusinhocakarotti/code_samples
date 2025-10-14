# ooplabs/utils/events.py

"""
Event system for the OOP Labs project.

Implements the Observer pattern (Publisher-Subscriber model).
Allows different components to subscribe and react to project-wide events.
"""

from typing import Callable, Dict, List         # Import type hints
from ooplabs.utils.logging import get_logger    # Import logger utility

# Create a logger for this module
logger = get_logger(__name__)

# ---------------------------------------------------------------------------
# Core EventBus Implementation
# ---------------------------------------------------------------------------
class EventBus:
    """
    A lightweight static event bus for broadcasting events
    to registered listener functions (observers).
    """

    _subscribers: Dict[str, List[Callable]] = {}  # Stores event_name -> list of callbacks

    @classmethod
    def subscribe(cls, event_name: str, listener: Callable):
        """
        Register a listener function to a specific event.

        Args:
            event_name (str): Unique name of the event
            listener (Callable): Function to call when event is emitted
        """
        # Add listener to the list
        cls._subscribers.setdefault(event_name, []).append(listener)
        logger.debug(f"Listener {listener.__name__} subscribed to '{event_name}'")

    @classmethod
    def emit(cls, event_name: str, *args, **kwargs):
        """
        Trigger an event and notify all registered listeners.

        Args:
            event_name (str): The event name to trigger
            *args: Positional arguments passed to the listeners
            **kwargs: Keyword arguments passed to the listeners
        """
        listeners = cls._subscribers.get(event_name, [])
        if not listeners:
            logger.warning(f"No listeners registered for event '{event_name}'")
            return

        logger.info(f"Emitting event '{event_name}' to {len(listeners)} listener(s).")
        for listener in listeners:
            try:
                listener(*args, **kwargs)  # Safely call each listener
            except Exception as e:
                logger.error(f"Error in listener {listener.__name__}: {e}")

    @classmethod
    def clear(cls):
        """Clear all subscribers (useful for resetting during tests)."""
        cls._subscribers.clear()
        logger.debug("EventBus subscribers cleared.")