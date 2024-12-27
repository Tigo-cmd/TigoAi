"""
this module will handle all patterns and language processing to enable other models understand
the users intent.
e.g: create, update, debug ETC......
such as text similarities, actions etc.
"""
import spacy
from TigoAi.models import keywords


nlp = spacy.load("en_core_web_lg")
w1 = nlp.vocab["create a file to do someth"]
w2 = nlp.vocab["create a python file to get api from a Model"]


print(w1.similarity(w2))