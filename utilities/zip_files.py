from collections import Counter
import zipfile
from word_counting_tools import make_counter

def read_zipped(path):
    counts = Counter()
    z = zipfile.ZipFile(path)
    for f in z.namelist():
        if f[-3:] == "txt":
            with z.open(f) as my_file:
                for line in my_file:                    
                    counts.update(make_counter(line))

    return counts
