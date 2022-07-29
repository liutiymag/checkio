class Army:
    def train_swordsman(self, name):
        pass

    def train_lancer(self, name):
        pass

    def train_archer(self, name):
        pass


class AsianArmy(Army):
    def train_swordsman(self, name):
        soldier = Swordsman()
        soldier.name = name
        soldier.unit_name = 'Samurai'
        soldier.army_type = 'Asian'
        return soldier

    def train_lancer(self, name):
        soldier = Lancer()
        soldier.name = name
        soldier.unit_name = 'Ronin'
        soldier.army_type = 'Asian'
        return soldier

    def train_archer(self, name):
        soldier = Archer()
        soldier.name = name
        soldier.unit_name = 'Shinobi'
        soldier.army_type = 'Asian'
        return soldier


class EuropeanArmy(Army):
    def train_swordsman(self, name):
        soldier = Swordsman()
        soldier.name = name
        soldier.unit_name = 'Knight'
        soldier.army_type = 'European'
        return soldier

    def train_lancer(self, name):
        soldier = Lancer()
        soldier.name = name
        soldier.unit_name = 'Raubritter'
        soldier.army_type = 'European'
        return soldier

    def train_archer(self, name):
        soldier = Archer()
        soldier.name = name
        soldier.unit_name = 'Ranger'
        soldier.army_type = 'European'
        return soldier


class Swordsman:
    name = ''
    unit_name = ''
    army_type = ''

    def introduce(self):
        return f'{self.unit_name} {self.name}, {self.army_type} swordsman'


class Lancer:
    name = ''
    unit_name = ''
    army_type = ''

    def introduce(self):
        return f'{self.unit_name} {self.name}, {self.army_type} lancer'


class Archer:
    name = ''
    unit_name = ''
    army_type = ''

    def introduce(self):
        return f'{self.unit_name} {self.name}, {self.army_type} archer'


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    my_army = EuropeanArmy()
    enemy_army = AsianArmy()

    soldier_1 = my_army.train_swordsman("Jaks")
    soldier_2 = my_army.train_lancer("Harold")
    soldier_3 = my_army.train_archer("Robin")

    soldier_4 = enemy_army.train_swordsman("Kishimoto")
    soldier_5 = enemy_army.train_lancer("Ayabusa")
    soldier_6 = enemy_army.train_archer("Kirigae")

    assert soldier_1.introduce() == "Knight Jaks, European swordsman"
    assert soldier_2.introduce() == "Raubritter Harold, European lancer"
    assert soldier_3.introduce() == "Ranger Robin, European archer"

    assert soldier_4.introduce() == "Samurai Kishimoto, Asian swordsman"
    assert soldier_5.introduce() == "Ronin Ayabusa, Asian lancer"
    assert soldier_6.introduce() == "Shinobi Kirigae, Asian archer"

    print("Coding complete? Let's try tests!")
