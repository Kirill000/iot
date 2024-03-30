class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print("The dog "+self.name+" is rolling over")
    def roll_over(self):
        print("The dog "+self.name+" sat")

my_dog = Dog("willie", 6)
print(dir(my_dog))
my_dog.sit()
my_dog.roll_over()