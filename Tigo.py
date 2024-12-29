#!/usr/bin/python3
"""
main entry for assistant
"""
"""MAIN ENTRY OF THE PROGRAM HANDLES ALL FUNCTIONALITIES FOR THE AI API"""

########################################################################
#       AN OPEN/GROQ AI CLI INTEGRATION BY NWALI UGONNA EMMANUEL
#       GITHUB: https://github.com/Tigo-cmd/TigoAi
#       All contributions are welcome!!!
#       yea lets do some coding!!!!!!!!!!!!
#########################################################################
"""
####################################################################################################################
Copyright (c) 2024 Emmanuel Tigo, All Rights Reserved
Originally By Nwali Ugonna Emmanuel (Emmanuel Tigo)
###################################################################################################################
"""

import os
from models.source import TigoGroq, load_dotenv
from argparse import ArgumentParser, Namespace
from colorama import Fore, Style, init
from models.controls import pass_gen, clear_screen, extract_filenames
from models.LanguageProcesssing import similarity_comprehension, get_best_match, instruct
from models.helperFunctions import is_exists

load_dotenv()  # typically loads API keys form underlining env file
client = TigoGroq()  # calls groqAPI client

keywords: list[str] = [
    'create a file to do something',
    'analyze a giving error',
    'debug a file with some error to be provided',
    'compile or run a file and print output',
    'explain something',
    'appreciation to show gratitude',
    'commendation on a task done'
]


def interactive_mode() -> None:
    # initialize color for crossPlatform compatibility
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
        print(Fore.MAGENTA + Style.BRIGHT + "Tigo CLI AI Assistant")  # gives te text color magenta
        print(Fore.GREEN + tigo_design)  # gives the tigo design text a green color
        while True:
            user_message: str = input(Fore.YELLOW + "Message 👉 ").strip('\n')
            if "exit" in user_message or "bye" in user_message:
                print(Fore.BLUE + "Tigo 🧒 > ", client.get_response_from_ai(user_message + " 👋.."))
                break
            print(Fore.BLUE + "Tigo 🧒 > ", client.get_response_from_ai(user_message), end="\n")
    except KeyboardInterrupt:
        print("\nProcess interrupted. Exiting...")


def main() -> None:
    # creating an into texts with argparse module
    entry = ArgumentParser(description="Tigo CLI Assistant", prog="Tigo")
    entry.add_argument('-i', '--interactive', type=str, nargs="*", choices=["chat", "start"], help="Runs in "
                                                                                                   "interactive mode")
    entry.add_argument('-p', '--passgen', type=int, nargs='?', metavar="password length", help="password "
                                                                                               "generator")
    entry.add_argument('text', nargs='?', help="enter A text to to do something")
    args: Namespace = entry.parse_args()

    length = args.passgen
    # arguments implementations

    # interactive mode with Tigo
    if args.interactive:
        clear_screen()
        for _ in args.interactive:
            if len(args.interactive) == 0:
                print(args.interactive)
            interactive_mode()

    if args.passgen:
        i = args.passgen
        print(pass_gen() if i is None else pass_gen(i))

    if args.text:
        text = ' '.join(args.text)
        if get_best_match(text, keywords) == keywords[6]:
            print(Fore.YELLOW + "Tigo 🧒 > ", client.get_response_from_ai(text))
        if get_best_match(text, keywords) == keywords[5]:
            print(Fore.LIGHTYELLOW_EX + "Tigo 🧒 > ", client.get_response_from_ai(text))
        if get_best_match(text, keywords) == keywords[4]:
            print(Fore.LIGHTYELLOW_EX + "Tigo 🧒 > ", client.get_response_from_ai(text))
        if get_best_match(text, keywords) == keywords[3]:
            filename = extract_filenames(text)
            if 'run' in text or 'compile' in text:

            if len(filename) == 1:
                print(is_exists(filename[0]))
            else:
                for i in filename:
                    print(is_exists(filename))
        if get_best_match(text, keywords) == keywords[2]:
            filename = client.get_response_from_ai(instruct(text))
            content = is_exists(filename)
            error = f" debug this error {content}"
            print(Fore.LIGHTYELLOW_EX + "Tigo 🧒 > ", client.get_response_from_ai(error))


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")