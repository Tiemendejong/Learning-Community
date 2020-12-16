#Add a method reflect_x to Point which returns a new Point,
# one which is the reflection of the point about thex-axis.For example,Point(3, 5).reflect_x()is(3,-5)

class Point:

    def __init__(self, x=0, y=0):

        self.x = x
        self.y = y

    def reflect_x(self):
        return (self.x, -self.y)

p = Point(3, 4)
print(p.reflect_x())