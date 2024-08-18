#!/usr/bin/env python3
import random
from collections import namedtuple

Card = namedtuple("Card", "rank suit")
RANKS = [str(n) for n in range(2, 11)] + list("JQKA")
SUITS = "spades diamonds clubs hearts".split()

CARDS = [Card(rank, suit) for suit in SUITS for rank in RANKS]


class Deck:
  def __init__(self, cards = CARDS):
    self._cards = list(cards)

  def __len__(self):
    return len(self._cards)

  def __getitem__(self, i):
    if isinstance(i,slice):
      return Deck(self._cards[i])
    return self._cards[i]
  
  def __add__(self, other):
    return Deck(list(self) + list(other))

  def deal(self, num_players):
    return [self[i::num_players] for i in range(num_players)]

beer_card = Card("7", "Diamonds")
deck = Deck()

"""
Advantages of using special methods to leverage the Python Data
Model
Users of your classes dont have to memorize arbitrary method 
names for standard operations. 
(“How to get the number of items? Is it .size(), .length(), or
what?”)
Its easier to benefit from the rich Python standard library and avoid reinventing
the wheel, like the random.choice function.
"""

# Python supports monkey patching
def put(deck, position, card):
  deck._cards[position] = card

Deck.__setitem__ = put

print(len(deck))
for card in deck[:3]:
  print(card)

random.shuffle(deck)
print(deck[:5])
for card in deck[:3]:
  print(card)

