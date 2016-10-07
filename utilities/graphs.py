import matplotlib.pyplot as plt
import numpy as np

def histogram(my_list):
    # taking square root of number of values in list
    # a common rule of thumb method for finding number
    # of bins
    n_bins = int(np.sqrt(len(my_list)))
    plt.hist(my_list, n_bins)
    plt.title("Distribution of word counts")
    plt.xlabel("Word appearances")
    plt.ylabel("Count appearance")
    plt.show()

if __name__ == "__main__":
    x = [1,2,3,1,3,6,2,2,3,2,1,2,5,10,10,10,10]
    histogram(x)
