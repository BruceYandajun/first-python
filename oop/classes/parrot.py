class Parrot:
    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sing(self, song):
        print("{} sing {}".format(self.name, song))

    def dance(self):
        print("{} is dancing".format(self.name))


blue = Parrot("Blue", 10)
wood = Parrot("Wood", 15)
print("Blue is a {}".format(blue.__class__.species))
print("Wood is a {}".format(wood.__class__.species))

print("{} is {} years old".format(blue.name, blue.age))
print("{} is {} years old".format(wood.name, wood.age))

blue.sing("Happy")
blue.dance()
