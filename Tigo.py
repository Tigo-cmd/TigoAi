#!/bin/bash/python3
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

from models.source import TigoGroq, load_dotenv, find_patterns
from argparse import ArgumentParser, Namespace

load_dotenv()  # typically loads API keys form underlining env file
client = TigoGroq()  # calls groqAPI client

# entry = ArgumentParser()
#
# entry.add_argument("")

message = input(">")
pattern = "create"


@find_patterns
def printOut():
    print(message, pattern)


printOut(message, pattern)
