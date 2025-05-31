"""
Wordplay module for CTchargen.

A module to generate words based on syllable patterns.

v3.0 - May 30th, 2025 - Updated for CTchargen refactoring
"""

import random
import argparse
import time
import json
import os
from typing import List, Dict, Any, Optional, Union

from src.lib import stellagama as sg
from src.config import config


class Wordplay:
    """
    Class for generating words based on syllable patterns.
    """
    
    def __init__(self):
        """Initialize the wordplay generator."""
        self.word = ''
        self.word_pronounced = ''
        self.number_of_syllables = 1
        self.random_seed = '1234'
        self.syllable_length = []
        self.syllable_size_list = []

        self.vowels = []
        self.voiced_vowels = []
        self.voiced_consonants = []
        self.voiceless_consonants = []

        self.syllable_styles = []
        self.language_syllable_styles = []

    def load_dictionary(self) -> None:
        """Load syllable rules from JSON file."""
        data_file = config.get('name_generation', {}).get(
            'data_file', 
            os.path.join(config.BASE_DIR, 'data', 'syllable_starter.json')
        )
        
        try:
            with open(data_file) as syllable_rules:
                data = json.load(syllable_rules)

            self.syllable_length = data['syllable_length']
            self.syllable_size_list = data['syllable_size_list']
            self.vowels = data['vowels']
            self.voiced_vowels = data['voiced_vowels']
            self.voiced_consonants = data['voiced_consonants']
            self.voiceless_consonants = data['voiceless_consonants']
            self.syllable_styles = data['syllable_styles']
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading syllable rules: {e}")
            # Set default values if file can't be loaded
            self.syllable_length = [1, 2, 3]
            self.syllable_size_list = [0, 1, 2]
            self.vowels = ['a', 'e', 'i', 'o', 'u']
            self.voiced_vowels = ['aa', 'ee', 'ii', 'oo', 'uu']
            self.voiced_consonants = ['b', 'd', 'g', 'j', 'l', 'm', 'n', 'r', 'v', 'w', 'y', 'z']
            self.voiceless_consonants = ['c', 'f', 'h', 'k', 'p', 'q', 's', 't', 'x']
            self.syllable_styles = [
                [['v'], ['c', 'v'], ['v', 'c']],
                [['c', 'v', 'c'], ['v', 'c', 'c'], ['c', 'c', 'v']],
                [['c', 'v', 'c', 'c'], ['c', 'c', 'v', 'c']]
            ]

    def create_syllables(self, number_of_syllables: int) -> List[str]:
        """
        Create syllables for a word.
        
        Args:
            number_of_syllables: Number of syllables to create
            
        Returns:
            List[str]: List of syllable components
        """
        current_syllable = 1
        syllable_size = 1
        current_word_syllables = []

        while current_syllable <= number_of_syllables:
            # Size of each syllable
            syllable_size = sg.random_choice(self.syllable_size_list)
            current_word_syllables.extend(sg.random_choice(self.syllable_styles[syllable_size]))
            current_syllable += 1

        # Clean up odd letter choices
        # Compare current and next sounds if they match combine
        current_sound = 0
        while current_sound < len(current_word_syllables):
            current_letter = current_word_syllables[current_sound]
            next_letter = current_word_syllables[current_sound + 1] if current_sound + 1 < len(current_word_syllables) else 'x'

            if current_letter == 'v' and next_letter == 'v':
                del(current_word_syllables[current_sound + 1])
                current_word_syllables[current_sound] = sg.random_choice(['v', 'vv'])

            elif current_letter == 'vv' and next_letter == 'vv':
                del(current_word_syllables[current_sound + 1])

            elif current_letter == 'vv' and next_letter == 'v':
                del(current_word_syllables[current_sound + 1])
                current_word_syllables[current_sound] = sg.random_choice(['v', 'vv'])

            elif current_letter == 'cc' and next_letter == 'cc':
                del(current_word_syllables[current_sound + 1])
                current_word_syllables[current_sound] = sg.random_choice(['c', 'cc'])

            elif current_letter == 'c' and next_letter == 'cc':
                del(current_word_syllables[current_sound + 1])
                current_word_syllables[current_sound] = sg.random_choice(['c', 'cc'])

            elif current_letter == 'c' and next_letter == 'c':
                del(current_word_syllables[current_sound + 1])
                current_word_syllables[current_sound] = sg.random_choice(['c', 'cc'])

            if current_letter != next_letter:
                current_sound += 1
            else:
                current_letter = sg.random_choice(['v', 'vv'])

        return current_word_syllables

    def create_seed(self, args: Optional[argparse.Namespace] = None, seed: Optional[str] = None) -> None:
        """
        Set the random seed for word generation.
        
        Args:
            args: Command line arguments (optional)
            seed: Seed string (optional)
        """
        if args and hasattr(args, 'seed') and args.seed:
            self.random_seed = args.seed
        elif seed and seed != 'A-1234567':
            self.random_seed = seed
        else:
            self.random_seed = str(time.time())

        random.seed(self.random_seed)

    def create_word(self, args: Optional[argparse.Namespace] = None, seed: Optional[str] = None) -> str:
        """
        Create a random word.
        
        Args:
            args: Command line arguments (optional)
            seed: Seed string (optional)
            
        Returns:
            str: Generated word
        """
        self.load_dictionary()

        self.word = ''
        self.word_pronounced = ''
        self.create_seed(args, seed)

        # Number of syllables
        self.number_of_syllables = sg.random_choice(self.syllable_length)

        # Create array of syllables
        current_word_syllables = self.create_syllables(self.number_of_syllables)

        for current_letter in current_word_syllables:
            if current_letter == 'v':
                letter = sg.random_choice(self.vowels)
                self.word += letter
                self.word_pronounced += letter
            elif current_letter == 'vv':
                letter = sg.random_choice(self.voiced_vowels)
                self.word += letter
                self.word_pronounced += letter
            elif current_letter == 'c':
                letter = sg.random_choice(self.voiceless_consonants)
                self.word += letter
                self.word_pronounced += letter
            elif current_letter == 'cc':
                letter = sg.random_choice(self.voiced_consonants)
                self.word += letter
                self.word_pronounced += letter
            elif current_letter == ",":
                self.word_pronounced += current_letter
            else:
                self.word += current_letter
                self.word_pronounced += current_letter

        return self.word


# Create a singleton instance
wordplay = Wordplay()
create_word = wordplay.create_word


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create words with a set pattern')
    parser.add_argument('-s', '--seed', help='seed with Homeworld UPP code')
    args = parser.parse_args()

    print(wordplay.create_word(args))
