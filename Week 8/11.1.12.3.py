class Point:

    def __init__(self, x=0, y=0):

        self.x = x
        self.y = y

    def SlopeFromOrigin(self):
        return (self.y / self.x)

print(Point(3, 4).SlopeFromOrigin())