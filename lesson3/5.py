class Nikola:

    name = "Nikolay"

    def __init__(self, custom_name, age):
        if str(self.name) != str(custom_name):
            self.name = "I am not "+custom_name+", but Nikolay"
        self.age = age
        self._surname = "Nikolaev"

    @property
    def surname(self):
        return self._surname

person1 = Nikola("Ivan", 31)
person2 = Nikola("Nikolay", 14)
print(person1.name)
print(person2.name)
try:
    person2.surname = "Petrov"
    print(person2.surname)
except AttributeError:
    print("Attribute didn't change - error occured")