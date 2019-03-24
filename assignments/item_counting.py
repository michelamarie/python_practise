#!/usr/bin/python3


occurrences = ['500', 'cat', 'dog', 'apple', '256']

for i in sample_string.split():
    occurrences[i] = occurrences.get(i, 0) + 1

for i in occurrences:
    print("The word", word, "occurs", occurrences[word], "times in the string")