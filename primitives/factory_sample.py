from interface_protocol_sample import Engine, ElectricCar, Car

class VehicleFactory:
    @staticmethod
    def create(kind: str):
        if kind == "car":
            return Car(Engine(130))                 	# create a conventional car
        if kind == "electric":
            return ElectricCar(85)                 		# create an electric car
        raise ValueError("Unknown kind")            	# invalid factory argument

my_car= VehicleFactory.create('car')
print("My Car: ",my_car)

my_ecar= VehicleFactory.create('electric')
print("My eCar:", my_ecar)