#!/usr/bin/env python3
import random
from collections import namedtuple
from collections.abc import MutableSequence

Card = namedtuple("Card", "rank suit")
RANKS = [str(n) for n in range(2, 11)] + list("JQKA")
SUITS = "spades diamonds clubs hearts".split()
SUIT_SYMBOLS = {"spades": "♠", "diamonds": "♦", "clubs": "♣", "hearts": "♥"}

CARDS = [Card(rank, suit) for suit in SUITS for rank in RANKS]


class Deck(MutableSequence):
  def __init__(self, cards=CARDS):
    self._cards = list(cards)

  def __len__(self):
    return len(self._cards)

  def __getitem__(self, index):
    if isinstance(index, slice):
      return Deck(self._cards[index])
    return self._cards[index]

  def __setitem__(self, index, cards):
    if isinstance(index, slice):
      if all(isinstance(card, Card) for card in cards):
        self._cards[index] = cards
      else:
        raise ValueError("All assigned values must be Card instances")
    elif isinstance(cards, Card):
      self._cards[index] = cards
    else:
      raise ValueError("Assigned value must be a Card instance")

  def __delitem__(self, index):
    del self._cards[index]

  def insert(self, index, value):
    if not isinstance(value, Card):
      raise ValueError("Inserted value must be a Card instance")
    self._cards.insert(index, value)

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


if __name__ == "__main__":
  print(len(deck))
  for card in deck[:3]:
    print(card)
  random.shuffle(deck)
  print(deck[:5])
  for card in deck[:3]:
    print(card)
  print(deck.deal(2))
