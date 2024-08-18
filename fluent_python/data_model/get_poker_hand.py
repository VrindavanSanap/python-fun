#!/usr/bin/env python3
import random

from french_deck import Deck

deck = Deck()
random.shuffle(deck)
while True:
  print(f"There are {len(deck)} cards left in the deck")
  print("Press Enter ⏎ to draw a hand...")
  print("Enter q ⏎ to quit...")
  user_input = input()
  if user_input.lower() == "q":
    break
  hand = deck.draw_cards(5)
  print(hand)
