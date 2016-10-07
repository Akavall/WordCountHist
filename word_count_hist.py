#!/usr/bin/env python

import os
import sys

from utilities.walk_all_files import make_all_words_counter
from utilities.graphs import histogram

if __name__ == "__main__":
    directory_path = sys.argv[1]
    all_words_counter = make_all_words_counter(directory_path)
    histogram(all_words_counter.values())

    
