"""
Stellagama utility module.

A module with various useful functions by Omer Golan-Joel.
This is open source code, feel free to use it for any purpose.

v3.0 - May 30th, 2025 - Updated for CTchargen refactoring
"""

import random
import string
import os
import platform
from typing import List, Any, Optional, Union


def yn() -> str:
    """
    Simple yes or no prompt filtering invalid results.
    
    Returns:
        str: "yes" or "no"
    """
    while True:
        answer = input("Y/N: ")
        if answer.lower() == "y":
            return "yes"
        if answer.lower() == "n":
            return "no"
        print("Invalid Answer")


def random_choice(items: List[Any]) -> Any:
    """
    Randomly chooses an element from a list.
    
    Args:
        items: List of items to choose from
        
    Returns:
        Any: Randomly selected element
    """
    return items[random.randint(0, len(items) - 1)]


def dice(n: int, sides: int) -> int:
    """
    Dice-roller.
    
    Args:
        n: Number of dice
        sides: Number of sides per die
        
    Returns:
        int: Sum of dice rolls
    """
    roll = 0
    for _ in range(n):
        roll += random.randint(1, sides)
    return roll


def pseudo_hex(num: int) -> Union[int, str]:
    """
    Converts numbers to Cepheus Engine "Pseudo-Hex".
    
    Args:
        num: Number to convert
        
    Returns:
        Union[int, str]: Pseudo-hex representation
    """
    num = int(num)
    code = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F", "G", "H", 
            "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    return code[num]


def current_dir() -> List[str]:
    """
    Lists the current directory's contents on Windows or Linux.
    
    Returns:
        List[str]: Directory contents
    """
    if platform.system() == "Windows":
        return os.listdir(".\\")
    else:
        return os.listdir(os.getcwd())


def check_file_exists(check_file: str) -> bool:
    """
    Checks if a file exists in the directory.
    
    Args:
        check_file: Filename to check
        
    Returns:
        bool: True if file exists, False otherwise
    """
    return check_file in os.listdir()


def savefile(extension: str) -> str:
    """
    File-saving function.
    
    Args:
        extension: File extension
        
    Returns:
        str: Filename with extension
    """
    filename = str(input("Please enter file name to generate: "))
    filecheck = filename + "." + extension
    
    if check_file_exists(filecheck):
        print(" ")
        print("File already exists. Overwrite?")
        overwrite = yn()
        if overwrite == "no":
            filename = input("Please enter new file name to generate: ")
    
    return filename + "." + extension


def clear_screen() -> None:
    """Clear screen function."""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def random_line(filename: str) -> str:
    """
    Randomly chooses a line from a text file.
    
    Args:
        filename: Path to text file
        
    Returns:
        str: Randomly chosen line
    """
    with open(filename, "r") as line_list:
        line = random_choice(line_list.readlines())
        line = line.strip()
    return line


class Getch:
    """
    Gets a single character from standard input.
    Does not echo to the screen.
    """
    def __init__(self):
        try:
            self.impl = GetchWindows()
        except ImportError:
            self.impl = GetchUnix()
            
    def __call__(self):
        return self.impl()


class GetchUnix:
    """Unix implementation of getch."""
    def __init__(self):
        import tty, sys
            
    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
        

class GetchWindows:
    """Windows implementation of getch."""
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


def getkeypress() -> str:
    """
    Reads a single keypress.
    
    Returns:
        str: Key pressed
    """
    if platform.system() == "Windows":
        key = Getch()
        return key().decode()
    else:
        key = Getch()
        return key()


def list_stringer(input_list: List[Any]) -> str:
    """
    Converts a list to a string.
    
    Args:
        input_list: List to convert
        
    Returns:
        str: Space-separated string of list items
    """
    output_list = []
    for item in input_list:
        output_list.append(str(item))
    return ' '.join(output_list)
