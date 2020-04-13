#!/usr/bin/env python
import sys

# maps words to their counts
wordCount = {}

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        continue

    try:
        wordCount[word] = wordCount[word] + count
    except:
        wordCount[word] = count

# write the tuples to stdout
# Note: they are unsorted
for word in wordCount.keys():
    print('%s\t%s' % (word, wordCount[word]))