import numpy as np
from matplotlib import pyplot as plt

def ecdf(data):
    """Computes an ECDF of given 1D np.array"""

    #Compute the values of the x-axis
    x = np.sort(data)

    bins = np.arange(0, len(data))
    bin_counts, bin_edges = np.histogram(x, len(bins))

    #Cumulative counts
    count = 0
    cum_bin_counts = np.array([])
    for n in bin_counts:
        count = count + n
        cum_bin_counts = np.append(cum_bin_counts, count)

    #Compute the values of the y-axis
    y = (cum_bin_counts + 1) / len(data)

    return (x, y)

#Plot the ECDF of high and low food data

# Load in data
xa_low = np.loadtxt('data/xa_low_food.csv', comments = '#')
xa_high = np.loadtxt('data/xa_high_food.csv', comments = '#')

#compute the ecdf
xa_low_x, xa_low_y = ecdf(xa_low)
xa_high_x, xa_high_y = ecdf(xa_high)

#Plot the ECDF
fig, ax = plt.subplots(1, 1)
ax.plot(xa_low_x, xa_low_y, marker='.', linestyle='none', color='b')
ax.plot(xa_high_x, xa_high_y, marker='.', linestyle='none', color='r')
ax.set_xlabel('Data')
ax.set_ylabel('Empirical Cumulative Probability')

#plt.show()
