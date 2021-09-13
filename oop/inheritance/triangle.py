from oop.inheritance.polygon import Polygon


class Triangle(Polygon):

    def __init__(self):
        super().__init__(3)

    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        # calculate the area
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print('The area of the triangle is %0.2f' % area)


t = Triangle()
t.inputSides()
t.disSides()
t.findArea()

print(isinstance(t, Triangle))
print(isinstance(t, Polygon))
print(isinstance(t, object))

print(issubclass(Triangle, Polygon))
print(issubclass(Triangle, object))
