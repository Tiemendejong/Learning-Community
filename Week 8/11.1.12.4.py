class Point:

    def __init__(self, x=0, y=0, z=0, f=0):

        self.x = x
        self.y = y
        self.z = z
        self.f = f


    def Slope(self):
        return ((self.y - self.f) / (self.x - self.z))

print("y=" ,Point(25, 4, 5, 5).Slope(),"x+b")
