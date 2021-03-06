#! /usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter
import logging
import string

def make_counter(line, english=None):
    no_punc = remove_punctuation(line)
    words = [w.lower() for w in no_punc.rstrip().split(" ") if w]
    ascii_words = [w for w in words if check_ascii(w)]
    not_num_ascii_words = [w for w in words if not w.isdigit()]
    if english:
        return sum(1 for w in not_num_ascii_words if w in english)

    return len(not_num_ascii_words)
    
def remove_punctuation(line):
    punctuation = set(string.punctuation)
    return "".join(x for x in line if x not in punctuation)

def check_ascii(word):
    try:
        word.decode('ascii')
        return True
    except UnicodeDecodeError:
        logging.warn("{} is Not unicode".format(word))
        return False 
    
    
