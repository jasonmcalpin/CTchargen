
<p align="center">

  <h3 align="center">CTchargen</h3>

  <p align="center">
    Generate a list of Classic Traveller characters.
    <br>
    <br>
    <a href="https://github.com/jasonmcalpin/CTchargen.git">Clone</a>
    ·
    <a href="https://github.com/jasonmcalpin/CTchargen/compare/templated?expand=1">Pull Requests</a>
  </p>
</p>

<br>

## Table of contents

- [Quick start](#quick-start)
- [Status](#status)
- [What's included](#whats-included)
- [Bugs and feature requests](#bugs-and-feature-requests)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [Community](#community)
- [Versioning](#versioning)
- [Creators](#creators)
- [Copyright and license](#copyright-and-license)

## Quick start

Several quick start options are available:

- `python chargen.py` to generate a character
- `python chargen.py -c ##` to generate ## number of characters
- `python chargen.py -s filename` to generate the character to a file
- `python chargen.py -s filename -c ##` to generate ## number of characters to a file
- `python chargen.py -s filename -c ## -t mycharactersheet` to generate ## number of characters to a file using the template file `mycharactersheet.template` that you put into the template folder.


## Status
[![star this repo](http://githubbadges.com/star.svg?user=jasonmcalpin&repo=CTchargen&style=default)](https://github.com/jasonmcalpin/node_starter)
[![fork this repo](http://githubbadges.com/fork.svg?user=jasonmcalpin&repo=CTchargen&style=default)](https://github.com/jasonmcalpin/node_starter/fork)


## What's included

Within this repo you'll find the following folders and files:

```
CTchargen/
├── templates/                   - The location of all of the template files for the generator.
│    ├── markdown.template       - A markdown template file
│    └── text.template           - A generic template file
│
├── femalenames.txt              - female names
├── malenames.txt                - male names
├── surnames.txt                 - list of last names
├── README.md                    - This file
├── stellagama.py                - General game functions
└── chargen.py                   - main generator file.
```


## Bugs and feature requests




## Documentation

This project is an expansion of a project started by Omer Golan-Joel. This version includes commandline arguments and  expanded output options. The format of the output has been moved to template files that are in the template folder. This will allow you to add any format you need for your own games to that folder without having to wait. The syntex of the templates is very simple.

To get help for what options are available you from the command line you can use `--help`.

The following commands are available.
```
usage: chargen.py [-h] [-c CHAR] [-s SAVE] [-t TEMPLATE]

Create Traveller characters. They will be posted to a file or the screen.

optional arguments:
  -h, --help            show this help message and exit
  -c CHAR, --char CHAR  Number of characters to generate.
  -s SAVE, --save SAVE  Save characters to this file name.
  -t TEMPLATE, --template TEMPLATE
                        Template name without the .template extension or
                        spaces in name. Default is text.
```

## Contributing

You can fork the project and commit a pull request with the new feature.


## Community

Get updates on DPI development and chat with the project maintainers and community members.

- Slack [#docker-project-init](https://oiny.slack.com/messages/CAV1X5N5U/details/).


## Versioning

0.5, July 30th, 2018
Template system added
psionic talents added
birth world added (placeholder)
discharge world added (placeholder)
alien race names added ( No modification to name, stats, or skills yet. this is a placeholder)


0.4, April 12th, 2018
All careers added
Rank skills added

0.3, April 9th, 2018
Cascade skills added
"Cascade" equipment added (gun and melee types)
Noble title are now by sex

0.2, April 9th, 2018
Army career finalized
Mustering out benefits added

0.15, April 6th, 2018
Improved the chargen loop and skill acquision
Implemented the Marines career
Implemented a more traditional character output format
Characters now have names and surnames randomly chosen from an external file
Implemented noble titles

0.1, April 6th, 2018
Returned to dictionaries for the career data structure, works perfectly.
Baseline career loop created. It still lacks mustering out and only uses the Service skill table, but starts generating something remotely resembling a Traveller character,
Careers are mock-up; all use Navy stats except for their names. To be changed later.

0.03, April 6th, 2018
Implemented the Named Tuple career data structure.

0.02, April 5th, 2018
Still extremely partial, but improved the data structure. The character will now be an object; I'll later add the careers as Named Tuples.

0.01, March 30th, 2018
Very early and very partial code. Includes several relevant functions, the career and character data structures, and the very beginning of the character object and the main character generation function.


## Creators
**By Omer Golan-Joel**
golan2072@gmail.com


**Jason McAlpin**
- <https://twitter.com/jasonmcalpin>
- <https://github.com/jasonmcalpin>

## Copyright and license
This code is open-source


