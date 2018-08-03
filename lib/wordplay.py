#wordplay.py
# A module to generate words
# v2.3 - March 31st, 2018
# This is open source code, feel free to use it for any purpose
# contact me at golan2072@gmail.com

#import modules
import random, argparse, time
import stellagama as game



# language structure will use a number of syllable styles but not all.
# randomly create a list of 3 to 7 syllables.
# random decide on the complexity of syllables with most weighted toward the 1,2, some 3 and 4 rare.
# randomly create a sublist of letters (vowel (1-3) and consonant(1-3)) that may be injected into some syllables
# generate words.
# Use a seed which will always be the UPP of the world. This is always make words match for that world.

class Wordplay:
	def __init__ (self):
		self.word =				''
		self.word_pronouced =   ''
		self.number_of_syllables = 1
		self.random_seed =      '1234'
		self.syllables =        ['Sv','Sv','Sv','v','v','v','v','v','v','v','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','v','v','v','v','v','v','v','Sc','Sc','Sc']
		self.syllable_length =  [1,1,1,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,4,4,4]
		self.syllable_size_list =  [0,0,0,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3]

		self.vowels =               ['a','e','i','o','u']
		self.voiced_vowels =        ['ay','ya','oy','ee','ea','ou','oo','ow']
		self.consonants =           ['b','ch','d','f','g','h','j','k','l','m','n','p','r','s','t','v','w','y','z']
		self.voiced_consonants =    ['b', 'd', 'g', 'j', 'l', 'm', 'n', 'ng', 'r', 'sz', 'th','v', 'w', 'y', 'z']
		self.voiceless_consonants = ['ch', 'f', 'k', 'p', 's', 'sh', 't', 'th']

		self.syllable_styles = [
				[
					['v'],
					['c']
				],
				[
					['cc'],
					['v','c'],
					['c','v'],
					['vv']
				],
				[
					['c','vv'],
					['cc','v'],
					['cc','c'],
					['c','cc'],
					['v','cc'],
					['vv','c'],
					['vv','v'],
					['v','vv'],
					['c','v','c'],
					['v','c','v']
				],
				[
					['c','vv','v'],
					['c','v','vv'],
					['cc','v','v'],
					['cc','c','v'],
					['c','cc','v'],
					['cc','c','c'],
					['c','cc','c'],
					['c','v','cc'],
					['cc','v','c'],
					['c','vv','c'],
					['v','cc','c'],
					['v','c','cc'],
					['vv','cc'],
					['vv','v','c'],
					['vv','vv'],
					['v','vv','v'],
					['v','c','vv'],
					['vv','c','v'],
					['v','cc','v']
				]
			]



		self.language_syllable_styles=[]



	def create_syllables(self, number_of_syllables):
		# work
		current_syllable = 1
		syllable_size = 1
		current_word_syllables = []
		
		while current_syllable <= number_of_syllables:
			# size of each syllable
			syllable_size = game.random_choice(self.syllable_size_list)
			print (syllable_size + 1)
			current_word_syllables.extend (game.random_choice(self.syllable_styles[syllable_size]) )
			# current_word_syllables.extend(",")
			current_syllable += 1
			print(current_word_syllables)

		#clean up odd letter choices.
		# compare current and next sounds if they match combine.
		current_sound = 0
		while current_sound < len(current_word_syllables):
			print(current_word_syllables)

			current_letter = current_word_syllables[current_sound]
			next_letter = current_word_syllables[current_sound+1] if current_sound + 1 < len(current_word_syllables) else 'x'
			
			if current_letter == 'v' and next_letter == 'v':
				del(current_word_syllables[current_sound + 1])
				current_word_syllables[current_sound] = game.random_choice(['v','vv'])

			elif current_letter == 'vv' and next_letter == 'vv':
				del(current_word_syllables[current_sound + 1])

			# elif current_letter == 'v' and next_letter == 'vv':
			# 	del(current_word_syllables[current_sound + 1])
			# 	current_word_syllables[current_sound] = 'vv'

			elif current_letter == 'vv' and next_letter == 'v':
				del(current_word_syllables[current_sound + 1])
				current_word_syllables[current_sound] = game.random_choice(['v','vv'])

			elif current_letter == 'cc' and next_letter == 'cc':
				del(current_word_syllables[current_sound + 1])
				current_word_syllables[current_sound] = game.random_choice(['c','cc'])

			elif current_letter == 'c' and next_letter == 'cc':
				del(current_word_syllables[current_sound + 1])
				current_word_syllables[current_sound] = game.random_choice(['c','cc'])

			elif current_letter == 'c' and next_letter == 'c':
				del(current_word_syllables[current_sound + 1])
				current_word_syllables[current_sound] = game.random_choice(['c','cc'])

			if current_letter != next_letter:
				current_sound += 1
			else:
				current_letter = game.random_choice(['v','vv'])

		return current_word_syllables

	def create_seed(self):
		if args.seed:
			self.random_seed = args.seed
		else:
			self.random_seed = time.strftime("%H:%M:%S", time.gmtime())

		random.seed(self.random_seed)

		# print (self.random_seed)

	def create_singleton_vowels(self):
		# work
		return 'create_singleton_vowels'

	def create_singleton_consonants(self):
		# work
		return 'create_singleton_consonants'

	def create_word(self):

		self.create_seed()

		# number of syllables
		self.number_of_syllables = game.random_choice(self.syllable_length)
		print (self.number_of_syllables)
		

		# create array of syllables

		current_word_syllables = self.create_syllables(self.number_of_syllables)

		print(current_word_syllables)
		for current_letter in current_word_syllables:
			if current_letter == 'v':
				letter = game.random_choice(self.vowels)
				self.word += letter
				self.word_pronouced += letter
				print (self.word)
			elif current_letter == 'vv':
				letter = game.random_choice(self.voiced_vowels)
				self.word += letter
				self.word_pronouced += letter
				print (self.word)

			elif current_letter == 'c':
				letter = game.random_choice(self.voiceless_consonants)
				self.word += letter
				self.word_pronouced += letter
				print (self.word)

			elif current_letter == 'cc':
				letter = game.random_choice(self.voiced_consonants)
				self.word += letter
				self.word_pronouced += letter
				print (self.word)

			elif current_letter == ",":
				self.word_pronouced += current_letter
				print (self.word)
			else:
				self.word += current_letter
				self.word_pronouced += current_letter


		print('word: '+ self.word)
		print('pronouced: '+ self.word_pronouced)

		return '\n\ncreate_word finished'


wordplay = Wordplay()
create_word = wordplay.create_word

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Create words with a set pattern')
	parser.add_argument('-s','--seed',help='seed with Homeworld UPP code')
	args = parser.parse_args()

	print(wordplay.create_word())
