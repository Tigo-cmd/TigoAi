"""
this module will handle all patterns and language processing to enable other models understand
the users intent.
e.g: create, update, debug ETC......
such as text similarities, actions etc.
"""
import spacy
import os
nlp = spacy.load("en_core_web_lg")  # loads the language vocabulary for similarity and comprehension


# Define the predefined command templates
# commands = [
#     'create a file to do something',
#     'analyze a giving error',
#     'debug a file with some error to be provided',
#     'compile or run a file and print output',
#     'explain something',
# ]


# Function to get the best match command
def get_best_match(user_input: str, commands: list[str]) -> str:
    # Process the user input with spaCy
    user_doc = nlp(user_input)

    # Store similarities
    best_similarity = 0
    best_match = None

    # Compare user input to each command template
    for command in commands:
        # Process each command template with spaCy
        command_doc = nlp(command)

        # Calculate similarity between user input and the command
        similarity = user_doc.similarity(command_doc)

        # Check if the similarity is the best so far
        if similarity > best_similarity:
            best_similarity = similarity
            best_match = command

    return best_match


def similarity_comprehension(text1: str, text2: str) -> float:
    """
    uses spacy to compare similarities and returns the average or percentage of confidence
    :param text1: first text to be compared
    :param text2: second text to be compared
    :return: percentage of similarity confidence
    """
    text1: nlp = nlp(text1)
    text2: nlp = nlp(text2)
    return text1.similarity(text2)


def compare_verbs(text1: str, text2: str) -> float:
    """
    for more confidence and comparison I'd check for verbs also and this function handles
    :param text1: first text to extract verb and compare
    :param text2: second text to extract verb and compare
    :return: float
    """
    text1: nlp = nlp(text1)
    text2: nlp = nlp(text2)

    verb1 = " ".join([token.lemma_ for token in text1 if token.pos_ == "VERB"])
    verb2 = " ".join([token.lemma_ for token in text2 if token.pos_ == "VERB"])
    return nlp(verb1).similarity(nlp(verb2))


def compare_noun(text1: str, text2: str) -> float:
    """
    for more confidence and comparison I'd check for verbs also and this function handles
    :param text1: first text to extract verb and compare
    :param text2: second text to extract verb and compare
    :return: float
    """
    text1: nlp = nlp(text1)
    text2: nlp = nlp(text2)

    noun1 = " ".join([token.lemma_ for token in text1 if token.pos_ == "NOUN"])
    noun2 = " ".join([token.lemma_ for token in text2 if token.pos_ == "NOUN"])
    return nlp(noun1).similarity(nlp(noun2))


# # Test with a user input
# user_input = "define love and give examples"
# matched_command = get_best_match(user_input, commands)
#
# print(f"Matched Command: {matched_command}")
