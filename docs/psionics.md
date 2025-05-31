# Psionic System Documentation

This document explains the psionic system in CTchargen.

## Overview

The psionic system implements Classic Traveller's rules for psionic abilities. Characters have a chance to possess psionic potential, which diminishes with age. If they have potential, they may receive training at a Psionic Institute, which allows them to develop psionic talents.

## Psionic Generation Process

The psionic generation process follows these steps:

1. **Check for Psionic Potential**: Roll 2D6 against a target number of 9+, with penalties for age.
2. **Generate Psionic Strength Rating (PSR)**: If the character has psionic potential, roll 2D6 for their PSR.
3. **Check for Psionic Training**: Roll 2D6 against a target number of 8+ to see if the character receives training.
4. **Determine Available Talents**: If trained, determine the number of available talents based on PSR.
5. **Select Talents**: Randomly select talents from the available options.

## Psionic Potential

The chance of having psionic potential is determined by a roll of 2D6 against a target number of 9+, with the following age penalties:

- No penalty for characters under 30
- -1 penalty for characters aged 30-49
- -2 penalty for characters aged 50+

If the roll fails, the character has no psionic potential.

## Psionic Strength Rating (PSR)

If a character has psionic potential, their Psionic Strength Rating (PSR) is determined by rolling 2D6. This rating determines the strength and number of talents available to the character.

## Psionic Training

Characters with psionic potential must roll 2D6 against a target number of 8+ to see if they receive training at a Psionic Institute. If the roll fails, their PSR is reduced by 1D6. If their PSR drops to 0, all psionic potential is lost.

## Available Talents

The number of available talents depends on the character's PSR:

- PSR 1-5: 1 talent
- PSR 6-8: 2 talents
- PSR 9-11: 3 talents
- PSR 12+: 4 talents

## Psionic Talents

The system includes the following psionic talents:

### Telepathy

The ability to read or influence the thoughts of others.

- Life Detection
- Telempathy
- Read Surface Thoughts
- Read Deep Thoughts
- Assault
- Shield
- Send Thoughts
- Probe
- Assault Shield

### Clairvoyance

The ability to sense events at a distance.

- Sense
- Tactical Awareness
- Clairvoyance
- Clairaudience
- Clairsentience
- Teleolocation

### Telekinesis

The ability to move objects with the mind.

- Telekinetic Punch
- Telekinetic Grab
- Telekinetic Move
- Telekinetic Crush
- Telekinetic Shield

### Awareness

The ability to control one's own body.

- Suspended Animation
- Enhanced Awareness
- Enhanced Strength
- Enhanced Endurance
- Regeneration
- Psionically Enhanced Strength
- Psionically Enhanced Endurance
- Body Weaponry
- Body Armor

### Teleportation

The ability to move instantly from one place to another.

- Teleport Object
- Teleport Self
- Teleport Others
- Teleport Assault

### Special

Rare and unusual psionic abilities.

- Pyrokinesis
- Cryokinesis
- Electrokinesis
- Photokinesis
- Probability Manipulation
- Precognition
- Retrocognition
- Astral Projection

## Character Data Structure

Psionic information is stored in the character's `psionic` attribute, which is a dictionary with the following keys:

- `has_psionic`: Boolean indicating whether the character has psionic abilities
- `psr`: Psionic Strength Rating (0-12)
- `is_trained`: Boolean indicating whether the character has received psionic training
- `talents`: List of psionic talents

## Output

Psionic information is included in the character output, both in the console preview and in the generated files. The templates in the `templates/` directory have been updated to include psionic information.

Example output:

```
Name: Ghush
UPP: 4774AC
Gender: Female
Race: Vilani
Age: 22
Career: Other
Rank: Civilian (Rank 0)
Terms: 1
Status: Deceased (died during service)
Skills: Medical-1, Gambling-1
Weapons: Pistol
Armor: 
Equipment: Toolkit, Toolkit
Cash: 1197 Credits
Psionics: PSR 6 (Trained) - Talents: Special, Clairvoyance
```

## Functions

The psionic system includes the following functions:

- `check_psionic_potential(age)`: Check if a character has psionic potential based on their age
- `generate_psr()`: Generate a Psionic Strength Rating (PSR)
- `check_psionic_training()`: Check if a character receives psionic training
- `reduce_psr(psr)`: Reduce PSR due to lack of training
- `get_available_talents(psr)`: Determine the number of available talents based on PSR
- `select_talents(psr, num_talents)`: Select random psionic talents
- `generate_psionic_abilities(age)`: Generate complete psionic abilities for a character

## Integration with Character Generation

The psionic system is integrated with the character generation system in `src/character.py`. The `Character` class includes a method `_generate_psionic_abilities()` that uses the psionic generation functions to create psionic abilities for the character.
