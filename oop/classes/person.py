class Person:
    """This is a person class"""
    age = 10

    def __init__(self, name):
        self.__name = name

    @staticmethod
    def greet():
        print("hello")

    def say(self):
        print("I am {}".format(self.__name))


harry = Person("Harry")

print(Person.age)
Person.greet()
print(Person.greet)
print(Person.say)
print(harry.say)
print(Person.__class__)
print(Person.__doc__)
harry.say()
print(Person.say(harry))
