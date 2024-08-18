#!/usr/bin/env python3
import random
from collections import namedtuple

Card = namedtuple("Card", "rank suit")
RANKS = [str(n) for n in range(2, 11)] + list("JQKA")
SUITS = "spades diamonds clubs hearts".split()
SUIT_SYMBOLS = {"spades": "♠", "diamonds": "♦", "clubs": "♣", "hearts": "♥"}

CARDS = [Card(rank, suit) for suit in SUITS for rank in RANKS]


class Deck:
  def __init__(self, cards=CARDS):
    self._cards = list(cards)

  def __len__(self):
    return len(self._cards)

  def __getitem__(self, i):
    if isinstance(i, slice):
      return Deck(self._cards[i])
    return self._cards[i]

  def __add__(self, other):
    return Deck(list(self) + list(other))

  def deal(self, num_players):
    return [self[i::num_players] for i in range(num_players)]

  def draw_cards(self, num_cards):
    if num_cards > len(self._cards):
      raise ValueError("Not enough cards in the deck")
    return Deck([self._cards.pop() for _ in range(num_cards)])

  def __repr__(self):
    len_ = len(self)
    if len_ <= 5:
      cards_str = ", ".join(f"{card.rank} {SUIT_SYMBOLS[card.suit]}" for card in self._cards)
      return f"Deck of {len(self)} cards: [{cards_str}]"
    else:
      return f"Deck of {len(self)} cards"


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


if __name__ == "__main__":
  print(len(deck))
  for card in deck[:3]:
    print(card)
  random.shuffle(deck)
  print(deck[:5])
  for card in deck[:3]:
    print(card)
  print(deck.deal(2))
