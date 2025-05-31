"""
Careers module for CTchargen.

This module handles career generation for Classic Traveller characters.
"""

import random
from typing import Dict, List, Any, Optional, Tuple

from src.lib import stellagama as sg

# Define career data with Classic Traveller tables
CAREERS = {
    "Navy": {
        "ranks": [
            "Crewman",
            "Ensign",
            "Lieutenant",
            "Lt Commander",
            "Commander",
            "Captain",
            "Admiral"
        ],
        "skills": [
            "Pilot",
            "Navigation",
            "Engineering",
            "Gunnery",
            "Computer",
            "Electronics",
            "Mechanical",
            "Medical",
            "Tactics",
            "Admin",
            "Leadership"
        ],
        "weapons": [
            "Laser Pistol",
            "Laser Rifle",
            "Cutlass"
        ],
        "equipment": [
            "Communicator",
            "Computer Terminal",
            "Dress Uniform",
            "Toolkit"
        ],
        "cash_table": [1000, 5000, 10000, 20000, 30000, 50000, 100000],
        # Classic Traveller tables
        "enlistment": 8,
        "enlistment_dm": {
            "INT": [8, 1],
            "EDU": [9, 2]
        },
        "survival": 5,
        "survival_dm": {
            "INT": [7, 1],
            "EDU": [8, 2]
        },
        "commission": 10,
        "commission_dm": {
            "SOC": [9, 1]
        },
        "promotion": 8,
        "promotion_dm": {
            "EDU": [8, 1]
        },
        "reenlistment": 6
    },
    "Marines": {
        "ranks": [
            "Private",
            "Lieutenant",
            "Captain",
            "Major",
            "Lt Colonel",
            "Colonel",
            "General"
        ],
        "skills": [
            "Tactics",
            "Battle Dress",
            "Gunnery",
            "Blade Combat",
            "Gun Combat",
            "Recon",
            "Leadership",
            "Demolition",
            "Heavy Weapons",
            "Survival"
        ],
        "weapons": [
            "Assault Rifle",
            "Combat Knife",
            "Grenade Launcher",
            "Laser Rifle"
        ],
        "equipment": [
            "Combat Armor",
            "Communicator",
            "Survival Kit",
            "Tactical Display"
        ],
        "cash_table": [1000, 5000, 10000, 20000, 30000, 50000, 100000],
        # Classic Traveller tables
        "enlistment": 9,
        "enlistment_dm": {
            "INT": [8, 1],
            "STR": [8, 1]
        },
        "survival": 6,
        "survival_dm": {
            "END": [8, 2]
        },
        "commission": 9,
        "commission_dm": {
            "EDU": [7, 1]
        },
        "promotion": 9,
        "promotion_dm": {
            "SOC": [8, 1]
        },
        "reenlistment": 6
    },
    "Army": {
        "ranks": [
            "Private",
            "Lieutenant",
            "Captain",
            "Major",
            "Lt Colonel",
            "Colonel",
            "General"
        ],
        "skills": [
            "Gun Combat",
            "Forward Observer",
            "Tactics",
            "Leadership",
            "Mechanical",
            "Electronics",
            "Recon",
            "Heavy Weapons",
            "Survival",
            "Vehicle"
        ],
        "weapons": [
            "Rifle",
            "Pistol",
            "SMG",
            "Combat Knife"
        ],
        "equipment": [
            "Flak Jacket",
            "Communicator",
            "Survival Kit",
            "Field Computer"
        ],
        "cash_table": [1000, 5000, 10000, 20000, 30000, 50000, 100000],
        # Classic Traveller tables
        "enlistment": 5,
        "enlistment_dm": {
            "DEX": [6, 1],
            "END": [5, 2]
        },
        "survival": 5,
        "survival_dm": {
            "EDU": [6, 2]
        },
        "commission": 5,
        "commission_dm": {
            "END": [7, 1]
        },
        "promotion": 6,
        "promotion_dm": {
            "EDU": [7, 1]
        },
        "reenlistment": 7
    },
    "Scouts": {
        "ranks": [
            "Scout",
            "Senior Scout",
            "Master Scout"
        ],
        "skills": [
            "Pilot",
            "Navigation",
            "Engineering",
            "Mechanical",
            "Electronics",
            "Jack-of-All-Trades",
            "Survival",
            "Recon",
            "Computer",
            "Communication"
        ],
        "weapons": [
            "Rifle",
            "Pistol",
            "Shotgun"
        ],
        "equipment": [
            "Communicator",
            "Survey Scanner",
            "Survival Kit",
            "Portable Computer"
        ],
        "cash_table": [1000, 5000, 10000, 20000, 30000, 50000, 100000],
        # Classic Traveller tables
        "enlistment": 7,
        "enlistment_dm": {
            "INT": [6, 1],
            "STR": [8, 1]
        },
        "survival": 7,
        "survival_dm": {
            "END": [9, 2]
        },
        "commission": 0,  # Scouts don't have commissioned ranks
        "commission_dm": {},
        "promotion": 0,  # Promotion is automatic with terms
        "promotion_dm": {},
        "reenlistment": 3
    },
    "Merchants": {
        "ranks": [
            "Crewman",
            "4th Officer",
            "3rd Officer",
            "2nd Officer",
            "1st Officer",
            "Captain"
        ],
        "skills": [
            "Pilot",
            "Navigation",
            "Engineering",
            "Mechanical",
            "Electronics",
            "Steward",
            "Medic",
            "Admin",
            "Broker",
            "Streetwise",
            "Trade"
        ],
        "weapons": [
            "Pistol",
            "Shotgun"
        ],
        "equipment": [
            "Communicator",
            "Trade Goods",
            "Merchant ID",
            "Portable Computer"
        ],
        "cash_table": [1000, 5000, 10000, 20000, 30000, 50000, 100000],
        # Classic Traveller tables
        "enlistment": 7,
        "enlistment_dm": {
            "INT": [6, 1],
            "STR": [7, 1]
        },
        "survival": 5,
        "survival_dm": {
            "INT": [7, 1]
        },
        "commission": 4,
        "commission_dm": {
            "INT": [6, 1]
        },
        "promotion": 10,
        "promotion_dm": {
            "INT": [9, 1]
        },
        "reenlistment": 4
    },
    "Other": {
        "ranks": [
            "Civilian"
        ],
        "skills": [
            "Streetwise",
            "Brawling",
            "Gambling",
            "Carousing",
            "Broker",
            "Admin",
            "Computer",
            "Electronics",
            "Mechanical",
            "Medical"
        ],
        "weapons": [
            "Knife",
            "Pistol"
        ],
        "equipment": [
            "Communicator",
            "Toolkit",
            "Portable Computer"
        ],
        "cash_table": [1000, 2000, 3000, 4000, 5000, 10000, 20000],
        # Classic Traveller tables
        "enlistment": 3,
        "enlistment_dm": {
            "INT": [5, 1]
        },
        "survival": 5,
        "survival_dm": {
            "INT": [5, 1]
        },
        "commission": 0,  # Civilians don't have commissioned ranks
        "commission_dm": {},
        "promotion": 0,  # Civilians don't have promotions
        "promotion_dm": {},
        "reenlistment": 5
    }
}

