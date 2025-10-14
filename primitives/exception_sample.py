from interface_protocol_sample import Engine

class VehicleError(Exception):
    """Base exception for vehicle domain errors."""  		# domain base exception

class EngineFailure(VehicleError):
    pass                                              		# specific engine failure

class Car:
    def __init__(self, engine: Engine):
        self.engine = engine                        		# store engine

    def start(self):
        if self.engine.horsepower <= 0:
            raise EngineFailure("Engine has no power")  	# raise domain-specific exception
        return "started"                             		# success case
    
try:
    bad = Car(Engine(0))                              		# engine with zero horsepower
    bad.start()                                       		# will raise EngineFailure
except EngineFailure as e:
    print("Caught:", e)                               		# handle engine-specific case
except VehicleError:
    print("Other vehicle error")                      		# catch other vehicle-related errors
