"""
Class Helena - 08/11/2018

Classe Helena representa a heroina da jogo que pode desenvolver suas habilidades ao longo do jogo

o step de level aumenta em 30% toda vez q os pontos de experiencia aumentam até o step um lvl é incrementado
o level 2 é atingido aos 30 xp e os demais em int(1,3* ultimo nivel de exp)
lvl 3 = 39 xp ganhos
lvl 4 = 51
lvl 5 = 66
lvl 6 = 86
lvl 7 = 112
lvl 8 = 146
"""

class Helena:

    experiencia = 0

    def __init__(self):
        self._level = 1
        self._hp = 15
        self._mp = 20
        self._attack = 7
        self._defense = 6
        self._exp = 0
        self._gold = 0
        self._inventory = []
        self._grimoars = []
        self._image = ''

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level += value
        self.check_level() # incrementa todos os atributos do personagem

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp += value

    @property
    def mp(self):
        return self._mp

    @mp.setter
    def mp(self, value):
        self._mp += value

    @property
    def attack(self):
        return self._attack

    @attack.setter
    def attack(self, value):
        self._attack += (1+value//self.level)//self.level

    @property
    def defense(self):
        return self._defense

    @defense.setter
    def defense(self, value):
        self._defense += (1+value//self.level)//self.level

    @property
    def grimoars(self):
        return self._grimoars

    @grimoars.setter
    def grimoars(self, value):
        self._grimoars.append(value)

    @property
    def inventory(self):
        return self._inventory

    @inventory.setter
    def inventory(self, value):
        self._inventory.append(value)

    @property
    def gold(self):
        return self._gold

    @gold.setter
    def gold(self, value):
        self._gold += value

    @property
    def exp(self):
        return self._exp

    @exp.setter
    def exp(self, value):
        if value > 0:
            self._exp += value
        else:
            self._exp = value

    def atacar(self, skill=""):
        atq = ""
        if skill == 'wind_strike':
            atq = self.wind_strike()
        elif skill == 'ataque_direto':
            atq = self.ataque_direto()
        return atq

    def defender(self):
        pass

    def ataque_direto(self):
        def power():
            if self.level < 8:
                return 3
            elif 8 <= self.level < 12:
                return 6
            elif 12 <= self.level < 16:
                return 9
            else:
                return 15

        def use():
            ataque = self.attack + power()
            return 'Helena usou Ataque Direto!', ataque

        atq = use()
        return 'Helena usou Ataque strike!', atq

    def wind_strike(self):

        def power():
            if self.level < 8:
                return 5
            elif 8<= self.level < 12:
                return 9
            elif 12<= self.level < 16:
                return 13

        def use():
            ataque = self.attack + power()
            return ataque

        def knowledge(self):
            if self.level == 4:
                return "Helena aprendeu Wind Strike!"

        if self.level >= 4:
            atq = use()
            return 'Helena usou wind strike!', atq
        else:
            return "Helena é incapaz de usar Wind Strike!"

    def acqua_wave(self):
        def power():
            if self.level < 8:
                return 5
            elif 8<= self.level < 12:
                return 9
            elif 12<= self.level < 16:
                return 13

        def use():
            ataque = self.attack + power()
            return ataque

        def knoledge(self):
            return "Helena aprendeu Acqua Wave!"

        if self.level >= 4:
            print('Helena usou wind strike!')
            atq = use()
            return atq
        else:
            return "Helena é incapaz de usar Wind Strike!"

    def auto_heal(self):
        def power():
            if self.level < 8:
                return 5
            elif 8<= self.level < 12:
                return 9
            elif 12<= self.level < 16:
                return 13

        def use():
            ataque = self.attack + power()
            return ataque

        def knoledge(self):
            return "Helena aprendeu Auto Heal!"

        if self.level >= 4:
            print('Helena usou wind strike!')
            atq = use()
            return atq
        else:
            return "Helena é incapaz de usar Wind Strike!"

    def fire_ball(self):
        def power():
            if self.level < 8:
                return 5
            elif 8 <= self.level < 12:
                return 9
            elif 12 <= self.level < 16:
                return 13

        def use():
            ataque = self.attack + power()
            return ataque

        def knoledge(self):
            return "Helena aprendeu Fire Ball!"

        if self.level >= 4:
            print('Helena usou wind strike!')
            atq = use()
            return atq
        else:
            return "Helena é incapaz de usar Wind Strike!"

    def check_level(self):
        self.hp = int(self.hp * 1.15)
        self.mp = int(self.mp * 1.15)
        self.attack = int(self.attack * 1.15)
        self.defense = int(self.defense * 1.15)

    def islevel_increase(self):

        if self.exp > int(1.3 * self.experiencia):
            return True
        else:
            return False

    def level_increase(self):
        if self.islevel_increase():
            self.experiencia += int(1.3*(self.exp-self.experiencia))
            self.level = 1
            self.exp = 0
            return "Helena ganhou um nivel!"

    def trocar_grimoar(self):
        pass

    def __repr__(self):
        return "Eu sou a Princesa Helena do Reino de Ikathyah!"



if __name__ == '__main__':
    helena = Helena()
    helena.exp = 30
    helena.level_increase()
    helena.exp = 30
    helena.level_increase()
    helena.exp = 30
    helena.level_increase()
    helena.exp = 30
    helena.level_increase()
    helena.exp = 30
    helena.level_increase()
    helena.exp = 30
    helena.level_increase()
    helena.exp = 30
    helena.level_increase()
    helena.exp = 60
    helena.level_increase()
    helena.exp = 90
    helena.level_increase()
    helena.atacar('wind_strike')
