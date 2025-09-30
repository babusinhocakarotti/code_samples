class Car:                          # Define a class 'Car'
    wheels = 4                      # Class attribute: shared by all Car instances

car_a = Car()                       # Create first instance of Car
car_b = Car()                       # Create second instance of Car

print(car_a.wheels)                 # Access class attribute via instance (prints 4)
print(car_b.wheels)                 # Access class attribute via another instance (prints 4)

Car.wheels = 3                      # Modify the class attribute on the class itself
print(car_a.wheels)                 # Instances see the updated class attribute (prints 3)
print(car_b.wheels)                 # Same for other instances (prints 3)

car_a.model = "Toyota"              # Create an instance attribute 'model' only on car_a
car_b.model = "TOGG"
print(car_a.model)                  # Access the instance attribute on car_a (prints "Toyota")
print(car_b.model)               # Uncommenting would raise AttributeError: car_b has no 'model'