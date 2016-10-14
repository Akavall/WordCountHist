#!/usr/bin/env python

import os
import sys

from utilities.walk_all_files import make_all_words_counter
from utilities.graphs import histogram

if __name__ == "__main__":
    directory_path = sys.argv[1]
    if len(sys.argv) == 3 and sys.argv[2] == "english":
        from nltk.corpus import words
        english = set(words.words())
        all_words_counter = make_all_words_counter(directory_path, english=english)
    else:
        all_words_counter = make_all_words_counter(directory_path, english=None)

    histogram(all_words_counter)

    
