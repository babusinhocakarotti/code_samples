class Vehicle:                                  # Same Vehicle base as before (simplified)
    def start(self):                            # Generic start method interface
        raise NotImplementedError               # Default: children should implement this

class Car(Vehicle):                             # Car implements start
    def start(self):                            # Concrete implementation for Car
        return "Car engine starts with a roar"  # Return a string representing Car start behavior

class Bicycle(Vehicle):                         # Bicycle implements start differently
    def start(self):                            # Concrete implementation for Bicycle
        return "You start pedaling the bicycle" # Return a string representing Bicycle start

def start_all(vehicles: list):                  # Function that uses polymorphism
    for v in vehicles:                          # Iterate over any Vehicle instances
        print(v.start())                        # Call start(); each object runs its own implementation
        

objects = [Car(), Bicycle()]                   # Create different objects (use constructors with no args for brevity)
# Note: if your classes require args, provide them accordingly.
start_all(objects)                             # Calls the correct start() for each object (polymorphic dispatch)