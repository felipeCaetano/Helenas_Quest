import pygame
from random import randint


class mob:
    pass


# Mobs lvl 2
class Goblin(mob):

    def __init__(self, level=2, life=10, mana=6, attack=7, defense=5, gold=10, image='imagens/mobs/images/goblin_rider.png', pos={'x':0, 'y':0}):

        self._randattr = randint(level - 1, level + 3)
        self.name = 'Goblin'
        self._level = level
        self._life = life
        self._mana = mana
        self._attack = attack
        self._defense = defense
        self._gold = gold
        self._image = image
        self._exp = 10

        self.level = self._randattr
        self.life = self._randattr
        self.mana = self._randattr
        self.attack = self._randattr
        self.defense = self._randattr
        self.gold = self._randattr
        self.exp = self._randattr

    @property
    def exp(self):
        return self._exp

    @exp.setter
    def exp(self, value):
        self._exp = int(self.exp + (1.2 * value))

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = self.level+(value-self.level)

    @property
    def life(self):
        return self._life

    @life.setter
    def life(self, value):
        self._life = int(self.life+(1.2*value))

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, value):
        self._mana = int(self.mana+(1.2*value))

    @property
    def attack(self):
        return self._attack

    @attack.setter
    def attack(self, value):
        self._attack = int(self.attack+(1.2*value))

    @property
    def defense(self):
        return self._defense

    @defense.setter
    def defense(self, value):
        self._defense = int(self.defense+(1.2*value))

    @property
    def gold(self):
        return self._gold

    @gold.setter
    def gold(self, value):
        self._gold = self.gold * (1 + value/100)

    def mob_msg(self):
        self.msg = "Um %s apareceu..." % self.name
        return self.msg

    def __repr__(self) -> str:
        return "Um %s apareceu..." % (self.name)

class Cachorro:

    def __init__(self, level=2, life=8, mana=2, attack=5, defense=3, gold=5, image='', pos={'x':0, 'y':0}):

        self._randattr = randint(level - 1, level + 3)
        self.name = 'Cachorro Louco'
        self._level = level
        self._life = life
        self._mana = mana
        self._attack = attack
        self._defense = defense
        self._gold = gold
        self._exp = 10
        self._image = image

        self.level = self._randattr
        self.life = self._randattr
        self.mana = self._randattr
        self.attack = self._randattr
        self.defense = self._randattr
        self.gold = self._randattr
        self.exp = self._randattr

        @property
        def exp(self):
            return self._exp

        @exp.setter
        def exp(self, value):
            self._exp = int(self.exp + (1.2 * value))

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = self.level+(value-self.level)

    @property
    def life(self):
        return self._life

    @life.setter
    def life(self, value):
        self._life = int(self.life+(1.2*value))

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, value):
        self._mana = int(self.mana+(1.2*value))

    @property
    def attack(self):
        return self._attack

    @attack.setter
    def attack(self, value):
        self._attack = int(self.attack+(1.2*value))

    @property
    def defense(self):
        return self._defense

    @defense.setter
    def defense(self, value):
        self._defense = int(self.defense+(1.2*value))

    @property
    def gold(self):
        return self._gold

    @gold.setter
    def gold(self, value):
        self._gold = self.gold * (1 + value/100)

    def __repr__(self) -> str:
        return "Um %s apareceu..." % (self.name)

class Elpy:

    def __init__(self, level=2, life=7, mana=3, attack=4, defense=2, gold=6, image='', pos={'x':0, 'y':0}):

        self._randattr = randint(level - 1, level + 3)
        self.name = 'Elpy'
        self._level = level
        self._life = life
        self._mana = mana
        self._attack = attack
        self._defense = defense
        self._gold = gold
        self._image = image

        self.level = self._randattr
        self.life = self._randattr
        self.mana = self._randattr
        self.attack = self._randattr
        self.defense = self._randattr
        self.gold = self._randattr

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = self.level+(value-self.level)

    @property
    def life(self):
        return self._life

    @life.setter
    def life(self, value):
        self._life = int(self.life+(1.2*value))

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, value):
        self._mana = int(self.mana+(1.2*value))

    @property
    def attack(self):
        return self._attack

    @attack.setter
    def attack(self, value):
        self._attack = int(self.attack+(1.2*value))

    @property
    def defense(self):
        return self._defense

    @defense.setter
    def defense(self, value):
        self._defense = int(self.defense+(1.2*value))

    @property
    def gold(self):
        return self._gold

    @gold.setter
    def gold(self, value):
        self._gold = self.gold * (1 + value/100)

    def __repr__(self) -> str:
        return "Um %s apareceu..." % (self.name)

# Mobs lvl 4
# Mobs lvl 8
# Mobs lvl 12
# Mobs lvl 16
# Mobs lvl 20
# Mobs lvl 22
# Mobs lvl 24
# Mobs lvl 26
# Mobs lvl 30
if __name__ == '__main__':
    goblin = Cachorro()
    print(goblin)
