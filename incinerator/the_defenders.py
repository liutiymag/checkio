class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
        self.defense = 0

    @property
    def is_alive(self):
        return self.health > 0


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7


class Defender(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 60
        self.attack = 3
        self.defense = 2


class Army:
    def __init__(self):
        self.units = []

    def add_units(self, unit_type, unit_amount):
        self.units += [unit_type() for i in range(unit_amount)] + self.units


class Battle:
    def __init__(self):
        pass

    @staticmethod
    def fight(army1, army2):
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
    fighter2.health -= (fighter1.attack - fighter2.defense) * (fighter1.attack > fighter2.defense)
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
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 1)

    army_4 = Army()
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
