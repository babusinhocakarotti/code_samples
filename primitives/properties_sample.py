class Car:
    def __init__(self):
        self._speed_kmh = 0.0                		# internal storage for speed in km/h

    @property
    def speed_kmh(self):
        return self._speed_kmh               		# getter: attribute-like access for callers

    @speed_kmh.setter
    def speed_kmh(self, value):
        if value < 0:
            raise ValueError("speed cannot be negative")  	# validation in setter
        self._speed_kmh = value              		# set internal value after validation

    @property
    def speed_ms(self):
        return self._speed_kmh / 3.6         		# computed read-only property converting km/h to m/s

c = Car()
c.speed_kmh = 72                        			# setter invoked; validation applies
print(c.speed_ms," m/s")                       		# computed read-only property: 20.0
