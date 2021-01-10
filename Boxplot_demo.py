# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 17:30:50 2019

This is a demonstration of making a box plot with the Matplotlib library.

@author: Ellen
"""

import numpy as np
import matplotlib.pyplot as plt

# Generate fake data. Note that this is a list of three NumPy arrays.
data = [np.random.rand(20), 2 * np.random.rand(20) + 4, 
        4 * np.random.rand(20) - 2]

# Make the figure:
plt.figure()

plt.boxplot(data)

# Add axis labels and a title:
plt.xlabel('x')
plt.ylabel('y')
plt.title('Boxplot Demo')

