from accessify import private

class KgToPounds:
    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        return self.__kg * 2.205

    def __kg(self):
        return self.kg

weight = KgToPounds(12)
print(weight.to_pounds())
print(weight.kg)
print(weight.kg)
try:
    weight.kg = 'десять'
except AttributeError:
    print("AttributeError occured")
finally:
    print(weight.kg)