# Maximum number of terms allowed
MAX_TERMS = 7

# Aging effects start after this many terms
AGING_START_TERM = 4


def check_enlistment(career: str, upp: Dict[str, int]) -> bool:
    """
    Check if a character can enlist in a career.
    
    Args:
        career: Career name
        upp: Character's UPP (Universal Personality Profile)
        
    Returns:
        bool: True if the character can enlist, False otherwise
    """
    if career not in CAREERS:
        return False
    
    # Get the enlistment target number
    target = CAREERS[career]["enlistment"]
    
    # Apply characteristic DMs
    for stat, values in CAREERS[career]["enlistment_dm"].items():
        threshold, bonus = values
        if upp[stat] >= threshold:
            target -= bonus
    
    # Roll 2D6
    roll = sg.dice(2, 6)
    
    return roll >= target


def check_survival(career: str, upp: Dict[str, int]) -> bool:
    """
    Check if a character survives a term in a career.
    
    Args:
        career: Career name
        upp: Character's UPP (Universal Personality Profile)
        
    Returns:
        bool: True if the character survives, False otherwise
    """
    if career not in CAREERS:
        return False
    
    # Get the survival target number
    target = CAREERS[career]["survival"]
    
    # Apply characteristic DMs
    for stat, values in CAREERS[career]["survival_dm"].items():
        threshold, bonus = values
        if upp[stat] >= threshold:
            target -= bonus
    
    # Roll 2D6
    roll = sg.dice(2, 6)
    
    return roll >= target


