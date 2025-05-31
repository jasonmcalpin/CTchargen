"""
World generation module for CTchargen.

This module handles world generation for Classic Traveller.

v3.0 - May 30th, 2025 - Updated for CTchargen refactoring
"""

from typing import List, Dict, Any, Optional, Union

from src.lib import stellagama as sg


class World:
    """
    Class for generating Traveller worlds.
    """
    
    def __init__(self):
        """Initialize and generate a random world."""
        self.starport = sg.random_choice([
            'X', 'E', 'E', 'E', 'E', 'E', 'E', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D',
            'C', 'C', 'C', 'C', 'C', 'C', 'C', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A'
        ])
        
        self.size = sg.dice(2, 6) - 2
        self.atmosphere = self.atmosphere_calc(self.size)
        self.hydrographics = self.hydrographics_calc(self.size, self.atmosphere)
        self.population = sg.dice(2, 6) - 2
        self.government = self.government_calc(self.population)
        self.lawlevel = self.law_level_calc(self.government, self.population)
        self.techlevel = self.techlevel_calc(
            self.population, self.starport, self.size, 
            self.atmosphere, self.hydrographics, self.government
        )
        
        self.upp = [
            self.size, self.atmosphere, self.hydrographics, 
            self.population, self.government, self.lawlevel, self.techlevel
        ]
        
        self.tradelevel = self.trade_classification(
            self.size, self.atmosphere, self.hydrographics, 
            self.population, self.government, self.lawlevel, self.techlevel
        )
    
    def atmosphere_calc(self, size: int) -> int:
        """
        Calculate atmosphere based on size.
        
        Args:
            size: World size
            
        Returns:
            int: Atmosphere value
        """
        atmo_base = sg.dice(2, 6) - 7 + size

        if atmo_base <= 0:
            return 0
        elif atmo_base >= 15:
            return 15
        else:
            return atmo_base

    def hydrographics_calc(self, size: int, atmosphere: int) -> int:
        """
        Calculate hydrographics based on size and atmosphere.
        
        Args:
            size: World size
            atmosphere: World atmosphere
            
        Returns:
            int: Hydrographics value
        """
        hydro_base = sg.dice(2, 6) - 7
        
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

    def government_calc(self, population: int) -> int:
        """
        Calculate government based on population.
        
        Args:
            population: World population
            
        Returns:
            int: Government value
        """
        gov_base = sg.dice(2, 6) - 7

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

    def law_level_calc(self, government: int, population: int) -> int:
        """
        Calculate law level based on government and population.
        
        Args:
            government: World government
            population: World population
            
        Returns:
            int: Law level value
        """
        law_base = sg.dice(2, 6) - 7

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

    def techlevel_calc(self, population: int, starport: str, size: int, 
                      atmosphere: int, hydrographics: int, government: int) -> int:
        """
        Calculate tech level based on various world characteristics.
        
        Args:
            population: World population
            starport: World starport class
            size: World size
            atmosphere: World atmosphere
            hydrographics: World hydrographics
            government: World government
            
        Returns:
            int: Tech level value
        """
        tech_base = sg.dice(1, 6)

        if population <= 0:
            return 0
        else:
            if starport == 'X':
                tech_base += -6
            elif starport == 'C':
                tech_base += 2
            elif starport == 'B':
                tech_base += 4
            elif starport == 'A':
                tech_base += 6

            if size in [1, 2]:
                tech_base += 2
            elif size in [2, 3, 4]:
                tech_base += 1

            if atmosphere in [0, 1, 2, 3, 10, 11, 12, 13, 14, 15]:
                tech_base += 1

            if hydrographics in [0, 9]:
                tech_base += 1
            elif hydrographics == 10:
                tech_base += 2

            if population in [0, 1, 2, 3, 4, 5, 9]:
                tech_base += 1
            elif population == 10:
                tech_base += 2
            elif population == 11:
                tech_base += 3
            elif population == 12:
                tech_base += 4

            if government in [0, 5]:
                tech_base += 1
            elif government == 7:
                tech_base += 2
            elif government in [13, 14]:
                tech_base += -2

            if tech_base <= 0:
                return 0
            elif tech_base >= 15:
                return 15
            else:
                return tech_base

    def trade_classification(self, size: int, atmosphere: int, hydrographics: int, 
                           population: int, government: int, lawlevel: int, techlevel: int) -> List[str]:
        """
        Determine trade classifications based on world characteristics.
        
        Args:
            size: World size
            atmosphere: World atmosphere
            hydrographics: World hydrographics
            population: World population
            government: World government
            lawlevel: World law level
            techlevel: World tech level
            
        Returns:
            List[str]: List of trade classifications
        """
        trade_list = []

        if atmosphere in [4, 5, 6, 7, 8, 9] and hydrographics in [4, 5, 6, 7, 8] and population in [4, 5, 6, 7]:
            trade_list.append('Ag')
        if size == 0 and atmosphere == 0 and hydrographics == 0:
            trade_list.append('As')
        if population == 0 and government == 0 and lawlevel == 0:
            trade_list.append('Ba')
        if atmosphere >= 2 and hydrographics == 0:
            trade_list.append('De')
        if atmosphere >= 10 and hydrographics >= 1:
            trade_list.append('Fl')
        if atmosphere >= 5 and hydrographics in [4, 5, 6, 7, 8, 9] and population in [4, 5, 6, 7, 8]:
            trade_list.append('Ga')
        if population >= 9:
            trade_list.append('Hi')
        if techlevel >= 12:
            trade_list.append('Ht')
        if atmosphere in [0, 1] and hydrographics >= 1:
            trade_list.append('Ic')
        if atmosphere in [0, 1, 2, 4, 7, 9] and population >= 9:
            trade_list.append('In')
        if population in [1, 2, 3]:
            trade_list.append('Lo')
        if techlevel <= 5:
            trade_list.append('Lt')
        if atmosphere in [0, 1, 2, 3] and hydrographics in [0, 1, 2, 3] and population >= 6:
            trade_list.append('Na')
        if population in [4, 5, 6]:
            trade_list.append('Ni')
        if atmosphere in [2, 3, 3, 4, 5] and hydrographics in [0, 1, 2, 3]:
            trade_list.append('Po')
        if atmosphere in [6, 8] and population in [6, 7, 8]:
            trade_list.append('Ri')
        if hydrographics == 10:
            trade_list.append('Wa')
        if atmosphere == 0:
            trade_list.append('Va')

        return trade_list
    
    def get_upp_string(self) -> str:
        """
        Get the world's UPP as a string.
        
        Returns:
            str: UPP string
        """
        return "".join(str(sg.pseudo_hex(val)) for val in self.upp)
    
    def get_trade_string(self) -> str:
        """
        Get the world's trade classifications as a string.
        
        Returns:
            str: Trade classifications string
        """
        return " ".join(self.tradelevel)
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the world to a dictionary.
        
        Returns:
            Dict[str, Any]: World data as a dictionary
        """
        return {
            "starport": self.starport,
            "size": self.size,
            "atmosphere": self.atmosphere,
            "hydrographics": self.hydrographics,
            "population": self.population,
            "government": self.government,
            "lawlevel": self.lawlevel,
            "techlevel": self.techlevel,
            "upp": self.upp,
            "upp_string": self.get_upp_string(),
            "tradelevel": self.tradelevel,
            "trade_string": self.get_trade_string()
        }
    
    def __str__(self) -> str:
        """
        Get a string representation of the world.
        
        Returns:
            str: World summary
        """
        return (
            f"UPP: {self.get_upp_string()}\n"
            f"Starport: {self.starport}\n"
            f"Size: {self.size}\n"
            f"Atmosphere: {self.atmosphere}\n"
            f"Hydrographics: {self.hydrographics}\n"
            f"Population: {self.population}\n"
            f"Government: {self.government}\n"
            f"Law Level: {self.lawlevel}\n"
            f"Tech Level: {self.techlevel}\n"
            f"Trade Classifications: {self.get_trade_string()}"
        )


def generate_world() -> World:
    """
    Generate a new random world.
    
    Returns:
        World: A new world instance
    """
    return World()


def generate_worlds(count: int = 1) -> List[World]:
    """
    Generate multiple random worlds.
    
    Args:
        count: Number of worlds to generate
        
    Returns:
        List[World]: List of world instances
    """
    return [World() for _ in range(count)]
