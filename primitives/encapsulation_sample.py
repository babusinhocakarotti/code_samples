class Car:                                        # Define a Car class
    def __init__(self, model: str, year: int):    # Constructor: initialize a new Car
        self.model = model                        # Public attribute: model name
        self.year = year                          # Public attribute: manufacturing year
        self.__speed = 0                          # Private attribute: current speed (encapsulated)

    def accelerate(self, delta: int):             # Public method to increase speed
        if delta < 0:                             # Validate input: delta must be non-negative
            raise ValueError("delta must be >= 0")# Raise error on invalid input
        self.__speed += delta                      # Modify private attribute __speed
        return self.__speed                        # Return new speed for convenience

    def brake(self, delta: int):                   # Public method to reduce speed
        if delta < 0:                              # Validate input again
            raise ValueError("delta must be >= 0") # Raise error on invalid input
        self.__speed = max(0, self.__speed - delta)# Ensure speed never goes below zero
        return self.__speed                        # Return new speed

    @property
    def speed(self) -> int:                        # Read-only property to access encapsulated speed
        return self.__speed                       # Return the private attribute's value
    
c = Car("Toyota", 2020)            # Create a Car instance
print(c.model, c.year)             # Access public attributes (works)
print(c.speed)                     # Access speed via the public property (safe)
c.accelerate(30)                   # Increase speed by 30
print(c.speed)                     # Now speed shows updated value
# print(c.__speed)                 # Would raise AttributeError (encapsulated/private)