import os
from collections import Counter
from utilities.zip_files import read_zipped
from utilities.word_counting_tools import make_counter

def count_words_in_file(file_path, english=None):
    counts = Counter()
    with open(file_path) as f_in:
        for line in f_in:
            counts.update(make_counter(line, english=english))
    return counts

def make_all_words_counter(directory_path, english=None):
    all_counts = Counter()
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            if os.path.splitext(file_name)[1] == ".txt":
                full_path = root + "/" + file_name
                counts = count_words_in_file(full_path, english=english)
                all_counts.update(counts)
            elif os.path.splitext(file_name)[1] == ".zip":
                full_path = root + "/" + file_name
                counts = read_zipped(full_path, english=english)
                all_counts.update(counts)
    return all_counts 
