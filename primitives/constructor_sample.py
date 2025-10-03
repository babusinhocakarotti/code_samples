class Car:                                      # Define class Car
    def __init__(self, model, year):            # Constructor: runs when a new Car is created
        self.model = model                      # Set instance attribute 'model' from argument
        self.year = year                        # Set instance attribute 'year' from argument
        print(f"Created {self.year} {self.model}")  # Informational print during initialization

    def describe(self):                         # Instance method that uses instance attributes
        print(f"This car is a {self.year} {self.model}")  # Use self.model and self.year

my_car = Car("Tesla Model 3", 2022)             # Create a Car object and initialize attributes
my_2ndcar=Car("Porche Cayenne TurboS",2017)
my_car.describe()                               # Call the method that prints the initialized attributes
my_2ndcar.describe()