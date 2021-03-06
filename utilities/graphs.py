import matplotlib.pyplot as plt
import numpy as np
import logging

def histogram(my_list):
    # taking square root of number of values in list
    # a common rule of thumb method for finding number
    # of bins
    if not my_list:
        logging.error("list provided to histogram is empty, check that you provided the correct directory")
        return
    n_bins = int(np.sqrt(len(my_list) + 1))
    plt.hist(my_list, n_bins)
    plt.title("Distribution of word counts in a file")
    plt.xlabel("Count per file")
    plt.ylabel("Frequency")
    plt.show()
