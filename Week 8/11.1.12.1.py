def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx * dx + dy * dy
    result = dsquared**0.5
    return result
class Point:

   def __init__(self, p1, p2, a1, a2):
    self.p1 = p1
    self.p2 = p2
    self.p3 = a1
    self.p4 = a2
    p = Point(p1.x, p2.y)
    b = Point(a1.x, a2.y)
    result = p ** 2 + b ** 2
    return result
print(Point)
