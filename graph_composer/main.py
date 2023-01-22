# Vrindavan sanap
# Based on code https://github.com/kying18/graph-composer


import string 
from graph import Vertex, Graph

def tokenise(text):
    """Returns list of words in small case from given string, removes punctiations"""

    text = ' '.join(text.split())
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    
    return words

with open("hp_sorcerer_stone.txt") as f:
    words = tokenise(f.read())

# words = tokenise("I am a cyber girl in a cyber world")
graph = Graph(words)
print(graph.generate_sentence("the",1000))