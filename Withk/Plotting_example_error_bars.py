# -*- coding: utf-8 -*-
"""
Example error bar plot.
"""

import numpy as np
import matplotlib.pyplot as plt


plt.close('all')

# Make up some fake data to plot:
num_data_pts = 1000
x = np.arange(num_data_pts)

mean = np.sin(0.01 * x)
std = 0.1 * np.ones(len(x))

"""First, plot the data using shading."""
plt.figure()
plt.plot(x, mean)
plt.fill_between(x, mean - std, mean + std, alpha = 0.3)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Shade between the Mean and Standard Deviation')

"""Now, plot the data with error bars."""
num_errorbars = 15     # Number of error bars to draw on the plot.

# Determine x-locations at which to draw the error bars. This is done by picking
# num_errorbars equally-spaced points in x. So that the error bars are not 
# drawn right at the edges of the plot, we can add 2 to the number of error 
# bars, and then chop off the 1st and last locations (via "[1: -1]"). The chopped-
# off locations are all the way at the left and right of the plot.
errorbar_x = np.linspace(1, num_data_pts, num_errorbars + 2)[1: -1]
errorbar_x = np.round(errorbar_x).astype(int)   # Round to nearest integer

plt.figure()
plt.plot(x, mean, color = 'blue')
plt.errorbar(errorbar_x, mean[errorbar_x], yerr = std[errorbar_x], 
             fmt='o', color = 'blue', ecolor='blue', capsize=5,
             linewidth = 2, capthick = 2)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Use Error Bars to Show the Standard Deviation')
