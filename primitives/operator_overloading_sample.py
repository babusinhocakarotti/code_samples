class Distance:
    def __init__(self, meters: float):
        self.meters = meters                     		# store distance in meters

    def __add__(self, other):
        if not isinstance(other, Distance):
            return NotImplemented               		# indicate unsupported operation for given type
        return Distance(self.meters + other.meters)  	# return a new Distance instance (immutable-style)

    def __repr__(self):
        return f"Distance({self.meters} m)"     		# readable representation for debugging

d1 = Distance(3.5)               			# Distance instance
d2 = Distance(1.5)               			# another Distance
print(d1 + d2)                   			# Distance(5.0 m)
