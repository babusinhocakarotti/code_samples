from functools import singledispatchmethod

class Logger:
    def log(self, msg: str, level: str = "INFO"):
        print(f"[{level}] {msg}")               			# default argument: level defaults to "INFO"

    def log_many(self, *msgs: str, level: str = "INFO"):
        for m in msgs:
            self.log(m, level=level)            		# variable number of messages handled via *msgs

class Math:
    @singledispatchmethod
    def area(self, shape):
        raise NotImplementedError               		# base: fallback when no registered type matches

    @area.register
    def _(self, radius: float):
        import math
        return math.pi * radius * radius       		# handles call when a float is passed (circle area)

    @area.register
    def _(self, rect: tuple):
        width, height = rect
        return width * height                  			# handles call when a tuple is passed (rectangle area)

m = Math()
print(m.area(2.0))            			# circle area computed by float-registered implementation
print(m.area((3, 4)))        			# rectangle area computed by tuple-registered implementation
