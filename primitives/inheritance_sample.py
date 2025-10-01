class Vehicle:                                  # Base class for transport types
    def __init__(self, make: str, year: int):    # Constructor for Vehicle
        self.make = make                         # Public attribute: manufacturer/make
        self.year = year                         # Public attribute: manufacturing year

    def info(self) -> str:                       # Common method returning a short description
        return f"{self.make} ({self.year})"      # Build and return a descriptive string

class Car(Vehicle):                              # Car inherits from Vehicle
    def __init__(self, make: str, year: int, model: str):
        super().__init__(make, year)             # Call Vehicle constructor to set make/year
        self.model = model                       # Car-specific attribute: model

    def info(self) -> str:                       # Optionally override info to include model
        base = super().info()                    # Call parent's info to reuse code
        return f"{base} - {self.model}"          # Extend parent's description with model

class Bicycle(Vehicle):                          # Bicycle also inherits from Vehicle
    def __init__(self, make: str, year: int, gear_count: int):
        super().__init__(make, year)             # Initialize make/year with parent constructor
        self.gear_count = gear_count             # Bicycle-specific attribute: number of gears

    def info(self) -> str:                       # Override info to include gears
        base = super().info()                    # Reuse Vehicle.info
        return f"{base} - {self.gear_count} gears" # Add bike-specific detail
    

v = Vehicle("Generic", 1999)         # Base vehicle instance
print(v.info())                      # Prints "Generic (1999)"

c = Car("Toyota", 2021, "Corolla")   # Car instance
print(c.info())                      # Prints "Toyota (2021) - Corolla"

b = Bicycle("Giant", 2019, 21)       # Bicycle instance
print(b.info())                      # Prints "Giant (2019) - 21 gears"