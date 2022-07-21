class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
        self.defense = 0
        self.vampirism = 0

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


class Vampire(Warrior):
    def __init__(self):
        super().__init__()
        self.health = 40
        self.attack = 4
        self.vampirism = 50


class Army:
    def __init__(self):
        self.units = []

    def add_units(self, unit_type, unit_amount):
        self.units.extend([unit_type() for _ in range(unit_amount)])


class Battle:
    def __init__(self):
        pass

    def fight(self, army1, army2):
        unit1 = army1.units[0]
        unit2 = army2.units[0]
        while len(army1.units) > 0 and len(army2.units) > 0:
            if fight(unit1, unit2):
                del army2.units[0]
                if len(army2.units) > 0:
                    unit2 = army2.units[0]
                else:
                    return True
            else:
                del army1.units[0]
                if len(army1.units) > 0:
                    unit1 = army1.units[0]
                else:
                    return False


def fight(fighter1, fighter2):
    damage = (fighter1.attack - fighter2.defense) * (fighter1.attack > fighter2.defense)
    fighter2.health -= damage
    fighter1.health += damage * fighter1.vampirism/100
    if fighter2.is_alive:
        fight(fighter2, fighter1)
    return fighter1.is_alive


if __name__ == '__main__':
    army_1 = Army()
    army_2 = Army()
    army_1.add_units(Defender, 5)
    army_1.add_units(Vampire, 6)
    army_1.add_units(Warrior, 7)
    army_2.add_units(Warrior, 6)
    army_2.add_units(Defender, 6)
    army_2.add_units(Vampire, 6)
    battle = Battle()
    print(battle.fight(army_1, army_2))
