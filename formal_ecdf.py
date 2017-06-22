import numpy as np
from matplotlib import pyplot as plt
import ecdf_infromal

def ecdf(data, formal=False, buff=0.1, min_x=None, max_x=None):
    """
    Generate `x` and `y` values for plotting an ECDF.

    Parameters
    ----------
    data : array_like
        Array of data to be plotted as an ECDF.
    formal : bool, default False
        If True, generate `x` and `y` values for formal ECDF.
        Otherwise, generate `x` and `y` values for "dot" style ECDF.
    buff : float, default 0.1
        How long the tails at y = 0 and y = 1 should extend as a
        fraction of the total range of the data. Ignored if
        `formal` is False.
    min_x : float, default None
        Minimum value of `x` to include on plot. Overrides `buff`.
        Ignored if `formal` is False.
    max_x : float, default None
        Maximum value of `x` to include on plot. Overrides `buff`.
        Ignored if `formal` is False.

    Returns
    -------
    x : array
        `x` values for plotting
    y : array
        `y` values for plotting
    """

    x, y = ecdf_infromal.ecdf(data)

    range_of_vals = max(x) - min(x)

    #Determine the domain of the ecdf plot
    if min_x != None:
        x_bot = min_x
    else:
        x_bot = np.floor(min(x) - buff*range_of_vals)

    if max_x != None:
        x_top = max_x
    else:
        x_top = np.ceil(max(x) + buff*range_of_vals)

    #Append the x values at the beginning and the end of the ecdf
    start = np.arange(x_bot, min(x))
    end = np.arange(max(x), x_top)
    x = np.insert(x, 0, start)
    x = np.append(x, end)

    #Append the y values at the beginning and the end of the ecdf
    y_start = np.zeros(len(start))
    y_end = np.ones(len(end))
    y = np.insert(y, 0, y_start)
    y = np.append(y, y_end)

    return(x, y)

def plot_ecdf(data, formal=False, buff=0.1, min_x=None, max_x=None):
    """
    Plots the ecdf
    """
    x, y = ecdf(data, formal=False, buff=0.1, min_x=None, max_x=None)

    #Generate the scatterplot ecdf
    fig, ax = plt.subplots(1, 1)
    ax.plot(x, y, marker='.', linestyle='none', color='r')
    ax.set_xlabel('Data')
    ax.set_ylabel('Empirical Cumulative Probability')

    if formal == False:
        plt.show()
    else:
        #extra points that indicate the "bottom of the step"
        new_x = [x[0]]
        new_y = [y[0]]

        for x_ind in range(0, len(x) - 1):

            #Include the tip of the stair value
            new_x.append(x[x_ind])
            new_y.append(y[x_ind])

            #Include the value at the bottom of the step
            step_x_val = x[x_ind + 1]
            step_y_val = y[x_ind]
            new_x.append(step_x_val)
            new_y.append(step_y_val)

        ax.plot(new_x, new_y, color='b')
        plt.show()
