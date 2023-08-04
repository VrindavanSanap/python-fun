#!/usr/bin/python3
import collections
from random import choice

Card = collections.namedtuple("Card", ["rank", "suit"])

class French_deck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
    
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = French_deck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

ace_of_spades = Card("A", "spades")
jack_of_clubs = Card("J", "clubs")
print(spades_high(ace_of_spades))
print(spades_high(jack_of_clubs))

deck = French_deck()

for card in sorted(deck, key=spades_high):
    print(card)