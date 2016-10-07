from collections import Counter
import os
import zipfile

from word_counting_tools import make_counter

def read_zipped(path, english=None):
    counts = Counter()
    z = zipfile.ZipFile(path)
    for f in z.namelist():
        if os.path.splitext(f) == ".txt":
            with z.open(f) as my_file:
                for line in my_file:                    
                    counts.update(make_counter(line, english=english))

    return counts
