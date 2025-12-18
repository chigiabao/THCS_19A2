import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        return math.sqrt(dx*dx + dy*dy)
p1 = Point(0, 0)
p2 = Point(3, 4)
kc = p1.distance(p2)
print(f"Khoảng cách giữa 2 điểm: {kc}")