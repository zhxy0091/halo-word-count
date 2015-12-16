#!/usr/bin/env python

import re
import collections

expected = ['the', 'and', 'to', 'of', 'i', 'you', 'a', 'my', 'hamlet', 'in']

def count_words():
    # TODO Please implement code here to analyze the hamlet.txt file and 
    # return an array the 10 most frequently found words in descending order of frequency.
    # Strip punctuation and make your comparisons case-insensitive.
    raise Exception('TODO')

if __name__ == '__main__':
    print('Most Frequent Words...')
    answer = count_words()

    print('Answer: %s' % answer)    
    assert(answer == expected)
    print('SUCCESS!')
