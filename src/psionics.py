"""
Psionics module for CTchargen.

This module handles psionic abilities for Classic Traveller characters.
"""

import random
from typing import Dict, List, Any, Optional, Tuple

from src.lib import stellagama as sg


# Psionic talents
PSIONIC_TALENTS = {
    "Telepathy": {
        "description": "The ability to read or influence the thoughts of others.",
        "levels": [
            "Life Detection",
            "Telempathy",
            "Read Surface Thoughts",
            "Read Deep Thoughts",
            "Assault",
            "Shield",
            "Send Thoughts",
            "Probe",
            "Assault Shield"
        ]
    },
    "Clairvoyance": {
        "description": "The ability to sense events at a distance.",
        "levels": [
            "Sense",
            "Tactical Awareness",
            "Clairvoyance",
            "Clairaudience",
            "Clairsentience",
            "Teleolocation"
        ]
    },
    "Telekinesis": {
        "description": "The ability to move objects with the mind.",
        "levels": [
            "Telekinetic Punch",
            "Telekinetic Grab",
            "Telekinetic Move",
            "Telekinetic Crush",
            "Telekinetic Shield"
        ]
    },
    "Awareness": {
        "description": "The ability to control one's own body.",
        "levels": [
            "Suspended Animation",
            "Enhanced Awareness",
            "Enhanced Strength",
            "Enhanced Endurance",
            "Regeneration",
            "Psionically Enhanced Strength",
            "Psionically Enhanced Endurance",
            "Body Weaponry",
            "Body Armor"
        ]
    },
    "Teleportation": {
        "description": "The ability to move instantly from one place to another.",
        "levels": [
            "Teleport Object",
            "Teleport Self",
            "Teleport Others",
            "Teleport Assault"
        ]
    },
    "Special": {
        "description": "Rare and unusual psionic abilities.",
        "levels": [
            "Pyrokinesis",
            "Cryokinesis",
            "Electrokinesis",
            "Photokinesis",
            "Probability Manipulation",
            "Precognition",
            "Retrocognition",
            "Astral Projection"
        ]
    }
}


def check_psionic_potential(age: int) -> bool:
    """
    Check if a character has psionic potential.
    
    Args:
        age: Character's age
        
    Returns:
        bool: True if the character has psionic potential, False otherwise
    """
    # Base target number is 9+
    target = 9
    
    # Apply age penalties
    if age >= 50:
        target += 2  # -2 penalty
    elif age >= 30:
        target += 1  # -1 penalty
    
    # Roll 2D6
    roll = sg.dice(2, 6)
    
    return roll >= target


def generate_psr() -> int:
    """
    Generate a Psionic Strength Rating (PSR).
    
    Returns:
        int: PSR value (2-12)
    """
    return sg.dice(2, 6)


def check_psionic_training() -> bool:
    """
    Check if a character receives psionic training.
    
    Returns:
        bool: True if the character receives training, False otherwise
    """
    # Target number is 8+
    target = 8
    
    # Roll 2D6
    roll = sg.dice(2, 6)
    
    return roll >= target


def reduce_psr(psr: int) -> int:
    """
    Reduce PSR due to lack of training.
    
    Args:
        psr: Current PSR value
        
    Returns:
        int: Reduced PSR value
    """
    reduction = sg.dice(1, 6)
    new_psr = psr - reduction
    
    return max(0, new_psr)


def get_available_talents(psr: int) -> int:
    """
    Determine the number of available talents based on PSR.
    
    Args:
        psr: PSR value
        
    Returns:
        int: Number of available talents
    """
    if psr <= 5:
        return 1
    elif psr <= 8:
        return 2
    elif psr <= 11:
        return 3
    else:
        return 4


def select_talents(psr: int, num_talents: int) -> List[str]:
    """
    Select random psionic talents.
    
    Args:
        psr: PSR value
        num_talents: Number of talents to select
        
    Returns:
        List[str]: Selected talents
    """
    available_talents = list(PSIONIC_TALENTS.keys())
    selected_talents = []
    
    for _ in range(min(num_talents, len(available_talents))):
        talent = random.choice(available_talents)
        selected_talents.append(talent)
        available_talents.remove(talent)
    
    return selected_talents


def generate_psionic_abilities(age: int) -> Dict[str, Any]:
    """
    Generate psionic abilities for a character.
    
    Args:
        age: Character's age
        
    Returns:
        Dict[str, Any]: Psionic abilities data
    """
    # Check for psionic potential
    has_potential = check_psionic_potential(age)
    
    if not has_potential:
        return {
            "has_psionic": False,
            "psr": 0,
            "is_trained": False,
            "talents": []
        }
    
    # Generate PSR
    psr = generate_psr()
    
    # Check for training
    is_trained = check_psionic_training()
    
    if not is_trained:
        # Reduce PSR due to lack of training
        psr = reduce_psr(psr)
        
        if psr == 0:
            return {
                "has_psionic": False,
                "psr": 0,
                "is_trained": False,
                "talents": []
            }
    
    # Determine available talents
    num_talents = get_available_talents(psr)
    
    # Select talents
    talents = select_talents(psr, num_talents) if is_trained else []
    
    return {
        "has_psionic": True,
        "psr": psr,
        "is_trained": is_trained,
        "talents": talents
    }
