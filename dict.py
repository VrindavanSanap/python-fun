#!/usr/bin/python3

b = {'apple': 3, 'banana': 1, 'cherry': 5, 'date': 2}
sorted_items = sorted(b.items(), key=lambda kv: -kv[1])
print(sorted_items)

