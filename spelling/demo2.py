import spelling
import re

with open("input.txt") as f:
  sentences  = f.readlines()
with open("input.txt") as f:
  words = f.read().split()

sentences = [re.sub(r'[^a-zA-Z \']+', '', sentence) for sentence in sentences]
 
words = list(map(str.strip, words))
words = [re.sub(r'[^a-zA-Z\']+', '', word) for word in words]
words = [word for word in words if word]


output = ''
for word in sorted(list(set(words))):
     if not spelling.check_word(word):
        
        output += (f"{word} (line")
        for i in range(len(sentences)):
           if word in sentences[i]:
              output += f", {i+1}"
        output += f") \n"              
# print(output)
with open("output2.txt", "w") as f:
   f.write(output)
