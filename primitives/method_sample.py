class Car:                                  # Define class Car
    def describe(self, wheel):                     # Define an instance method 'describe'
        print("This car has", wheel," wheels.")     # Simple behavior: print a message

c = Car()                                   # Create an instance of Car
c.describe(4)                                # Call the method on the instance (prints message)