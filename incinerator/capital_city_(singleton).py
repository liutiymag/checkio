class Capital:
    def __new__(cls, city_name):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
            cls.instance.city_name = city_name
        return cls.instance

    def name(self):
        return self.city_name

    @classmethod
    def destroy(cls):
        del cls.instance


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    ukraine_capital_1 = Capital("Kyiv")
    ukraine_capital_2 = Capital("London")
    ukraine_capital_3 = Capital("Marocco")

    assert ukraine_capital_2.name() == "Kyiv"
    assert ukraine_capital_3.name() == "Kyiv"

    assert ukraine_capital_2 is ukraine_capital_1
    assert ukraine_capital_3 is ukraine_capital_1

    Capital.destroy()

    ukraine_capital_3 = Capital("Marocco")
    ukraine_capital_2 = Capital("London")
    assert ukraine_capital_3.name() == "Marocco"
    assert ukraine_capital_2.name() == "Marocco"
