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

from models.source import TigoGroq, load_dotenv
from argparse import ArgumentParser, Namespace
from TigoAi.models.controls import pass_gen
# initialize color for crossPlatform compatibility


load_dotenv()  # typically loads API keys form underlining env file
client = TigoGroq()  # calls groqAPI client


def main() -> None:

    # creating an into texts with argparse module
    entry = ArgumentParser(description="Tigo CLI Assistant", prog="Tigo")
    entry.add_argument('-i', '--interactive', type=str, nargs="*", choices=["chat", "start"], help="Runs in "
                                                                                                   "interactive mode")
    entry.add_argument('-p', '--passgen', type=int, nargs='?', metavar="password length", help="password generator")
    args: Namespace = entry.parse_args()

    length = args.passgen
# arguments implementations

    # interactive mode with Tigo
    if args.interactive:
        for _ in args.interactive:
            if len(args.interactive) == 0:
                print(args.interactive)
            interactive_mode()

    # password generator
    if args.passgen:
        i = args.passgen
        print(pass_gen(i if i is not None else 16))


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
