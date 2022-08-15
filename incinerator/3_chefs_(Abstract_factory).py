class AbstractCook:
    total_food_price = 0
    total_drink_price = 0
    food_name = ''
    drink_name = ''

    def add_food(self, food_amount, food_price):
        self.total_food_price += food_amount*food_price

    def add_drink(self, drink_amount, drink_price):
        self.total_drink_price += drink_amount * drink_price

    def total(self):
        return f'{self.food_name}: {self.total_food_price}, {self.drink_name}: {self.total_drink_price}, ' \
               f'Total: {self.total_food_price+self.total_drink_price}'


class JapaneseCook(AbstractCook):
    food_name = 'Sushi'
    drink_name = 'Tea'


class RussianCook(AbstractCook):
    food_name = 'Dumplings'
    drink_name = 'Compote'


class ItalianCook(AbstractCook):
    food_name = 'Pizza'
    drink_name = 'Juice'


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    client_1 = JapaneseCook()
    client_1.add_food(2, 30)
    client_1.add_food(3, 15)
    client_1.add_drink(2, 10)

    client_2 = RussianCook()
    client_2.add_food(1, 40)
    client_2.add_food(2, 25)
    client_2.add_drink(5, 20)

    client_3 = ItalianCook()
    client_3.add_food(2, 20)
    client_3.add_food(2, 30)
    client_3.add_drink(2, 10)

    assert client_1.total() == "Sushi: 105, Tea: 20, Total: 125"
    assert client_2.total() == "Dumplings: 90, Compote: 100, Total: 190"
    assert client_3.total() == "Pizza: 100, Juice: 20, Total: 120"
    print("Coding complete? Let's try tests!")