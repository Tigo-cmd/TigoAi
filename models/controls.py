"""
handles some addition functions
"""

import os
import platform
from typing import Callable
from colorama import Fore, Style, init
from string import ascii_letters, digits, punctuation
from secrets import choice
import re


def clear_screen() -> None:
    """
    just to clear the screen of the terminal so cool 😀
    :return: nothing
    """
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system('clear -x')


def extract_filenames(text):
    # Define the updated regex pattern to match more complex filenames
    pattern = r'\b[\w\.-]+(?:\.[a-zA-Z0-9]+)\b'

    # Use re.findall() to find all occurrences of filenames in the text
    filenames = re.findall(pattern, text)

    return filenames


def pass_gen(length: int = 16) -> str:
    """
    just added some sweet password gen functionality just to spice up this tool
    cool right? I know! 😀😀

    :param length: length of the password.
    :return:  password generated
    """
    passGen: Callable[[int], str] = lambda x: ''.join(choice(ascii_letters + digits + punctuation) for _ in range(x))

    return passGen(length)

