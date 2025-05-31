"""
Character module for CTchargen.

This module handles character generation for Classic Traveller.
"""

import random
from typing import Dict, List, Any, Optional, Tuple, Union
import os

from src.lib import stellagama as sg
from src.lib import wordplay
from src.config import config
from src.careers import (
    generate_career, 
    generate_rank, 
    generate_skills, 
    generate_equipment, 
    generate_cash,
    generate_career_history,
    CAREERS,
    MAX_TERMS,
    AGING_START_TERM
)
from src.psionics import generate_psionic_abilities


class Character:
    """
    Class representing a Traveller character.
    """
    
    def __init__(self):
        """Initialize a new character with random characteristics."""
        # Basic characteristics
        self.upp = self._generate_characteristics()
        self.name = ""
        self.gender = self._generate_gender()
        self.age = 18
        self.race = self._generate_race()
        
        # Skills and career
        self.skills = {}
        self.career = ""
        self.rank = 0
        self.terms = 0
        self.died = False
        
        # Equipment
        self.weapons = []
        self.armor = ""
        self.equipment = []
        self.cash = 0
        
        # Psionics
        self.psionic = {
            "has_psionic": False,
            "psr": 0,
            "is_trained": False,
            "talents": []
        }
        
        # Generate a random name
        self._generate_name()
        
        # Generate career and related attributes
        self._generate_career_and_skills()
        
        # Generate psionic abilities
        self._generate_psionic_abilities()
    
    def _generate_characteristics(self) -> Dict[str, int]:
        """
        Generate the six basic characteristics for a character.
        
        Returns:
            Dict[str, int]: Dictionary of characteristics
        """
        return {
            "STR": self._roll_characteristic(),
            "DEX": self._roll_characteristic(),
            "END": self._roll_characteristic(),
            "INT": self._roll_characteristic(),
            "EDU": self._roll_characteristic(),
            "SOC": self._roll_characteristic()
        }
    
    def _roll_characteristic(self) -> int:
        """
        Roll 2d6 for a characteristic.
        
        Returns:
            int: Characteristic value (2-12)
        """
        return sg.dice(2, 6)
    
    def _generate_gender(self) -> str:
        """
        Generate a random gender.
        
        Returns:
            str: "Male" or "Female"
        """
        return random.choice(["Male", "Female"])
    
    def _generate_race(self) -> str:
        """
        Generate a random race.
        
        Returns:
            str: Race name
        """
        return random.choice(config.get_races())
    
    def _generate_name(self) -> None:
        """Generate a random name for the character."""
        # Use phonetic name generation
        if config.get('name_generation', {}).get('use_phonetic', True):
            self.name = wordplay.create_word(None)
            # Capitalize the first letter
            self.name = self.name[0].upper() + self.name[1:]
        else:
            # Use name lists based on gender
            if self.gender == "Male":
                name_file = os.path.join(config.NAMES_DIR, "malenames.txt")
            else:
                name_file = os.path.join(config.NAMES_DIR, "femalenames.txt")
            
            # Add a surname
            surname_file = os.path.join(config.NAMES_DIR, "surnames.txt")
            
            try:
                first_name = sg.random_line(name_file)
                surname = sg.random_line(surname_file)
                self.name = f"{first_name} {surname}"
            except FileNotFoundError:
                # Fallback to phonetic name generation
                self.name = wordplay.create_word(None)
                self.name = self.name[0].upper() + self.name[1:]
    
    def add_skill(self, skill: str, level: int = 1) -> None:
        """
        Add a skill to the character.
        
        Args:
            skill: Skill name
            level: Skill level (default: 1)
        """
        if skill in self.skills:
            self.skills[skill] += level
        else:
            self.skills[skill] = level
    
    def _generate_career_and_skills(self) -> None:
        """Generate a career, skills, and equipment for the character using Classic Traveller rules."""
        # Generate career history
        self.career, self.rank, self.terms, self.died = generate_career_history(self.upp)
        
        # Update age based on terms
        self.age = 18 + (self.terms * 4)
        
        # If the character died, reduce terms by 1 (they died during their last term)
        if self.died:
            self.terms = max(1, self.terms - 1)
        
        # Generate skills
        self.skills = generate_skills(self.career, self.terms)
        
        # Generate equipment
        self.weapons, self.armor, self.equipment = generate_equipment(self.career)
        
        # Generate cash
        self.cash = generate_cash(self.career, self.terms)
        
        # Apply aging effects if applicable
        if self.terms >= AGING_START_TERM:
            self._apply_aging_effects()
    
    def _apply_aging_effects(self) -> None:
        """Apply aging effects to the character's characteristics."""
        # Apply aging effects for each term after the 3rd
        for term in range(AGING_START_TERM, self.terms + 1):
            # Roll for each physical characteristic (STR, DEX, END)
            for stat in ["STR", "DEX", "END"]:
                # Chance of reduction increases with age
                target = 8 + (term - AGING_START_TERM)
                
                # Roll 2D6
                roll = sg.dice(2, 6)
                
                # If roll is >= target, reduce characteristic by 1
                if roll >= target:
                    self.upp[stat] = max(1, self.upp[stat] - 1)
    
    def _generate_psionic_abilities(self) -> None:
        """Generate psionic abilities for the character."""
        self.psionic = generate_psionic_abilities(self.age)
    
    def set_career(self, career: str, rank: int = 0, terms: int = 1) -> None:
        """
        Set the character's career.
        
        Args:
            career: Career name
            rank: Rank in the career (default: 0)
            terms: Number of terms served (default: 1)
        """
        self.career = career
        self.rank = rank
        self.terms = terms
        self.age = 18 + (terms * 4)
    
    def add_weapon(self, weapon: str) -> None:
        """
        Add a weapon to the character's equipment.
        
        Args:
            weapon: Weapon name
        """
        self.weapons.append(weapon)
    
    def set_armor(self, armor: str) -> None:
        """
        Set the character's armor.
        
        Args:
            armor: Armor name
        """
        self.armor = armor
    
    def add_equipment(self, item: str) -> None:
        """
        Add an item to the character's equipment.
        
        Args:
            item: Equipment item name
        """
        self.equipment.append(item)
    
    def set_cash(self, amount: int) -> None:
        """
        Set the character's cash amount.
        
        Args:
            amount: Cash amount in credits
        """
        self.cash = amount
    
    def get_upp_string(self) -> str:
        """
        Get the character's UPP as a string in hexadecimal notation.
        
        Returns:
            str: UPP string (e.g., "777777" or "7A7B8C")
        """
        def to_hex(value):
            if value < 10:
                return str(value)
            else:
                return chr(ord('A') + (value - 10))
                
        return "".join(to_hex(self.upp[stat]) for stat in ["STR", "DEX", "END", "INT", "EDU", "SOC"])
    
    def get_skills_string(self) -> str:
        """
        Get the character's skills as a formatted string.
        
        Returns:
            str: Skills string (e.g., "Pilot-1, Gunner-2")
        """
        if not self.skills:
            return "None"
        
        skill_strings = []
        for skill, level in self.skills.items():
            skill_strings.append(f"{skill}-{level}")
        
        return ", ".join(skill_strings)
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the character to a dictionary.
        
        Returns:
            Dict[str, Any]: Character data as a dictionary
        """
        return {
            "name": self.name,
            "gender": self.gender,
            "race": self.race,
            "age": self.age,
            "upp": self.upp,
            "upp_string": self.get_upp_string(),
            "career": self.career,
            "rank": self.rank,
            "terms": self.terms,
            "died": self.died,
            "skills": self.skills,
            "skills_string": self.get_skills_string(),
            "weapons": self.weapons,
            "armor": self.armor,
            "equipment": self.equipment,
            "cash": self.cash,
            "psionic": self.psionic
        }
    
    def get_rank_title(self) -> str:
        """
        Get the character's rank title based on career and rank.
        
        Returns:
            str: Rank title
        """
        if not self.career or self.career not in CAREERS:
            return ""
        
        ranks = CAREERS[self.career]["ranks"]
        if self.rank < len(ranks):
            return ranks[self.rank]
        else:
            return ranks[-1] if ranks else ""
    
    def get_psionic_string(self) -> str:
        """
        Get the character's psionic abilities as a formatted string.
        
        Returns:
            str: Psionic abilities string
        """
        if not self.psionic["has_psionic"]:
            return "None"
        
        psr = self.psionic["psr"]
        is_trained = self.psionic["is_trained"]
        talents = self.psionic["talents"]
        
        if not is_trained:
            return f"PSR {psr} (Untrained)"
        
        talents_str = ", ".join(talents) if talents else "None"
        return f"PSR {psr} (Trained) - Talents: {talents_str}"
    
    def __str__(self) -> str:
        """
        Get a string representation of the character.
        
        Returns:
            str: Character summary
        """
        rank_title = self.get_rank_title()
        rank_display = f"{rank_title} (Rank {self.rank})" if rank_title else f"Rank {self.rank}"
        
        weapons_str = ", ".join(self.weapons) if self.weapons else "None"
        equipment_str = ", ".join(self.equipment) if self.equipment else "None"
        
        status = "Deceased (died during service)" if self.died else "Active"
        
        return (
            f"Name: {self.name}\n"
            f"UPP: {self.get_upp_string()}\n"
            f"Gender: {self.gender}\n"
            f"Race: {self.race}\n"
            f"Age: {self.age}\n"
            f"Career: {self.career}\n"
            f"Rank: {rank_display}\n"
            f"Terms: {self.terms}\n"
            f"Status: {status}\n"
            f"Skills: {self.get_skills_string()}\n"
            f"Weapons: {weapons_str}\n"
            f"Armor: {self.armor or 'None'}\n"
            f"Equipment: {equipment_str}\n"
            f"Cash: {self.cash} Credits\n"
            f"Psionics: {self.get_psionic_string()}\n"
        )


def generate_character() -> Character:
    """
    Generate a new random character.
    
    Returns:
        Character: A new character instance
    """
    return Character()


def generate_characters(count: int = 1) -> List[Character]:
    """
    Generate multiple random characters.
    
    Args:
        count: Number of characters to generate
        
    Returns:
        List[Character]: List of character instances
    """
    return [Character() for _ in range(count)]
