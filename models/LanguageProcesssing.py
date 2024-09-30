"""
this module will handle all patterns and language processing to enable other models understand
the users intent.
e.g: create, update, debug ETC......
such as text similarities, actions etc.
"""
import spacy
from TigoAi.models import keywords


nlp = spacy.load("en_core_web_lg")
w1 = nlp.vocab["create"]
w2 = nlp.vocab[""]


print(w1.similarity(w2))