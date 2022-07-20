class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5

    @property
    def is_alive(self):
        return self.health > 0


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7


class Army:
    def __init__(self):
        self.units = []

    def add_units(self, unit_type, unit_amount):
        self.units += [unit_type() for i in range(unit_amount)] + self.units


class Battle:
    def __init__(self):
        pass

    def fight(self, army1, army2):
        army1_fighter = army1.units.pop()
        army2_fighter = army2.units.pop()
        while len(army1.units) >= 0 and len(army2.units) >= 0:
            if fight(army1_fighter, army2_fighter):
                if len(army2.units) > 0:
                    army2_fighter = army2.units.pop()
                else:
                    return True
            else:
                if len(army1.units) > 0:
                    army1_fighter = army1.units.pop()
                else:
                    return False


def fight(fighter1, fighter2):
    fighter2.health -= fighter1.attack
    if fighter2.is_alive:
        fight(fighter2, fighter1)
    return fighter1.is_alive


if __name__ == '__main__':
    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    # battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)

    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
