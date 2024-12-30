#!/usr/bin/python3
"""
main entry for assistant
"""
import argparse

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

import asyncio
from models.source import TigoGroq, load_dotenv
from argparse import ArgumentParser, Namespace
from colorama import Fore, Style, init
from models.controls import pass_gen, clear_screen, extract_filenames, run_file, extract_code
from models.LanguageProcesssing import similarity_comprehension, get_best_match, instruct
from models.helperFunctions import is_exists, file_exec

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


async def interactive_mode() -> None:
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
                print(Fore.BLUE + "Tigo 🧒 > ", await client.get_response_from_ai(user_message + " 👋.."))
                break
            print(Fore.BLUE + "Tigo 🧒 > ", await client.get_response_from_ai(user_message), end="\n")
    except KeyboardInterrupt:
        print("\nProcess interrupted. Exiting...")


async def main() -> None:
    # creating an into texts with argparse module
    entry = ArgumentParser(description="Tigo CLI Assistant", prog="Tigo")
    entry.add_argument('-i', '--interactive', type=str, nargs="*", choices=["chat", "start"], help="Runs in "
                                                                                                   "interactive mode")
    entry.add_argument('-p', '--passgen', type=int, nargs='?', metavar="password length", help="password "
                                                                                               "generator")
    entry.add_argument('text', nargs=argparse.REMAINDER, help="enter A text to to do something")
    args: Namespace = entry.parse_args()

    length = args.passgen
    # arguments implementations

    # interactive mode with Tigo
    if args.interactive:
        clear_screen()
        for _ in args.interactive:
            if len(args.interactive) == 0:
                print(args.interactive)
            await interactive_mode()

    if args.passgen:
        i = args.passgen
        print(pass_gen() if i is None else pass_gen(i))

    # process natural text from user
    if args.text:
        text = ' '.join(args.text)

        # Asynchronously get the best match
        best_match = await get_best_match(text, keywords)

        if best_match == keywords[6]:
            print(Fore.YELLOW + "Tigo 🧒 > ", await client.get_response_from_ai(text))
        elif best_match == keywords[5]:
            print(Fore.LIGHTYELLOW_EX + "Tigo 🧒 > ", await client.get_response_from_ai(text))
        elif best_match == keywords[4]:
            print(Fore.LIGHTYELLOW_EX + "Tigo 🧒 > ", await client.get_response_from_ai(text))
        elif best_match == keywords[3]:
            filename = extract_filenames(text)
            if 'run' in text.lower():
                for i in filename:
                    run_file(i)
            if len(filename) == 1:
                print(Fore.GREEN + 'Files contents 👍 > ', end="")
                print(is_exists(filename[0]))
            else:
                for i in filename:
                    print(is_exists(i))
        elif best_match == keywords[2]:
            filename = extract_filenames(text)
            if len(filename) == 1:
                content = is_exists(filename[0])
                if 'line' in text.lower():
                    error = f" debug this error {text} {content}"
                    print(Fore.LIGHTYELLOW_EX + "Tigo 🧒 > ", await client.get_response_from_ai(error))
                else:
                    error = f" debug this error {text} {content}"
                    print(Fore.LIGHTYELLOW_EX + "Tigo 🧒 > ", await client.get_response_from_ai(error))
            else:
                for i in filename:
                    content = is_exists(i)
                    if 'line' in text.lower():
                        error = f" debug this error {text} {content}"
                        print(Fore.LIGHTYELLOW_EX + "Tigo 🧒 > ", await client.get_response_from_ai(error))
                    else:
                        error = f" debug this error {text} {content}"
                        print(Fore.LIGHTYELLOW_EX + "Tigo 🧒 > ", await client.get_response_from_ai(error))
        elif best_match == keywords[0]:
            response = await client.get_response_from_ai(text)
            print(response)
            details = extract_code(response)
            print(details['code'])
            filename = extract_filenames(details['file_name'])
            print(filename)
            if not filename:
                filename = extract_filenames(response)
            if len(filename) == 1:
                file_exec(filename[0], details['code'])
            else:
                for i in range(0, len(filename)):
                    file_exec(filename[i], details['code'][i])


if __name__ == '__main__':
    try:
        # Run the main function asynchronously
        asyncio.run(main())
        print("Done!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
