from abc import ABC, abstractmethod              # Import the Abstract Base Class helpers

class AbstractVehicle(ABC):                      # Define an abstract base class
    @abstractmethod
    def start(self) -> str:                       # Declare abstract method start
        """Start the vehicle and return a status string.""" # Docstring describes contract
        pass                                     # No implementation here; subclasses must implement

    @abstractmethod
    def stop(self) -> str:                        # Declare another abstract method stop
        """Stop the vehicle and return a status string."""
        pass

class Car(AbstractVehicle):                       # Concrete Car must implement abstract methods
    def start(self) -> str:                       # Implement start for Car
        return "Car engine starts"

    def stop(self) -> str:                        # Implement stop for Car
        return "Car engine stops"

class Bicycle(AbstractVehicle):                   # Concrete Bicycle implements the same interface
    def start(self) -> str:                       # Implement start for Bicycle
        return "Begin pedaling"

    def stop(self) -> str:                        # Implement stop for Bicycle
        return "Apply brakes to stop"
    

# AbstractVehicle()                    # Would raise TypeError: can't instantiate abstract class
car = Car()                              # Valid: Car implements required methods
bike = Bicycle()                         # Valid: Bicycle implements required methods
print(car.start(), car.stop())           # Use methods defined by the abstract interface
print(bike.start(), bike.stop())         # Same interface, different implementations
