#!/usr/bin/env python3

from itertools import chain

list1 = ["thanos", "peter", "george"]
list2 = ["vrindavan", "bob", "luciano"]
list3 = ["andrej", "beff", "zucc"]

list4 = [list2, list3]
combined = chain(list1, list2, list3)
combined2 = chain(list1, list4)
result = list(combined)
result2 = list(combined2)

print(result)  
print(result2)  
