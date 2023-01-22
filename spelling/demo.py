import spelling
import re

with open("input.txt") as f:
  words = f.read().split()
words = list(map(str.strip, words))
words = [re.sub(r'[^a-zA-Z\']+', '', word) for word in words]
words = [word for word in words if word]

output = ''

for word in sorted(list(set(words))):
  if not spelling.check_word(word):
    output += (f"{word} ({words.count(word)}) \n")

with open("output1.txt", "w") as f:
    f.write(output)