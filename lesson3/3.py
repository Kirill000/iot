class Human:

    default_name = "John"
    default_age = 19

    def __init__(self, age=default_age, name=default_name):
        self.name = name
        self.age = age
        self._money = 100
        self.house = 0

    def name(self):
        print(self.name)

    def age(self):
        print(self.age)

    def _money(self):
        print(self._money)

    def _house(self):
        print(self._house)

    def info(self):
        print(
            "My name is " + str(self.name) + ". I am " + str(self.age) + " years old. I have " + str(self._money) + " roubles. I " + "am homeless." * (not self.house) + "have a house." * (self.house)
        )

    def default_info(self):
        print(self.default_name, self.default_age)

    @staticmethod
    def default_info():
        global default_name, default_age
        print(Human.default_age, Human.default_name)

    def make_deal(self, house, cost):
        self.house = house
        self._money = self._money-cost
        print(self._money, self.house)

    def earn_money(self, amount):
        self._money = self._money+amount

    def buy_house(self, house, cost):
        if int(self._money) >= cost:
            self.make_deal(house, cost)
        else:
            print("Too little money for the house!")

class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        return (self._price-discount)

class SmallHouse(House):
    def __init__(self, price):
        self._area = 40

human = Human()
human.default_info()
human.info()
small_house = SmallHouse(180)
human.buy_house(small_house, 180)
human.earn_money(100)
human.buy_house(small_house, 180)