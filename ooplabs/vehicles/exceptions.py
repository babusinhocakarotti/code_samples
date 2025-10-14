# ooplabs/vehicles/exceptions.py

"""
Custom exceptions for the OOP Labs Vehicles module.
"""

class VehicleError(Exception):
    """Base class for all vehicle-related exceptions."""
    pass


class EngineFailure(VehicleError):
    """Raised when the engine fails to start or operate."""
    pass


class MaintenanceError(VehicleError):
    """Raised when a repair or maintenance action fails."""
    pass


class InvalidOperationError(VehicleError):
    """Raised for invalid or unsupported operations."""
    pass