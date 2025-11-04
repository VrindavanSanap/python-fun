#!/usr/bin/env python3
import collections
import sys

counts = collections.Counter()
for line in sys.stdin:
    words = line.lower().split()
    counts.update(words)

for word, count in counts.most_common()[:10]:
    print(word, count)

