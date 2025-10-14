from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: float
    y: float

    def translate(self, dx: float, dy: float):
        return Point(self.x + dx, self.y + dy)    		# return new Point rather than mutating (functional style)

class mPoint:
    def __init__(self, x:float, y:float):
        self.x= x
        self.y= y
        
    def __repr__(self):
        return f"mPoint(x={self.x}, y={self.y})"

p1 = Point(0.0, 0.0)
p2 = p1.translate(1.0, 2.0)                      		# returns new Point(1.0, 2.0)
#p1 = p1.translate(3.0,4.0)

p3 = mPoint(0.0,0.0)
p3.x = 1.0

print('p1: ',p1,' p2: ',p2, ' p3: ',p3)

#p1.x = 10.0    # would raise FrozenInstanceError because dataclass is frozen (immutable)
