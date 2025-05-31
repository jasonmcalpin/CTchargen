# Career Generation System

This document explains the career generation system in CTchargen.

## Overview

The career generation system creates realistic Classic Traveller characters with careers, ranks, skills, equipment, and cash. The system is designed to be flexible and extensible, allowing for easy addition of new careers and customization of existing ones.

## Career Data Structure

Each career is defined in the `CAREERS` dictionary in `src/careers.py`. The dictionary has the following structure:

```python
CAREERS = {
    "Career Name": {
        "ranks": [
            "Rank 1",
            "Rank 2",
            # ...
        ],
        "skills": [
            "Skill 1",
            "Skill 2",
            # ...
        ],
        "weapons": [
            "Weapon 1",
            "Weapon 2",
            # ...
        ],
        "equipment": [
            "Equipment 1",
            "Equipment 2",
            # ...
        ],
        "cash_table": [amount1, amount2, ...]
    },
    # More careers...
}
```

### Career Fields

- `ranks`: List of rank titles in order of progression. The index in this list corresponds to the rank level.
- `skills`: List of skills available to this career. Characters will randomly select skills from this list based on their terms served.
- `weapons`: List of weapons available to this career. Characters may be assigned 0-2 weapons from this list.
- `equipment`: List of equipment available to this career. Characters will be assigned 1-3 equipment items from this list.
- `cash_table`: List of cash amounts based on terms served. The index in this list corresponds to the number of terms served (minus 1).

## Available Careers

The system currently includes the following careers:

1. **Navy**: Space navy personnel
   - Ranks: Crewman, Ensign, Lieutenant, Lt Commander, Commander, Captain, Admiral
   - Skills: Pilot, Navigation, Engineering, Gunnery, Computer, Electronics, etc.
   - Weapons: Laser Pistol, Laser Rifle, Cutlass
   - Equipment: Communicator, Computer Terminal, Dress Uniform, Toolkit

2. **Marines**: Space marine personnel
   - Ranks: Private, Lieutenant, Captain, Major, Lt Colonel, Colonel, General
   - Skills: Tactics, Battle Dress, Gunnery, Blade Combat, Gun Combat, etc.
   - Weapons: Assault Rifle, Combat Knife, Grenade Launcher, Laser Rifle
   - Equipment: Combat Armor, Communicator, Survival Kit, Tactical Display

3. **Army**: Planetary ground forces
   - Ranks: Private, Lieutenant, Captain, Major, Lt Colonel, Colonel, General
   - Skills: Gun Combat, Forward Observer, Tactics, Leadership, etc.
   - Weapons: Rifle, Pistol, SMG, Combat Knife
   - Equipment: Flak Jacket, Communicator, Survival Kit, Field Computer

4. **Scouts**: Exploration service
   - Ranks: Scout, Senior Scout, Master Scout
   - Skills: Pilot, Navigation, Engineering, Mechanical, Electronics, etc.
   - Weapons: Rifle, Pistol, Shotgun
   - Equipment: Communicator, Survey Scanner, Survival Kit, Portable Computer

5. **Merchants**: Commercial space traders
   - Ranks: Crewman, 4th Officer, 3rd Officer, 2nd Officer, 1st Officer, Captain
   - Skills: Pilot, Navigation, Engineering, Mechanical, Electronics, etc.
   - Weapons: Pistol, Shotgun
   - Equipment: Communicator, Trade Goods, Merchant ID, Portable Computer

6. **Other**: Civilian or miscellaneous careers
   - Ranks: Civilian
   - Skills: Streetwise, Brawling, Gambling, Carousing, etc.
   - Weapons: Knife, Pistol
   - Equipment: Communicator, Toolkit, Portable Computer

## Career Generation Process

The career generation process involves several steps:

1. **Career Selection**: A random career is selected from the available careers.
2. **Terms Determination**: The character serves 1-4 terms in their career.
3. **Rank Determination**: The character's rank is determined based on their career and terms served.
4. **Skill Acquisition**: The character acquires 1-2 skills per term served, selected from their career's skill list.
5. **Equipment Assignment**: The character is assigned weapons, armor, and equipment based on their career.
6. **Cash Determination**: The character's starting cash is determined based on their career and terms served.

## Functions

The career generation system includes the following functions:

- `generate_career()`: Selects a random career from the available careers.
- `generate_rank(career, terms)`: Determines the character's rank based on their career and terms served.
- `generate_skills(career, terms)`: Assigns skills to the character based on their career and terms served.
- `generate_equipment(career)`: Assigns weapons, armor, and equipment to the character based on their career.
- `generate_cash(career, terms)`: Determines the character's starting cash based on their career and terms served.

## Extending the System

To add a new career to the system:

1. Add a new entry to the `CAREERS` dictionary in `src/careers.py`.
2. Define the career's ranks, skills, weapons, equipment, and cash table.
3. Ensure the career generation functions work with your new career.

Example:

```python
CAREERS["Diplomat"] = {
    "ranks": [
        "Attaché",
        "Third Secretary",
        "Second Secretary",
        "First Secretary",
        "Counselor",
        "Minister",
        "Ambassador"
    ],
    "skills": [
        "Admin",
        "Liaison",
        "Linguistics",
        "Streetwise",
        "Carousing",
        "Bribery",
        "Leadership",
        "Computer",
        "Legal"
    ],
    "weapons": [
        "Pistol",
        "Stunner"
    ],
    "equipment": [
        "Communicator",
        "Diplomatic ID",
        "Formal Attire",
        "Portable Computer"
    ],
    "cash_table": [2000, 5000, 10000, 20000, 30000, 50000, 100000]
}
```

## Integration with Character Generation

The career generation system is integrated with the character generation system in `src/character.py`. The `Character` class includes a method `_generate_career_and_skills()` that uses the career generation functions to create a complete character with a career, skills, equipment, and cash.

## Output

The career information is included in the character output, both in the console preview and in the generated files. The templates in the `templates/` directory have been updated to include the career information.

Example output:

```
Name: Kihrssuoy
UPP: 98BAA6
Gender: Male
Race: Hiver
Age: 30
Career: Navy
Rank: Ensign (Rank 1)
Terms: 3
Skills: Leadership-1, Engineering-1, Tactics-1, Pilot-1
Weapons: Cutlass
Armor: None
Equipment: Dress Uniform, Communicator, Computer Terminal
Cash: 8258 Credits
