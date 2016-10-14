import os
import zipfile

from word_counting_tools import make_counter

def read_zipped(path, english=None):
    counts_list = []
    z = zipfile.ZipFile(path)
    for f in z.namelist():
        if os.path.splitext(f)[1] == ".txt":
            counts = 0
            with z.open(f) as my_file:
                for line in my_file:                    
                    counts += make_counter(line, english=english)
            counts_list.append(counts)

    return counts_list
