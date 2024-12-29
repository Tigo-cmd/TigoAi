"""
this module will handle all patterns and language processing to enable other models understand
the users intent.
e.g: create, update, debug ETC......
such as text similarities, actions etc.
"""
import spacy
from typing import List

# Declare a global variable for the spaCy model
nlp = None


# Lazy load the spaCy model when needed
def get_spacy_model():
    global nlp
    if nlp is None:
        nlp = spacy.load("en_core_web_lg")
    return nlp

# Define the predefined command templates
# commands = [
#     'create a file to do something',
#     'analyze a giving error',
#     'debug a file with some error to be provided',
#     'compile or run a file and print output',
#     'explain something',
# ]


def instruct(text):
    return (f"From this text \"{text}\",I want you to look for the name of the file being discussed "
            f"and return "
            f"just the name of the file with its extension. "
            f"Do not include any other words. For example,"
            f" in the sentence Please open file document.txt you should return just 'document.txt'.")


# Function to get the best match command
async def get_best_match(user_input: str, commands: list[str]) -> str:
    # Process the user input with spaCy
    nlp_load = get_spacy_model()
    user_doc = nlp_load(user_input)

    # Store similarities
    best_similarity = 0
    best_match = None

    # Compare user input to each command template
    for command in commands:
        # Process each command template with spaCy
        command_doc = nlp_load(command)

        # Calculate similarity between user input and the command
        similarity = user_doc.similarity(command_doc)

        # Check if the similarity is the best so far
        if similarity > best_similarity:
            best_similarity = similarity
            best_match = command

    return best_match


async def similarity_comprehension(text1: str, text2: str) -> float:
    """
    uses spacy to compare similarities and returns the average or percentage of confidence
    :param text1: first text to be compared
    :param text2: second text to be compared
    :return: percentage of similarity confidence
    """
    nlpl = get_spacy_model()
    text1 = nlpl(text1)
    text2  = nlpl(text2)
    return text1.similarity(text2)


# async def compare_verbs(text1: str, text2: str) -> float:
#     """
#     for more confidence and comparison I'd check for verbs also and this function handles
#     :param text1: first text to extract verb and compare
#     :param text2: second text to extract verb and compare
#     :return: float
#     """
#     nlpl = get_spacy_model()
#     text1 = nlpl(text1)
#     text2 = nlpl(text2)
#
#     verb1 = " ".join([token.lemma_ for token in text1 if token.pos_ == "VERB"])
#     verb2 = " ".join([token.lemma_ for token in text2 if token.pos_ == "VERB"])
#     return nlpl(verb1).similarity(nlpl(verb2))


# async def compare_noun(text1: str, text2: str) -> float:
#     """
#     for more confidence and comparison I'd check for verbs also and this function handles
#     :param text1: first text to extract verb and compare
#     :param text2: second text to extract verb and compare
#     :return: float
#     """
#     nlpl = get_spacy_model()
#     text1 = nlpl(text1)
#     text2 = nlpl(text2)
#
#     noun1 = " ".join([token.lemma_ for token in text1 if token.pos_ == "NOUN"])
#     noun2 = " ".join([token.lemma_ for token in text2 if token.pos_ == "NOUN"])
#     return nlpl(noun1).similarity(nlpl(noun2))

# # Test with a user input
# user_input = "define love and give examples"
# matched_command = get_best_match(user_input, commands)
#
# print(f"Matched Command: {matched_command}")
