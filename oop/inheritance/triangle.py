from oop.inheritance.polygon import Polygon


class Triangle(Polygon):

    def __init__(self, name):
        super().__init__(3, name)

    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        # calculate the area
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        print('The area of the triangle is %0.2f' % area)

    def __get_name(self):
        return "Hello" + self.name


t = Triangle("T")
t.inputSides()
t.disSides()
t.findArea()

print(isinstance(t, Triangle))
print(isinstance(t, Polygon))
print(isinstance(t, object))

print(issubclass(Triangle, Polygon))
print(issubclass(Triangle, object))


print(t.say_name())
