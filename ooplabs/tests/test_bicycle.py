# ooplabs/tests/test_bicycle.py

"""
Test module for Bicycle class.
Demonstrates abstraction, inheritance, and polymorphism.
"""

from ooplabs.vehicles.vehicles import Bicycle   # Bicycle implementation
from ooplabs.utils.logging import get_logger    # Logger factory

logger = get_logger(__name__)


def test_bicycle_move_and_stop():
    """Test movement and stopping of a Bicycle instance."""
    bike = Bicycle("Giant", "Escape 3", 2022)
    msg_move = bike.move()
    msg_stop = bike.stop()
    print(msg_move)
    print(msg_stop)
    logger.info(msg_move)
    logger.info(msg_stop)
    assert "pedaling" in msg_move
    assert "stopped" in msg_stop