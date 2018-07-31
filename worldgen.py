import stellagama as game

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
			
			if size == 0 or size == 1:
				tech_base += 2
			elif size >= 2 and size <= 4:
				tech_base += 1
			
			if atmosphere <= 3 or atmosphere >= 10:
				tech_base += 1

			if hydrographics == 0 or hydrographics == 9:
				tech_base += 1
			elif hydrographics == 10:
				tech_base += 2
			
			if population <= 5 or  population == 9:
				tech_base += 1
			elif population == 10:
				tech_base += 2
			elif population == 11:
				tech_base += 3
			elif population == 12:
				tech_base += 4
			
			if government == 0 or government == 5:
				tech_base += 1
			elif government == 7:
				tech_base += 2
			elif government == 13 or government == 14:
				tech_base += -2

			if tech_base <= 0:
				return 0
			elif tech_base >= 15:
				return 15
			else:
				return tech_base
