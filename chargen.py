"""
chargen.py
Classic Traveller character generator
v0.9, March 6th, 2019
By Omer Golan-Joel, golan2072@gmail.com
By Jason McAlpin, golmspace@gmail.com
This code is open-source
"""

# import modules
import lib.stellagama as game
import sys, argparse, re, time, random
from string import Template
from lib.worldgen import world
from lib.hyphenate import hyphenate_word
from lib.wordplay import create_word
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
# command line control system





#classes

class Character:
	"""character generation class"""
	def __init__ (self, args={}):
		start_seed = time.time()
		random.seed(start_seed)
		"""generate basic stats"""
		self.upp = [game.dice(2, 6), game.dice(2, 6), game.dice(2, 6), game.dice(2, 6), game.dice(2, 6), game.dice(2, 6)]
		self.skills = {}
		self.possessions = {}
		self.rank = 0
		self.race = game.random_choice(self.Races)
		self.birth_world = world()
		self.birth_upp = self.birth_world.upp
		self.birth_starport = self.birth_world.starport
		self.discharge_world = world()
		self.discharge_starport = self.discharge_world.starport
		self.discharge_upp = self.discharge_world.upp
		self.psionic_trained = "no"
		self.psionic_rating = game.dice(2, 6)
		self.psionic_talents = {}
		self.tas_member = ""
		self.terms = 0
		self.cash = 0
		self.title = ""
		self.status = ""
		self.sex = game.random_choice(["male", "female"])

		

		self.birth_world_name =     self.phonetic_gen(args)
		self.discharge_world_name = self.phonetic_gen(args)
		self.name =                 self.phonetic_gen(args)
		self.surname =              self.phonetic_gen(args)
		self.career =               self.career_choice(self.upp)
		self.age = 18

		# Test for world values use with -t world
		self.birth_size =          self.birth_world.size,
		self.birth_atmosphere =    self.birth_world.atmosphere,
		self.birth_hydrographics = self.birth_world.hydrographics,
		self.birth_population =    self.birth_world.population,
		self.birth_government =    self.birth_world.government,
		self.birth_lawlevel =      self.birth_world.lawlevel,
		self.birth_techlevel =     self.birth_world.techlevel,
		self.birth_tradelevel =    self.birth_world.tradelevel
		"""enlistment"""
		enlistment=game.dice(2,6)
		if self.upp[self.career["enlistment DM+1"]]>=self.career["enlistment DM+1 level"]:
			enlistment+=1
		if self.upp[self.career["enlistment DM+2"]]>=self.career["enlistment DM+2 level"]:
			enlistment+=2
		if enlistment>= self.career["enlistment"]:
			self.career=self.career
		else:
			self.career=game.random_choice([self.Navy, self.Marines, self.Army, self.Merchants, self.Scouts, self.Other])
		"""career generation loop"""
		in_career=True
		while in_career == True:
			if self.terms==0:
					if 0 in self.career["rank skills"]:
						self.add_skill(self.skills, self.career["rank skills"][0])
			survival=game.dice(2,6)
			if self.upp[self.career["survival DM+1"]]>=self.career["survival DM+1 level"]:
				survival+=1
			if survival>=self.career["survival"]:
				in_career=True
				self.terms+=1
				self.age+=4
			else:
				self.status="DECEASED"
				in_career=False
				break
			"""skill generation"""
			if self.career in [self.Scouts, self.Other]:
				for i in range (0,2):
					skill_table=game.random_choice(["personal", "service", "advanced", "advanced 2"])
					self.add_skill(self.skills, game.random_choice(self.career[skill_table]))
			else:
				if self.terms==1:
					for i in range (0,2):
						skill_table=game.random_choice(["personal", "service", "advanced", "advanced 2"])
						self.add_skill(self.skills, game.random_choice(self.career[skill_table]))
				else:
					skill_table=game.random_choice(["personal", "service", "advanced", "advanced 2"])
					self.add_skill(self.skills, game.random_choice(self.career[skill_table]))
			"""commission and promotion"""
			if self.career in [self.Scouts, self.Other]:
				self.rank=0
			elif self.rank==0:
				commission=game.dice(2,6)
				if self.upp[self.career["commission DM+1"]]>=self.career["commission DM+1 level"]:
					commission+=1
				if commission>=self.career["commission"]:
					self.rank+=1
					skill_table=game.random_choice(["personal", "service", "advanced", "advanced 2"])
					self.add_skill(self.skills, game.random_choice(self.career[skill_table]))
					if self.rank in self.career["rank skills"]:
						self.add_skill(self.skills, self.career["rank skills"][self.rank])
				else:
					self.rank=self.rank
			if self.rank>0 and self.rank<6:
				promotion=game.dice(2,6)
				if self.upp[self.career["promotion DM+1"]]>=self.career["promotion DM+1 level"]:
					promotion+=1
				if promotion>=self.career["promotion"]:
					self.rank+=1
					skill_table=game.random_choice(["personal", "service", "advanced", "advanced 2"])
					self.add_skill(self.skills, game.random_choice(self.career[skill_table]))
					if self.rank in self.career["rank skills"]:
						self.add_skill(self.skills, self.career["rank skills"][self.rank])
				else:
					self.rank=self.rank
			"""reenlistment"""
			reenlistment=game.dice(2,6)
			if self.terms<7 and reenlistment>= self.career["reenlist"]:
				in_career=True
			elif self.terms>=7 and reenlistment==12:
				in_career=True
			else:
				in_career=False
		"""mustering out"""
		if self.status=="DECEASED":
			self.possessions={}
			self.add_possession(self.possessions, "Grave marker")
		else:
			muster_throws=self.terms
			if self.rank in [1,2]:
				muster_throws+=1
			elif self.rank in [3,4]:
				muster_throws+=2
			elif self.rank in [5,6]:
				muster_throws+=3
			for i in range (0, muster_throws):
				muster_table=game.random_choice(["muster", "cash"])
				muster_roll=game.dice(1, 6)-1
				if muster_table=="muster" and self.rank>=5:
					muster_roll+=1
				if muster_table=="cash" and "Gambling" in self.skills:
					muster_roll+=1
				if muster_table=="muster":
					self.add_possession(self.possessions, self.career["muster"][muster_roll])
				elif muster_table=="cash":
					self.cash+=self.career["cash"][muster_roll]

			if (self.psionic_rating - self.terms) >= 1:
				if self.cash >= 100000:
					if game.dice(2, 6) >= 7:
						self.cash -= 100000
						self.psionic_trained = "yes"
						self.psionic_talents = self.add_psionic_talent(self.psionic_rating, self.terms)
		"""characteristic modifications"""
		for k in list(self.skills.keys()):
			if k == "+1 STR":
				self.upp[0]+=1
				del self.skills[k]
			elif k == "+1 DEX":
				self.upp[1]+=1
				del self.skills[k]
			elif k == "+1 END":
				self.upp[2]+=1
				del self.skills[k]
			elif k == "+1 INT":
				self.upp[3]+=1
				del self.skills[k]
			elif k == "+1 EDU":
				self.upp[4]+=1
				del self.skills[k]
			elif k == "+2 EDU":
				self.upp[4]+=2
				del self.skills[k]
			elif k == "+1 SOC":
				self.upp[5]+=1
				del self.skills[k]
			elif k == "+2 SOC":
				self.upp[5]+=2
				del self.skills[k]
			elif k == "-1 SOC":
				self.upp[5]-=1
		for k in list(self.possessions.keys()):
			if k == "+1 STR":
				self.upp[0]+=1
				del self.possessions[k]
			elif k == "+1 DEX":
				self.upp[1]+=1
				del self.possessions[k]
			elif k == "+1 END":
				self.upp[2]+=1
				del self.possessions[k]
			elif k == "+1 INT":
				self.upp[3]+=1
				del self.possessions[k]
			elif k == "+1 EDU":
				self.upp[4]+=1
				del self.possessions[k]
			elif k == "+2 EDU":
				self.upp[4]+=2
				del self.possessions[k]
			elif k == "+1 SOC":
				self.upp[5]+=1
				del self.possessions[k]
			elif k == "+2 SOC":
				self.upp[5]+=2
				del self.possessions[k]
		"""titles"""
		if self.upp[5]==11:
			if self.sex=="male":
				self.title="Sir"
			elif self.sex=="female":
				self.title="Lady"
		elif self.upp[5]==12:
			if self.sex=="male":
				self.title="Baron"
			elif self.sex=="female":
				self.title="Baroness"
		elif self.upp[5]==13:
			if self.sex=="male":
				self.title="Marquis"
			elif self.sex=="female":
				self.title="Marquesa"
		elif self.upp[5]==14:
			if self.sex=="male":
				self.title="Count"
			elif self.sex=="female":
				self.tatile="Contessa"
		elif self.upp[5]==15:
			if self.sex=="male":
				self.title="Duke"
			elif self.sex=="female":
				self.title="Duchess"
		elif self.rank>=5:
			self.title=self.career["ranks"][self.rank]
		else:
			if self.sex=="male":
				self.title="Mr."
			elif self.sex=="female":
				self.title=game.random_choice(["Ms.", "Mrs."])
		if self.upp[4]>=12:
			self.title="Dr." #you get PhD at EDU 12+!
		if "Medical" in self.skills:
			if self.skills["Medical"]>=3:
				self.title="Dr."

	def add_possession(self, possessions, item): #inputs the possession dictionary and item
		"""
		adds a skill or characteristic bonus to a character
		"""
		if item=="":
			return possessions
		if item=="Blade":
			item=game.random_choice(self.melee)
		if item=="Gun":
			item=game.random_choice(self.guns)
		if item in possessions:
			possessions[item] += 1
		elif item not in possessions:
			possessions[item] = 1
		return possessions #outputs the skill dictionary

	

	def skill_stringer(self, input_dict): #input a dictionary
		"""
		converts a dictionary to a string, Traveller skill format
		"""
		return ', '.join('-'.join((k, str(v))) for k,v in sorted(input_dict.items())) #output formatted skill list string

	def array_stringer(self, input_dict): #input a dictionary
		"""
		converts a dictionary to a string, Traveller psionic list format
		"""
		return ', '.join(input_dict) #output formatted psionic talent list string

	def possession_stringer(self, input_dict):
		"""
		converts a dictionary to a string, Traveller possessions format
		"""
		return ', '.join(' x'.join((k, str(v))) for k,v in sorted(input_dict.items())) #output formatted skill list string

	def upp_stringer(self, input_list): #input a characteristics list
		"""
		converts a characteristics list to a UPP string
		"""
		output_list=[]
		for item in input_list:
			output_list.append(str(game.pseudo_hex(item)))
		return ''.join (output_list) #output a string

	def add_psionic_talent(self, psi_rating, terms):
		talent_list = ['Telepathy', 'Clairvoyance', 'Telekinesis', 'Awareness', 'Teleportation']

		psionic_training_attempts = 0

		talent_learned =[]

		while 0 < len(talent_list):
			telepathy_chance     = 4 + psi_rating - psionic_training_attempts - terms
			clairvoyance_chance  = 3 + psi_rating - psionic_training_attempts - terms
			telekinesis_chance   = 2 + psi_rating - psionic_training_attempts - terms
			awareness_chance     = 1 + psi_rating - psionic_training_attempts - terms
			teleportation_chance = 0 + psi_rating - psionic_training_attempts - terms

			psi_talent_training = game.random_choice(talent_list)

			if psi_talent_training == 'Telepathy':
				if telepathy_chance > 1:
					if game.dice(2,6) <= telepathy_chance:
						talent_list.remove('Telepathy')
						talent_learned.extend(['Telepathy'])
						psionic_training_attempts += 1
					else:
						psionic_training_attempts += 1
				else:
					talent_list.remove('Telepathy')

			if psi_talent_training == 'Clairvoyance':
				if clairvoyance_chance > 1:
					if game.dice(2,6) <= clairvoyance_chance:
						talent_list.remove('Clairvoyance')
						talent_learned.extend(['Clairvoyance'])
						psionic_training_attempts += 1
					else:
						psionic_training_attempts += 1
				else:
					talent_list.remove('Clairvoyance')

			if psi_talent_training == 'Telekinesis':
				if telekinesis_chance > 1:
					if game.dice(2,6) <= telekinesis_chance:
						talent_list.remove('Telekinesis')
						talent_learned.extend(['Telekinesis'])
						psionic_training_attempts += 1
					else:
						psionic_training_attempts += 1
				else:
					talent_list.remove('Telekinesis')

			if psi_talent_training == 'Awareness':
				if awareness_chance > 1:
					if game.dice(2,6) <= awareness_chance:
						talent_list.remove('Awareness')
						talent_learned.extend(['Awareness'])
						psionic_training_attempts += 1
					else:
						psionic_training_attempts += 1
				else:
					talent_list.remove('Awareness')

			if psi_talent_training == 'Teleportation':
				if teleportation_chance > 1:
					if game.dice(2,6) <= teleportation_chance:
						talent_list.remove('Teleportation')
						talent_learned.extend(['Teleportation'])
						psionic_training_attempts += 1
					else:
						psionic_training_attempts += 1
				else:
					talent_list.remove('Teleportation')

		return talent_learned
	def career_choice (self, upp): #input upp list
		"""
		chooses a career based on UPP characteristics.
		"""
		if upp[4]==max(upp):
			career=self.Navy
		elif upp[0]==max(upp):
			career=game.random_choice([self.Scouts, self.Marines])
		elif upp[2]==max(upp):
			career=self.Army
		elif upp[3]==max(upp):
			career=self.Merchants
		else:
			career=self.Other
		return career #outputs the chatacter's career


	def add_skill(self, skill_list, skill): #inputs the skill dictionary and skill
		"""
		adds a skill or characteristic bonus to a character
		"""
		if skill=="":
			return skill_list
		if skill=="Gun Combat":
			if game.dice(1,6)>=3:
				for item in self.guns:
					if item in skill_list:
						skill=item
					else:
						skill=game.random_choice(self.guns)
			else:
				skill=game.random_choice(self.guns)
		elif skill in ["Blade Combat", "Blade Cbt"]:
			if game.dice(1,6)>=3:
				for item in self.melee:
					if item in skill_list:
						skill=item
					else:
						skill=game.random_choice(self.melee)
			else:
				skill=game.random_choice(self.melee)
		elif skill=="Vehicle":
			if game.dice(1,6)>=3:
				for item in self.vehicles:
					if item in skill_list:
						skill=item
				else:
					skill=game.random_choice(self.vehicles)
			else:
				skill=game.random_choice(self.vehicles)
		if skill in skill_list:
			skill_list[skill] += 1
		elif skill not in skill_list:
			skill_list[skill] = 1
		return skill_list #outputs the skill dictionary

	def word_gen_new(self, args): #input character sex
		"""
		randomly create a word from language rules
		"""
		name = create_word(args)
		return name.capitalize()


	def phonetic_gen(self, args): #input character sex
		"""
		randomly create a syllable from a random list of syllables
		"""
		phonetic_onset = "names/phonetic_english_onset.txt"
		phonetic_nucleus = "names/phonetic_english_nucleus.txt"
		phonetic_coda = "names/phonetic_english_coda.txt"
		phonetic_structure = game.random_line("names/phonetic_english_structure.txt")
		structure_length = len(phonetic_structure)

		

		name=""
		
		for syllable in phonetic_structure:
			if syllable == "o":
				name += game.random_line(phonetic_onset)
			elif syllable == "n":
				name += game.random_line(phonetic_nucleus)
			else:
				name += game.random_line(phonetic_coda)
			

		return name.capitalize()

	def word_gen(self, args): #input character sex
		"""
		randomly create a syllable from a random list of syllables
		"""
		name_source = name=""
		name_source =  game.random_choice([
			"names/englishsyllables.txt",
			# "names/mericansyllables.txt",
			# "names/evilsyllables.txt",
			# "names/frenchsyllables.txt",
			# "names/irishsyllables.txt",
			# "names/italiansyllables.txt",
			# "names/latinwords.txt",
			# "names/spanishsyllables.txt",
		])
		
		syllable_length =  [1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,4,4,4]
		num_syl = game.random_choice(syllable_length)
		while num_syl > 0:
			name += game.random_line(name_source)
			num_syl -= 1
		return name.capitalize()

	Races=[
		"Aslan",
		"Droyne",
		"Hiver",
		"Humaniti",
		"K'kree",
		"Vargr",
		"Solomani",
		"Vilani",
		"Zhodani",
		"Imperial",
		"Darrian",
		"Geonee",
		"Suerrat"
	]
	guns=[
		"Body Pistol",
		"Autopistol",
		"Revolver",
		"Carbine",
		"Rifle",
		"Autorifle",
		"Shotgun",
		"SMG",
		"Laser Carbine",
		"Laser Rifle"
	]
	melee=[
		"Blade",
		"Foil",
		"Cutlass",
		"Sword",
		"Broadsword",
		"Bayonet",
		"Spear",
		"Halberd",
		"Pike",
		"Cudgel"
	]
	vehicles=[
		"Aircraft (Helicopter)",
		"Aircraft (Propeller-driven)",
		"Aircraft (Jet-driven)" "Grav Vehicle",
		"Tracked Vehicle",
		"Wheeled Vehicle",
		"Watercraft (Small Watercraft)",
		"Watercraft (Large Watercraft)",
		"Watercraft (Hovercraft)",
		"Watercraft (Submerisible)"
	]

	Navy={
		"name": "Navy",
		"enlistment": 8,
		"enlistment DM+1": 3,
		"enlistment DM+1 level": 8,
		"enlistment DM+2": 4,
		"enlistment DM+2 level": 9,
		"survival": 5,
		"survival DM+1": 3,
		"survival DM+1 level": 7,
		"commission": 10,
		"commission DM+1": 5,
		"commission DM+1 level": 9,
		"promotion": 8,
		"promotion DM+1": 4,
		"promotion DM+1 level": 8,
		"reenlist": 6,
		"ranks": [
			"Starman",
			"Ensign",
			"Lieutenant",
			"Lt Commander",
			"Commander",
			"Captain",
			"Admiral"
		], 
		"muster": [
			"Low Passage",
			"+1 INT",
			"+2 EDU",
			"Blade",
			"TAS",
			"High Passage",
			"+2 SOC"
		], 
		"cash": [
			1000,
			5000,
			5000,
			10000,
			20000,
			50000,
			50000
		],
		"personal": [
			"+1 STR",
			"+1 DEX",
			"+1 END",
			"+1 INT",
			"+1 EDU",
			"+1 SOC"
		], 
		"service": [
			"Ship's Boat",
			"Vacc Suit",
			"Forward Obs",
			"Gunnery",
			"Blade Combat",
			"Gun Combat"
		], 
		"advanced": [
			"Vacc Suit",
			"Mechanical",
			"Electronics",
			"Engineering",
			"Gunnery",
			"J-o-T"
		], 
		"advanced 2": [
			"Medical",
			"Navigation",
			"Engineering",
			 "Computer",
			 "Pilot",
			 "Admin"
		 ], 
		 "rank skills": {
			 5:"+1 Soc", 
			 6: "+1 SOC"
		 }
	}

	Marines={
		"name": "Marines",
		"enlistment": 9,
		"enlistment DM+1": 3,
		"enlistment DM+1 level": 8,
		"enlistment DM+2": 0,
		"enlistment DM+2 level": 8,
		"survival": 6,
		"survival DM+1": 2,
		"survival DM+1 level": 8,
		"commission": 9,
		"commission DM+1": 4,
		"commission DM+1 level": 7,
		"promotion": 9,
		"promotion DM+1": 5,
		"promotion DM+1 level": 8,
		"reenlist": 6,
		"ranks": [
			"Trooper",
			"Lieutenant",
			"Captain",
			"Force Cmdr",
			"Lt Colonel",
			"Colonel",
			"Brigadier"
		],
		"muster": [
			"Low Passage",
			"+2 INT",
			"+1 EDU",
			"Blade",
			"TAS",
			"High Passage",
			"+2 SOC"
		],
		"cash": [
			1000,
			5000,
			5000,
			10000,
			20000,
			30000,
			40000
		],
		"personal": [
			"+1 STR",
			"+1 DEX",
			"+1 END",
			"Gambling",
			"Brawling",
			"Blade Cbt"
		],
		"service": [
			"ATV",
			"Mechanical",
			"Electronic",
			"Tactics",
			"Blade Cbt",
			"Gun Combat"
		],
		"advanced": [
			"Vehicle",
			"Mechanical",
			"Electronic",
			"Tactics",
			"Blade Cbt",
			"Gun Combat"
		],
		"advanced 2": [
			"Medical",
			"Tactics",
			"Tactics",
			"Computer",
			"Leader",
			"Admin"
		],
		"rank skills":{
			0:"Cutlass",
			1:"Revolver"
		}
	}

	Army={
		"name": "Army",
		"enlistment": 5,
		"enlistment DM+1": 1,
		"enlistment DM+1 level": 6,
		"enlistment DM+2": 2,
		"enlistment DM+2 level": 5,
		"survival": 5,
		"survival DM+1": 4,
		"survival DM+1 level": 6,
		"commission": 5,
		"commission DM+1": 1,
		"commission DM+1 level": 7,
		"promotion": 6,
		"promotion DM+1": 4,
		"promotion DM+1 level": 7,
		"reenlist": 7,
		"ranks": [
			"Private",
			"Lieutenant",
			"Captain",
			"Major",
			"Lt. Colonel",
			"Colonel",
			"General"
		],
		"muster": [
			"Low Passage",
			"+1 INT",
			"+2 EDU",
			"Gun",
			"High Passage",
			"Mid Passage",
			"+1 SOC"
		],
		"cash": [
			2000,
			5000,
			10000,
			10000,
			10000,
			20000,
			30000
		],
		"personal": [
			"+1 STR",
			"+1 DEX",
			"+1 END",
			"Gambling",
			"+1 EDU",
			"Brawling"
		],
		"service": [
			"ATV",
			"Air/Raft",
			"Gun Combat",
			"Forward Obs",
			"Blade Combat",
			"Gun Combat"
		],
		"advanced": [
			"Vehicle",
			"Mechanical",
			"Electronics",
			"Tactics",
			"Blade Combat",
			"Gun Combat"
		],
		"advanced 2": [
			"Medical",
			"Tactics",
			"Tactics",
			"Computer",
			"Leader",
			"Admin"
		],
		"rank skills": {
			0:"Rifle",
			1: "SMG"
		}
	}

	Merchants={
		"name": "Merchants",
		"enlistment": 7,
		"enlistment DM+1": 0,
		"enlistment DM+1 level": 7,
		"enlistment DM+2": 3,
		"enlistment DM+2 level": 6,
		"survival": 5,
		"survival DM+1": 3,
		"survival DM+1 level": 7,
		"commission": 4,
		"commission DM+1": 3,
		"commission DM+1 level": 7,
		"promotion": 10,
		"promotion DM+1": 3,
		"promotion DM+1 level": 9,
		"reenlist": 4,
		"ranks": [
			"Spaceman",
			"4th Officer",
			"3rd Officer",
			"2nd Officer",
			"1st Officer",
			"Captain",
			""
		],
		"muster": [
			"Low Passage",
			"+1 INT",
			"+1 EDU",
			"Blade",
			"Low Passage",
			"High Passage",
			"Free Trader"
		],
		"cash": [
			1000,
			5000,
			10000,
			10000,
			10000,
			50000,
			100000
		],

		"personal": [
			"+1 STR",
			"+1 DEX",
			"+1 END",
			"+1 STR",
			"Blade Combat",
			"Bribery"
		],
		"service": [
			"Vehicle",
			"Vacc Suit",
			"J-o-T",
			"Steward",
			"Electronic",
			"Gun Combat"
		],
		"advanced": [
			"Streetwise",
			"Mechanical",
			"Electronic",
			"Navigation",
			"Gunnery",
			"Medical"
		],
		"advanced 2": [
			"Medical",
			"Navigation",
			"Engineering",
			"Computer",
			"Pilot",
			"Admin"
		],
		"rank skills": {
			1: "Pilot"
		}
	}

	Scouts={
		"name": "Scouts",
		"enlistment": 7,
		"enlistment DM+1": 3,
		"enlistment DM+1 level": 6,
		"enlistment DM+2": 0,
		"enlistment DM+2 level": 8,
		"survival": 7,
		"survival DM+1": 2,
		"survival DM+1 level": 9,
		"commission": 12,
		"commission DM+1": 5,
		"commission DM+1 level": 9,
		"promotion": 8,
		"promotion DM+1": 4,
		"promotion DM+1 level": 8,
		"reenlist": 3,
		"ranks": [
			"",
			"",
			"",
			"",
			"",
			"",
			""
		],
		"muster": [
			"Low Passage",
			"+2 INT",
			"+2 EDU",
			"Blade",
			"Gun",
			"Scout Ship",
			""
		],
		"cash": [
			20000,
			20000,
			30000,
			30000,
			50000,
			50000,
			50000
		],
		"personal": [
			"+1 STR",
			"+1 DEX",
			"+1 END",
			"+1 INT",
			"+1 EDU",
			"Gun Combat"
		],
		"service": [
			"Air/Raft",
			"Vacc Suit",
			"Mechanical",
			"Navigation",
			"Electronic",
			"J-o-T"
		],
		"advanced": [
			"Vehicle",
			"Mechanical",
			"Electronics",
			"J-o-T",
			"Gunnery",
			"Medical"
		],
		"advanced 2": [
			"Medical",
			"Navigation",
			"Engineering",
			"Computer",
			"Pilot",
			"J-o-T"
		],
		"rank skills": {
			0: "Pilot"
		}
	}

	Other={
		"name": "Other",
		"enlistment": 3,
		"enlistment DM+1": 3,
		"enlistment DM+1 level": 14,
		"enlistment DM+2": 4,
		"enlistment DM+2 level": 14,
		"survival": 5,
		"survival DM+1": 3,
		"survival DM+1 level": 9,
		"commission": 10,
		"commission DM+1": 5,
		"commission DM+1 level": 9,
		"promotion": 8,
		"promotion DM+1": 4,
		"promotion DM+1 level": 8,
		"reenlist": 5,
		"ranks": [
			"",
			"",
			"",
			"",
			"",
			"",
			""
		],
		"muster": [
			"Low Passage",
			"+1 INT",
			"+1 EDU",
			"Gun",
			"High Passage",
			"",
			""
		],
		"cash": [
			1000,
			5000,
			10000,
			10000,
			10000,
			50000,
			100000
		],
		"personal": [
			"+1 STR",
			"+1 DEX",
			"+1 END",
			"Blade Combat",
			"Brawling",
			"-1 SOC"
		],
		"service": [
			"Vehicle",
			"Gambling",
			"Brawling",
			"Bribery",
			"Blade Combat",
			"Gun Combat"
		],
		"advanced": [
			"Streetwise",
			"Mechanical",
			"Electronics",
			"Gambling",
			"Brawling",
			"Forgery"
		],
		"advanced 2": [
			"Medical",
			"Forgery",
			"Electronic",
			"Computer",
			"Streetwise",
			"J-o-T"
		],
		"rank skills": {
		}
	}

	def create_character(self, args):

		#main program

		#data basics
		number_of_runs = 1

		print_template    = 'templates'
		print_extension   = 'txt'
		file_name         = ''
		template_name     = print_template + '/text.template'


		if args.char:
			if args.char >= 1:
				number_of_runs = args.char


		if args.template:
			if args.template == 'markdown':
				print_extension = 'md'
				template_name = print_template + '/' + args.template + '.template'
			else:
				print_extension = 'txt'
				template_name = print_template + '/' + args.template + '.template'


		filein = open( template_name )
		character_sheet = Template( filein.read() )

		if args.file:
			file_name = args.file + '.' + print_extension

		if file_name:
			sys.stdout = open(file_name, "w")


		for x in range(number_of_runs):
			character1=Character(args)
			print (
				character_sheet.substitute(
					title = character1.title, 
					name = character1.name, 
					surname = character1.surname, 
					race = character1.race,
					sex = character1.sex,
					upp = character1.upp_stringer(character1.upp), 
					age = character1.age, 
					birth_world_name = character1.birth_world_name,
					birth_starport = character1.birth_starport,
					birth_upp = character1.upp_stringer(character1.birth_upp),
					discharge_world_name = character1.discharge_world_name,
					discharge_starport = character1.discharge_starport,
					discharge_upp = character1.upp_stringer(character1.discharge_upp),
					psionic_trained = character1.psionic_trained,
					psionic_rating = character1.psionic_rating,
					psionic_talents = character1.array_stringer(character1.psionic_talents),
					tas_member = character1.tas_member,
					career_name = character1.career["name"], 
					ranks = character1.career["ranks"][character1.rank], 
					terms = character1.terms, 
					status = character1.status, 
					cash = character1.cash, 
					skills = character1.skill_stringer(character1.skills), 
					possessions = character1.possession_stringer(character1.possessions),

					# Test for world values 
					size = character1.upp_stringer(character1.birth_size),
					atmosphere = character1.upp_stringer(character1.birth_atmosphere),
					hydrographics = character1.upp_stringer(character1.birth_hydrographics),
					population = character1.upp_stringer(character1.birth_population),
					government = character1.upp_stringer(character1.birth_government),
					lawlevel = character1.upp_stringer(character1.birth_lawlevel),
					techlevel = character1.upp_stringer(character1.birth_techlevel),
					trade = character1.array_stringer(character1.birth_tradelevel)
				)
			)
		sys.stdout = sys.__stdout__
		return "complete"

character = Character()
create_character = character.create_character

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Create Traveller characters. They will be posted to a file or the screen.')

	parser.add_argument('-c', '--char', type=int, help='Number of characters to generate.')
	parser.add_argument('-f', '--file',           help='Save characters to this file name.')
	parser.add_argument('-t', '--template',       help='Template name without the .template extension or spaces in name. Default is text.')
	parser.add_argument('-s', '--seed',           help='seed in the form of a UPP code')

	args = parser.parse_args()

	print(character.create_character(args))