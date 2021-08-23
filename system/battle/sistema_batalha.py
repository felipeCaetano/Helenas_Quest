from random import randint


def ismobdied(mob):
	if mob.life <= 0:
		return True
	else:
		return False


def calcula_dano(ataque, mob):
	dano = 1.2 * (ataque - mob.defense)
	if dano > 0:  # causou dano!
		mob.life -= dano
		if ismobdied(mob):
			return dano, 1, mob.exp, mob.gold  # dano, derrotado, xp, gold
		else:
			return dano, 0, None, None
	else:  # não causou dano
		return -1, 0, None, None


class Battle:
	"""
	Class Battle é a batalha entre o player e o mob
	"""

	def __init__(self, jogador, mob):
		self.turn = True
		self.jogador = jogador
		self.mob = mob

	def round(self):
		if self.turn:
			skill_selected = self.select_skill(self.jogador)
			result = self.jogador.atacar(skill_selected)
			msg = calcula_dano(result[1], self.mob)

	def select_skill(self, skill):
		skill_name, action = skill
		if action == 40:
			self.jogador.atacar(skill_name)
		elif action == 41:
			pass
		elif action == 42:
			pass
		elif action == 43:
			pass

	def select_action(self, action):
		if action == 30:
			return 35  # show grimoar choose
		elif action == 31:
			return 45
		elif action == 32:
			pass
		elif action == 33:
			pass
