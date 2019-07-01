import lib.stellagama as game

class world:
	"""character generation class"""
	def __init__ (self):
		"""generate basic stats"""
		self.starport = game.random_choice(['X', 'E', 'E', 'E', 'E', 'E', 'E', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A','A'])

		self.size = game.dice(2, 6) - 2
		self.atmosphere = self.atmosphere_calc( self.size )
		self.hydrographics = self.hydrographics_calc( self.size, self.atmosphere )
		self.population = game.dice(2, 6) - 2
		self.government = self.government_calc( self.population )
		self.lawlevel = self.law_level_calc( self.government, self.population )
		self.techlevel = self.techlevel_calc(self.population, self.starport, self.size, self.atmosphere, self.hydrographics, self.government)
		self.upp = [self.size, self.atmosphere, self.hydrographics, self.population, self.government, self.lawlevel, self.techlevel ]
		self.tradelevel = self.trade_classification(self.size, self.atmosphere, self.hydrographics, self.population, self.government, self.lawlevel, self.techlevel)
	def atmosphere_calc(self, size):
		atmo_base = game.dice(2, 6) - 7 + size

		if atmo_base <= 0:
			return 0
		elif atmo_base >= 15:
			return 15
		else:
			return atmo_base

	def hydrographics_calc(self, size, atmosphere):
		hydro_base = game.dice(2, 6) - 7
		if size <= 1:
			return 0
		else:
			if atmosphere <= 1:
				hydro_base += -4
			elif atmosphere >= 10 and atmosphere <= 12:
				hydro_base += -4

			hydro_base += size

			if hydro_base <= 0:
				return 0
			elif hydro_base >= 15:
				return 15
			else:
				return hydro_base

	def government_calc(self, population):
		gov_base = game.dice(2, 6) - 7

		if population <= 0:
			return 0
		else:
			gov_base += population
			if gov_base <= 0:
				return 0
			elif gov_base >= 15:
				return 15
			else:
				return gov_base

	def law_level_calc(self, government, population):
		law_base = game.dice(2, 6) - 7

		if population < 1:
			return 0
		else:
			law_base += government

			if law_base <= 0:
				return 0
			elif law_base >= 15:
				return 15
			else:
				return law_base

	def techlevel_calc(self, population, starport, size, atmosphere, hydrographics, government):
		tech_base = game.dice(1, 6)

		if population <= 0:
			return 0
		else:
			if starport =='X':
				tech_base += -6
			elif starport =='C':
				tech_base += 2
			elif starport =='B':
				tech_base += 4
			elif starport =='A':
				tech_base += 6

			if size in [1,2]:
				tech_base += 2
			elif size in [2,3,4]:
				tech_base += 1

			if atmosphere in [0,1,2,3,10,11,12,13,14,15]:
				tech_base += 1

			if hydrographics in [0,9]:
				tech_base += 1
			elif hydrographics == 10:
				tech_base += 2

			if population in [0,1,2,3,4,5,9]:
				tech_base += 1
			elif population == 10:
				tech_base += 2
			elif population == 11:
				tech_base += 3
			elif population == 12:
				tech_base += 4

			if government in [0,5]:
				tech_base += 1
			elif government == 7:
				tech_base += 2
			elif government in [13,14]:
				tech_base += -2

			if tech_base <= 0:
				return 0
			elif tech_base >= 15:
				return 15
			else:
				return tech_base

	def trade_classification ( self, size, atmosphere,hydrographics, population, government, lawlevel, techlevel ):
		trade_list =[]

		if atmosphere in [4,5,6,7,8,9] and hydrographics in [4,5,6,7,8] and population in [4,5,6,7]:
			trade_list.extend(['Ag'])
		if size == 0 and atmosphere == 0 and hydrographics == 0:
			trade_list.extend(['As'])
		if population == 0 and government == 0 and lawlevel == 0:
			trade_list.extend(['Ba'])
		if atmosphere >= 2 and hydrographics == 0:
			trade_list.extend(['De'])
		if atmosphere >= 10 and hydrographics >= 1:
			trade_list.extend(['Fl'])
		if atmosphere >= 5 and hydrographics in [4,5,6,7,8,9] and population in [4,5,6,7,8]:
			trade_list.extend(['Ga'])
		if population >= 9:
			trade_list.extend(['Hi'])
		if techlevel >= 12:
			trade_list.extend(['Ht'])
		if atmosphere in [0,1] and hydrographics >= 1:
			trade_list.extend(['Ic'])
		if atmosphere in [0,1,2,4,7,9] and population >= 9:
			trade_list.extend(['In'])
		if population in [1,2,3]:
			trade_list.extend(['Lo'])
		if techlevel <= 5:
			trade_list.extend(['Lt'])
		if atmosphere in [0,1,2,3] and hydrographics in [0,1,2,3] and population >= 6:
			trade_list.extend(['Na'])
		if population in [4,5,6]:
			trade_list.extend(['Ni'])
		if atmosphere in [2,3,3,4,5] and hydrographics in [0,1,2,3]:
			trade_list.extend(['Po'])
		if atmosphere in[6,8] and population in [6,7,8]:
			trade_list.extend(['Ri'])
		if hydrographics == 10:
			trade_list.extend(['Wa'])
		if atmosphere == 0:
			trade_list.extend(['Va'])

		return trade_list

# Space Opera World Creation
# When generating a mainworld for a space opera setting, generate Size and Atmosphere as normal then consult the following if Size is 4 or less:
# If Size is 0-2, Atmosphere is set to 0. The world is too small to retain an atmosphere.
# If Size is 3-4 and Atmopshere is 0-2, set Atmosphere to 0.
# If Size is 3-4 and Atmosphere is 3-5, set Atmosphere to 1.
# If Size is 3-4 and Atmopshere is 6+, set Atmosphere to A.
# Hydrographics is also affected. Apply the following DMs to rolls on the Hydrographics Table:
# If Size is 3-4 and Atmosphere is A the DM is -6.
# If Atmosphere is 0-1 the DM is -6.
# If Atmosphere is 2-3, B or C the DM is -4.
# Hard Science World Creation
# Hard science worlds use the space opera modifiers above, plus additional Dice Modifi ers to Population based on the Size and Atmosphere as follows:
# If Size is 0-2 (low gravity world) then the DM is -1.
# If Size is A (high gravity world) then the DM is -1.
# If Atmosphere is not 5, 6 or 8 then the DM is -1.
# If Atmosphere is 5, 6 or 8 then the DM is +1.
# In addition, the population of a world has an affect on the class of the local starport. Instead of rolling 2d6 on the Starport Table, roll 2d6-7 and add the Population value.