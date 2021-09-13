class Sample:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # this method will be called when we print the object
    def __str__(self):
        return f"{self.name} is {self.age} years old."


sample = Sample("Harry", 20)
print(sample)
