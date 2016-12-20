#!/usr/bin/env python

import re
import collections

import string  
import sys  

expected = ['the', 'and', 'to', 'of', 'i', 'you', 'a', 'my', 'hamlet', 'in']

def count_words():
    # TODO Please implement code here to analyze the hamlet.txt file and 
    # return an array the 10 most frequently found words in descending order of frequency.
    # Strip punctuation and make your comparisons case-insensitive.
    fname = "hamlet.txt"  
      
    try:  
        text = open(fname,'r').read()  
        text = string.lower(text)  
    except:  
        print "\nfile does not exist or I/O error"  
        sys.exit()  
    #ignore all punctuation
    for c in string.punctuation:  
        text=text.replace(c," ")

    #split into each word
    words = string.split(text)

    counts = {}  
    #count freq of word using dict
    for w in words:  
        counts[w] = counts.get(w,0) + 1  
    
    #sort by value using comparator
    items = counts.items()  
    items.sort(compareItems)  
    
    #construct result
    res = []
    for i in range(10):  
        #print items[i]
        res.append(items[i][0])

    return res  

#comparator order by freq in descending order
def compareItems((w1,c1), (w2,c2)):  
	if c1 > c2:  
	    return -1  
	elif c1 == c2:  
	    return cmp(w1, w2)  
	else:  
	    return 1  
   

if __name__ == '__main__':
    print('Most Frequent Words...')
    answer = count_words()

    print('Answer: %s' % answer)    
    assert(answer == expected)
    print('SUCCESS!')
