class VIN:
    def __init__(self, vin: str):
        self.vin = vin                        		# store VIN string

    def __eq__(self, other):
        if not isinstance(other, VIN):
            return NotImplemented              		# let other fallbacks handle comparison
        return self.vin == other.vin           		# equality by VIN value

    def __hash__(self):
        return hash(self.vin)                   	# hashing based on VIN string

    def __repr__(self):
        return f"VIN({self.vin!r})"            		# helpful debug representation

a = VIN("1HGCM82633A004352")
b = VIN("1HGCM82633A004352")
assert a == b                             			# uses __eq__
d = {a: "vehicle"}                        			# uses __hash__ to be dict key
print(a)                                  			# uses __repr__