def check_commission(career: str, upp: Dict[str, int]) -> bool:
    """
    Check if a character receives a commission.
    
    Args:
        career: Career name
        upp: Character's UPP (Universal Personality Profile)
        
    Returns:
        bool: True if the character receives a commission, False otherwise
    """
    if career not in CAREERS or CAREERS[career]["commission"] == 0:
        return False
    
    # Get the commission target number
    target = CAREERS[career]["commission"]
    
    # Apply characteristic DMs
    for stat, values in CAREERS[career]["commission_dm"].items():
        threshold, bonus = values
        if upp[stat] >= threshold:
            target -= bonus
    
    # Roll 2D6
    roll = sg.dice(2, 6)
    
    return roll >= target


def check_promotion(career: str, upp: Dict[str, int]) -> bool:
    """
    Check if a character receives a promotion.
    
    Args:
        career: Career name
        upp: Character's UPP (Universal Personality Profile)
        
    Returns:
        bool: True if the character receives a promotion, False otherwise
    """
    if career not in CAREERS or CAREERS[career]["promotion"] == 0:
        return False
    
    # Get the promotion target number
    target = CAREERS[career]["promotion"]
    
    # Apply characteristic DMs
    for stat, values in CAREERS[career]["promotion_dm"].items():
        threshold, bonus = values
        if upp[stat] >= threshold:
            target -= bonus
    
    # Roll 2D6
    roll = sg.dice(2, 6)
    
    return roll >= target


def check_reenlistment(career: str) -> bool:
    """
    Check if a character can reenlist in a career.
    
    Args:
        career: Career name
        
    Returns:
        bool: True if the character can reenlist, False otherwise
    """
    if career not in CAREERS:
        return False
    
    # Get the reenlistment target number
    target = CAREERS[career]["reenlistment"]
    
    # Roll 2D6
    roll = sg.dice(2, 6)
    
    # Special case: roll of 12 always succeeds
    if roll == 12:
        return True
    
    return roll >= target


def generate_career() -> str:
    """
    Generate a random career.
    
    Returns:
        str: Career name
    """
    return random.choice(list(CAREERS.keys()))


def process_career_term(career: str, upp: Dict[str, int], current_rank: int, 
                       has_commission: bool) -> Tuple[bool, bool, int]:
    """
    Process a single term in a career.
    
    Args:
        career: Career name
        upp: Character's UPP
        current_rank: Current rank in the career
        has_commission: Whether the character has a commission
        
    Returns:
        Tuple[bool, bool, int]: (survived, has_commission, new_rank)
    """
    # Check survival
    survived = check_survival(career, upp)
    if not survived:
        return False, has_commission, current_rank
    
    # Check for commission if not already commissioned
    if not has_commission and CAREERS[career]["commission"] > 0:
        has_commission = check_commission(career, upp)
        if has_commission:
            current_rank = 1  # Start at rank 1 when commissioned
    
    # Check for promotion if already commissioned
    if has_commission and check_promotion(career, upp):
        max_rank = len(CAREERS[career]["ranks"]) - 1
        current_rank = min(current_rank + 1, max_rank)
    
    # For Scouts, promotion is automatic with terms
    if career == "Scouts":
        max_rank = len(CAREERS[career]["ranks"]) - 1
        current_rank = min(current_rank + 1, max_rank)
    
    return True, has_commission, current_rank


