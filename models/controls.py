"""
handles some addition functions
"""

import os
import platform
from typing import Callable
from colorama import Fore, Style, init
from string import ascii_letters, digits, punctuation
from secrets import choice


def clear_screen() -> None:
    """
    just to clear the screen of the terminal so cool 😀
    :return: nothing
    """
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system('clear -x')


def pass_gen(length: int = 16) -> str:
    """
    just added some sweet password gen functionality just to spice up this tool
    cool right? I know! 😀😀

    :param length: length of the password.
    :return:  password generated
    """
    default = 12
    passGen: Callable[[int], str] = lambda x: ''.join(choice(ascii_letters + digits + punctuation) for _ in range(x))

    return passGen(length)


def interactive_mode() -> None:
    init(autoreset=True)

    """for interactive mode with Tigo"""
    try:
        tigo_design: str = '''
          TTTTT  III   GGGG     OOOO
            T     I  G         O    O
            T     I  G   GG    O    O
            T     I  G     G   O    O
            T    III   GGGG     OOOO
        '''
        print(Fore.MAGENTA + Style.BRIGHT + "Tigo CLI AI Assistant")
        print(Fore.GREEN + tigo_design)
        while True:
            user_message: str = input("Message > ")
            if "exit" in user_message:
                print(Fore.BLUE + "Tigo 🧒 > ", client.get_response_from_ai(user_message + " 👋.."))
                break
            print(Fore.BLUE + "Tigo 🧒 > ", client.get_response_from_ai(user_message))
    except KeyboardInterrupt:
        print("\nProcess interrupted. Exiting...")


