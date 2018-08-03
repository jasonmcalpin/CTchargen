
#!/usr/bin/python
import random, argparse, time



# language structure will use a number of syllable styles but not all.
# randomly create a list of 3 to 7 syllables.
# random decide on the complexity of syllables with most weighted toward the 1,2, some 3 and 4 rare. 
# randomly create a sublist of letters (vowel (1-3) and consonant(1-3)) that may be injected into some syllables
# generate words.
# Use a seed which will always be the UPP of the world. This is always make words match for that world.

class Wordplay:
	def __init__ (self):
		self.random_seed =       '1234'
		self.syllables =        ['Sv','Sv','Sv','v','v','v','v','v','v','v','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','c','v','v','v','v','v','v','v','Sc','Sc','Sc']
		self.syllable_length =  [1,1,1,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,4,4,4]
		self.vowels =           ['a','e','i','o','u']
		self.consonant =        ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

		self.syllable_styles_1 = [
				['v'],
				['c']
			]
		self.syllable_styles_2 = [
				['c','c'],
				['v','c'],
				['c','v'],
				['c','c'],
				['v','v']
			]
		self.syllable_styles_3 = [
				['c','v','v'],
				['c','c','v'],
				['c','c','c'],
				['v','c','c'],
				['v','v','c'],
				['v','v','v'],
				['c','v','c'],
				['v','c','v']
			]
		self.syllable_styles_4 = [
				['c','v','v','v'],
				['c','c','v','v'],
				['c','c','c','v'],
				['c','c','c','c'],
				['c','v','c','c'],
				['c','c','v','c'],
				['c','v','v','c'],
				['v','c','c','c'],
				['v','v','c','c'],
				['v','v','v','c'],
				['v','v','v','v'],
				['v','c','v','v'],
				['v','v','c','v'],
				['v','c','c','v']
			]

		self.syllable_singleton_styles_1 = [
				['S']
			]
		self.syllable_singleton_styles_2 = [
				['S','' ],
				['' ,'S'],
				['S','S'],
			]
		self.syllable_singleton_styles_3 = [
				['S','' ,'' ],
				['' ,'S','' ],
				['' ,'' ,'S'],
				['S','S','' ],
				['S','S','S'],
				['' ,'S','S'],
			]
		self.syllable_singleton_styles_4 = [
				['S','' ,'' ,'' ],
				['' ,'S','' ,'' ],
				['' ,'' ,'S','' ],
				['' ,'' ,'' ,'S'],
				['S','S','' ,'' ],
				['' ,'S','S','' ],
				['' ,'' ,'S','S'],
				['S','S','S','' ],
				['' ,'S','S','S'],
				['S','S','S','S'],
			]

		self.language_syllable_styles=[]
		self.singleton_vowels = []
		self.singleton_consonants = []


	def create_syllable_styles(self):
		# work
		return 'create_syllable_styles'

	def create_seed(self):
		if args.seed:
			self.random_seed = args.seed
		else:
			self.random_seed = time.strftime("%H:%M:%S", time.gmtime())

		random.seed(self.random_seed)

		print (self.random_seed)


	def create_singleton_vowels(self):
		# work
		return 'create_singleton_vowels'

	def create_singleton_consonants(self):
		# work
		return 'create_singleton_consonants'

	def create_word(self):
	

		self.create_seed()

		# all random rolls start here for consistancy
		print( random.randint(1,36) )
		return 'create_word'




		# work

# https://www.howmanysyllables.com/english_grammar/syllable_rules/syllable_patterns-vcv-vccv
# Syllable Rules   >>   Syllable Patterns    Examples

# Syllable Patterns
# Words are divided into syllables by using the Syllable Division Rules or Syllable Pattern Rules. To divide using syllable patterns:
# Separate prefixes and suffixes from root words.
# examples:  pre-view, work-ing, re-do, end-less, & out-ing
# Write a V on top of every vowel.
# Write a C on top of every consonant.
# Use the V (vowel) & C (consonant) patterns below.
# Cite This SourceDownload as PDF
# VC/CV and VC/CCV
# Divide between the 1st and 2nd consonants.
# examples:  buf-fet, des-sert, ob-ject, ber-ry, & pil-grim
# Never split 2 consonants that are different letters, but make only 1 sound when pronounced together.
# examples:  th, sh, ph, th, ch, & wh

 
# V/CV and VC/V
# Does the 1st vowel have a long sound?  (Like the 'i' in line)
# Divide before the consonant:  V/CV
# examples:  ba-by, re-sult, i-vy, fro-zen, & Cu-pid
# Does the 1st vowel have a short sound?  (Like the 'i' in mill)
# Divide after the consonant:  VC/V
# examples:  met-al, riv-er, mod-el, val-ue, & rav-age
# Fun Fact
# The word “alphabet” 
# comes from Alpha & Beta.
# !Get more facts

 
# CV/V, CV/VC, and CV/VVC
# Do the vowels make 2 different vowel sounds?
# Divide between the vowel letters which separate the different sounds.
# examples:  tri-o, po-em, li-on, be-ing, & cu-ri-ous

 

 
# VCe
# VCe stands for Vowel-Consonant-e.
# The "e" in VCe is usually silent.
# VCe is usually the last syllable in a root word.
# If the word has more than 1 syllable, divide before the vowel.
# examples:  ex-ile. take, line, tone, & tune
# C-le
# C-le stands for Consonant-le.
# It's usually the last syllable in a root word.
# Does the word end with 'ckle'?
# Divide right before the 'le.'
# examples:  tack-le, freck-le, tick-le, & buck-le
# Does the word end with 'le' (not 'ckle')?
# Is the letter before the 'le' a consonant?
# Divide 1 letter before the 'le.'
# examples:  ap-ple, rum-ble, fa-ble, & ta-ble
# Is the letter before the 'le' a vowel?
# Do nothing.
# examples:  ale, scale, sale, file, & tile
# Next:  Syllable Rules
# Syllable Rules   >>   Syllable Patterns    Examples

# Examples
# Buffet
# cvc-cvc
# buf-fet
# Pilgrim
# cvc-ccvc
# pil-grim

 
# Baby
# cv-cv
# ba-by
# Metal
# cvc-vc
# met-al
# Trio
# ccv-v
# tri-o
# Poem
# cv-vc
# po-em
# Curious
# cv-cv-vvc
# cu-ri-ous
# Take
# cvce
# take
# Exile
# vc-vce
# ex-ile
# Tackle
# cvck-le
# tack-le
# Apple
# vc-cle
# ap-ple
# 
# 

wordplay = Wordplay()
create_word = wordplay.create_word

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Create words with a set pattern')
	parser.add_argument('-s', '--seed',           help='seed with Homeworld UPP code')
	args = parser.parse_args()

	print(wordplay.create_word())
