"""
handles some addition functions
"""

import os
import subprocess
import platform
from typing import Callable
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


def run_file(filename):
    # List of common file extensions and the corresponding commands to run them
    file_extensions = {
        '.py': 'python',
        '.java': 'javac',  # Compile using javac (for Java files)
        '.js': 'node',  # Node.js for JavaScript files
        '.html': 'start',  # Open HTML in default browser (Windows-specific, change for your OS)
        '.css': 'start',  # Open CSS in default browser (Windows-specific, change for your OS)
        '.sh': 'bash',  # For shell scripts
        '.c': 'gcc',  # C compiler
        '.cpp': 'g++',  # C++ compiler
        '.exe': '',  # Executable files (no need to run, directly executed on the system)
    }

    # Extract file extension
    file_extension = os.path.splitext(filename)[1].lower()

    # Check if extension is supported
    if file_extension in file_extensions:
        command = file_extensions[file_extension]
        print(f"Running file: {filename}")
        subprocess.run([command, filename], check=True)
    else:
        print(f"Unsupported file extension: {file_extension}")


