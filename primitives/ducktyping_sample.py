from interface_protocol_sample import ElectricCar
class Boat:
    def start(self):
        return "boat motor on"                 	# Boat provides start() method

def boot_vehicle(v):
    return v.start()                         	# no type checks — rely on presence of start()

print(boot_vehicle(Boat()))                 	# works because Boat has start()
print(boot_vehicle(ElectricCar(75)))       		# works because ElectricCar implements start()
