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
    n_bins = int(np.sqrt(len(my_list)))
    plt.hist(my_list, n_bins)
    plt.title("Distribution of word counts")
    plt.xlabel("Word appearances")
    plt.ylabel("Count appearance")
    plt.show()
