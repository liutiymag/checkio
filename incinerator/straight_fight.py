class Warrior:
    def __init__(self):
        self.max_health = 50
        self.health = 50
        self.attack = 5
        self.defense = 0
        self.vampirism = 0.0  # rate
        self.extra_damage = 0.0  # rate
        self.healing = 0

    @property
    def is_alive(self):
        return self.health > 0

    def heal(self, unit):
        unit.health += self.healing
        if unit.health > unit.max_health:
            unit.health = unit.max_health


class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7


class Defender(Warrior):
    def __init__(self):
        super().__init__()
        self.max_health = 60
        self.health = 60
        self.attack = 3
        self.defense = 2


class Vampire(Warrior):
    def __init__(self):
        super().__init__()
        self.max_health = 40
        self.health = 40
        self.attack = 4
        self.vampirism = 0.5


class Lancer(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 6
        self.extra_damage = 0.5


class Healer(Warrior):
    def __init__(self):
        super().__init__()
        self.max_health = 60
        self.health = 60
        self.attack = 0
        self.healing = 2


class Army:
    def __init__(self):
        self.units = []

    def add_units(self, unit_class, count):
        # Add amount of specified units into army
        for _ in range(count):
            self.units.append(unit_class())

    def get_unit(self):
        # Return current unit and next unit
        return self.units[0], self.units[1] if self.size > 1 else None

    @property
    def size(self):
        return len(self.units)

    def delete_dead_units(self):
        self.units = [unit for unit in self.units if unit.is_alive]


class Battle:
    @staticmethod
    def fight(army1, army2):
        unit1, unit1_next = army1.get_unit()
        unit2, unit2_next = army2.get_unit()
        while army1.size > 0 and army2.size > 0:
            if fight(unit1, unit2, unit1_next, unit2_next):
                del army2.units[0]
                if army2.size > 0:
                    unit2, unit2_next = army2.get_unit()
                else:
                    return True
            else:
                del army1.units[0]
            if army1.size > 0:
                unit1, unit1_next = army1.get_unit()
            else:
                return False

    def straight_fight(self, army1, army2):
        if army1.size > 0 and army2.size > 0:
            for i in range(min(army1.size, army2.size)):
                fight(army1.units[i], army2.units[i])
            army1.delete_dead_units()
            army2.delete_dead_units()
            self.straight_fight(army1, army2)

        return army1.size > 0


def make_hit(unit_1, unit_2, damage):
    damage = 0 if damage < 0 else damage
    unit_2.health -= damage
    unit_1.health += unit_1.vampirism * damage
    return unit_1, unit_2


def fight(unit_1, unit_2, unit_1_next=None, unit_2_next=None):
    if unit_1_next:
        unit_1_next.heal(unit_1)
    damage = unit_1.attack - unit_2.defense
    unit_1, unit_2 = make_hit(unit_1, unit_2, damage)
    if unit_2_next:
        extra_damage = unit_1.extra_damage * damage - unit_2_next.defense
        unit_1, unit_2_next = make_hit(unit_1, unit_2_next, extra_damage)
    if unit_2.is_alive:
        fight(unit_2, unit_1, unit_2_next, unit_1_next)
    return unit_1.is_alive


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
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()
    freelancer = Lancer()
    vampire = Vampire()
    priest = Healer()

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
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True
    assert fight(freelancer, vampire) == True
    assert freelancer.is_alive == True
    assert freelancer.health == 14
    priest.heal(freelancer)
    assert freelancer.health == 16

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Healer, 1)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Lancer, 2)
    my_army.add_units(Healer, 1)
    my_army.add_units(Warrior, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Lancer, 4)
    enemy_army.add_units(Healer, 1)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)
    enemy_army.add_units(Healer, 1)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Lancer, 1)
    army_3.add_units(Healer, 1)
    army_3.add_units(Defender, 2)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 1)
    army_4.add_units(Healer, 1)
    army_4.add_units(Lancer, 2)

    army_5 = Army()
    army_5.add_units(Warrior, 10)

    army_6 = Army()
    army_6.add_units(Warrior, 6)
    army_6.add_units(Lancer, 5)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    res = battle.straight_fight(army_5, army_6)
    assert res == False
