class DriveBehavior:
    def drive(self):
        return "generic driving"               		# base behavior template

class SportDrive(DriveBehavior):
    def drive(self):
        return "sporty drive"                 		# specialized behavior

class EcoDrive(DriveBehavior):
    def drive(self):
        return "eco-friendly drive"           		# another behavior variant

class DrivableCar:
    def __init__(self, drive_behavior: DriveBehavior):
        self.drive_behavior = drive_behavior  		# behavior injected via composition

    def drive(self):
        return self.drive_behavior.drive()     		# delegate to composed behavior

car = DrivableCar(SportDrive())             		# compose car with a sport driving behavior
print(car.drive())                          		# "sporty drive"
car.drive_behavior = EcoDrive()             		# swap behavior at runtime
print(car.drive())                          		# "eco-friendly drive"
