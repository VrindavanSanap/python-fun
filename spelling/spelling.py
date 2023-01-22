#!/usr/bin/env python3
# Vrindavan Sanap
# Craft assignment 2 part trois
with open ('dict.txt', 'r') as f:
  dict = f.readlines()
  dict = list(map(str.strip, dict))

def check_word(word):
  """checks if the word is valid english word"""
  if word in dict:
    return True
  else:
    return False
def check_sentence(sentence):
  """divice the sentence into words and check if those words are in valid english word"""
  pass

def add_word(word):
  """adds word to dict if not already exits"""

def remove_word(word):
  """removes word from dict"""

def give_incorrect_words(sentece):
  """gives all incorrect words and their incidesfrom the sentence"""

def sentence_accuracy(sentence):
  """gives what % of words in a sentence are spelled correcty"""
 
def fix_word(word):
  """repalces word with its closet pair in the dic"""
 
def fix_sentence(sentence):
   """applies fix_words to all the words in the sentence"""

def foo():
  print("bar")
