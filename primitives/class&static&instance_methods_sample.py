class Vehicle:
    registry = {}                			# class-level registry shared across class and subclasses

    def __init__(self, make: str, year: int):
        self.make = make         		    # instance attribute
        self.year = year        			# instance attribute

    @classmethod
    def register(cls, name: str, factory):
        cls.registry[name] = factory        # classmethod manipulates class-level registry

    @staticmethod
    def is_motorized():
        return True                         # staticmethod: utility independent of class/instance

    def info(self):
        return f"{self.make} ({self.year})" # instance method uses instance state

Vehicle.register("generic", lambda: Vehicle("Generic", 2000))  	# register factory at class level
print(Vehicle.is_motorized())     					            # True (static utility)
v = Vehicle("Toyota", 2021)
print(v.info())                   						        # "Toyota (2021)" (instance method)
