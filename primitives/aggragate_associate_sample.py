class Engine:
    def __init__(self, horsepower: int):
        self.horsepower = horsepower 	     # store horsepower value

class Wheel:
    def __init__(self, size: int):
        self.size = size                     # store wheel size

class Driver:
    def __init__(self, name: str):
        self.name = name                      # driver name

class Car:
    def __init__(self, make: str, year: int, model: str, engine: Engine, wheels: list[Wheel]):
        self.make = make                      # instance attribute: make
        self.year = year                      # instance attribute: year
        self.model = model                    # instance attribute: model
        self.engine = engine                  # aggregation: engine passed in (not created here)
        self.wheels = wheels                  # aggregation: wheels passed in (can be shared/replaced)
        self._driver = None                   # association: optional link to Driver, Car doesn't own Driver

    def assign_driver(self, driver: Driver):
        self._driver = driver                 # association: assign external Driver instance

    def remove_driver(self):
        self._driver = None                   # association: remove reference to Driver

    def replace_engine(self, new_engine: Engine):
        self.engine = new_engine              # aggregation: engine replaced by another external Engine

    def __repr__(self):
        return f"Car({self.make}, {self.year}, {self.model})"  	# readable representation

class ComposedCar:
    def __init__(self, make: str, year: int, model: str):
        self.make = make                      # store make
        self.year = year                      # store year
        self.model = model                    # store model
        self.engine = Engine(150)             # composition: Engine created inside (owned by ComposedCar)
        self.wheels = [Wheel(16) for _ in range(4)]  	# composition: Wheels created inside (owned)

class Mechanic:
    def tune(self, car: Car):
        car.replace_engine(Engine(200))       # dependency: Mechanic uses Car's API temporarily to replace engine

