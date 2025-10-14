from abc import ABC, abstractmethod
from typing import Protocol

class Starter(Protocol):
    def start(self) -> str:
        ...                                 # Protocol: requires a start() method returning str

class AbstractVehicle(ABC):
    @abstractmethod
    def start(self) -> str:
        pass                                # ABC: subclasses must implement start()

    @abstractmethod
    def stop(self) -> str:
        pass                                # ABC: subclasses must implement stop()

class ElectricCar(AbstractVehicle):
    def __init__(self, battery_kwh: float):
        self.battery_kwh = battery_kwh      # store battery capacity

    def start(self) -> str:
        return "Electric motor whirs to life"  # implement start()

    def stop(self) -> str:
        return "Regenerative braking stops the car" 	# implement stop()
    
    def __repr__(self):
        return f"ElectricCar(battery_kwh={self.battery_kwh})"

class Engine:
    def __init__(self, horsepower: int):
        self.horsepower = horsepower           # store horsepower for engine objects

class Car(AbstractVehicle):
    def __init__(self, engine: Engine):
        self.engine = engine

    def start(self) -> str:
        return "Car started"  # implement start()

    def stop(self) -> str:
        return "Car stopped" 	# implement stop()

    def __repr__(self):
        return f"Car(engine={self.engine.horsepower})"


def ensure_can_start(v: Starter):
    print(v.start())                        # accepts any object that exposes start(), using Protocol/duck typing

c= Car(Engine(100))
c.start()

e=ElectricCar(150)
e.start()

print("Car: ", c, "eCar: ", e)