def generate_career_history(upp: Dict[str, int]) -> Tuple[str, int, int, bool]:
    """
    Generate a complete career history for a character.
    
    Args:
        upp: Character's UPP
        
    Returns:
        Tuple[str, int, int, bool]: (career, rank, terms, died)
    """
    # Try to enlist in a random career
    attempts = 0
    career = ""
    while not career and attempts < 6:
        attempts += 1
        potential_career = random.choice(list(CAREERS.keys()))
        if check_enlistment(potential_career, upp):
            career = potential_career
    
    # If all enlistment attempts fail, default to "Other"
    if not career:
        career = "Other"
    
    # Start career
    terms = 0
    rank = 0
    has_commission = False
    died = False
    
    # Process terms
    while terms < MAX_TERMS:
        # First term is mandatory
        if terms == 0 or check_reenlistment(career):
            terms += 1
            survived, has_commission, rank = process_career_term(career, upp, rank, has_commission)
            
            if not survived:
                died = True
                break
        else:
            # Failed reenlistment
            break
    
    return career, rank, terms, died


def generate_rank(career: str, terms: int, upp: Dict[str, int] = None) -> int:
    """
    Generate a rank based on career and terms served.
    
    Args:
        career: Career name
        terms: Number of terms served
        upp: Character's UPP (optional)
        
    Returns:
        int: Rank index
    """
    if career not in CAREERS:
        return 0
    
    # If UPP is provided, use the full career generation system
    if upp is not None:
        _, rank, _, _ = generate_career_history(upp)
        return rank
    
    # Otherwise use the simplified system
    max_rank = min(terms, len(CAREERS[career]["ranks"]) - 1)
    
    # Roll for promotion
    if max_rank > 0:
        # 50% chance of promotion per term after the first
        rank = 0
        for _ in range(terms - 1):
            if random.random() < 0.5:  # 50% chance
                rank += 1
        return min(rank, max_rank)
    else:
        return 0


def generate_skills(career: str, terms: int) -> Dict[str, int]:
    """
    Generate skills based on career and terms served.
    
    Args:
        career: Career name
        terms: Number of terms served
        
    Returns:
        Dict[str, int]: Dictionary of skills and levels
    """
    if career not in CAREERS:
        return {}
    
    skills = {}
    
    # Generate 1-2 skills per term
    for _ in range(terms):
        num_skills = random.randint(1, 2)
        for _ in range(num_skills):
            skill = random.choice(CAREERS[career]["skills"])
            if skill in skills:
                skills[skill] += 1
            else:
                skills[skill] = 1
    
    return skills


def generate_equipment(career: str) -> Tuple[List[str], str, List[str]]:
    """
    Generate equipment based on career.
    
    Args:
        career: Career name
        
    Returns:
        Tuple[List[str], str, List[str]]: Weapons, armor, and equipment
    """
    if career not in CAREERS:
        return [], "", []
    
    # Generate 0-2 weapons
    num_weapons = random.randint(0, 2)
    weapons = []
    for _ in range(num_weapons):
        if CAREERS[career]["weapons"]:
            weapons.append(random.choice(CAREERS[career]["weapons"]))
    
    # Generate armor (20% chance)
    armor = ""
    if random.random() < 0.2:
        if career in ["Marines", "Army"]:
            armor = "Combat Armor" if random.random() < 0.5 else "Flak Jacket"
        elif career in ["Navy", "Scouts"]:
            armor = "Mesh Armor" if random.random() < 0.5 else "Cloth Armor"
        else:
            armor = "Cloth Armor"
    
    # Generate 1-3 equipment items
    num_equipment = random.randint(1, 3)
    equipment = []
    for _ in range(num_equipment):
        if CAREERS[career]["equipment"]:
            equipment.append(random.choice(CAREERS[career]["equipment"]))
    
    return weapons, armor, equipment


def generate_cash(career: str, terms: int) -> int:
    """
    Generate cash based on career and terms served.
    
    Args:
        career: Career name
        terms: Number of terms served
        
    Returns:
        int: Cash amount in credits
    """
    if career not in CAREERS:
        return 0
    
    # Base cash based on terms
    cash_index = min(terms - 1, len(CAREERS[career]["cash_table"]) - 1)
    if cash_index < 0:
        cash_index = 0
    
    base_cash = CAREERS[career]["cash_table"][cash_index]
    
    # Add some randomness (±20%)
    variation = random.uniform(0.8, 1.2)
    
    return int(base_cash * variation)
