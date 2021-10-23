class Polygon:

    def __init__(self, n, name):
        self.n = n
        self.sides = [0 for _ in range(n)]
        self.name = name

    def inputSides(self):
        self.sides = [float(input(f"Enter side {i + 1} : ")) for i in range(self.n)]

    def disSides(self):
        for i in range(self.n):
            print(f"Side", i + 1, "is", self.sides[i])

    def say_name(self):
        return "My name is " + self.__get_name()

    def __get_name(self):
        return self.name
