# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 14:13:35 2020

@author: student-minecraft
"""

import matplotlib.pyplot as plt
import numpy as np

plt.close('all')

x = np.linspace(-1, 1, num = 21)
y1 = x
y2 = x**2
y3 = x**3

plt.figure()
plt.plot(x, y1, 'chocolate')
plt.plot(x, y2, 'm')
plt.plot(x, y3, 'forestgreen')

plt.grid('on')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Quadratic vs Linear')
plt.legend(['y=x', 'y=x^2', 'y=x^3'])

def findstdev (array):
    summation = 0 
    mean = np.mean(array)
    for l in range(len(array)):
        summation += (array[l] - mean)**2
    stdev = (summation / len(array))** 0.5
    return stdev

print(np.std(y1))
print(findstdev(y1))
print(findstdev(y2))

z = np.array([1, 2, 10])
standard_deviations = np.zeros(3)

for i in range(len(z)):
    arr = np.random.uniform(0, z[i], 2000)
    
    plt.figure()
    plt.hist(arr, bins = 20, color ='b')
    standard_deviations[i] = findstdev(arr)
    
plt.figure()
plt.bar(np.arange(3), standard_deviations)

points = 20
numerator = 0
random = np.random.uniform(-1, 1, points)

numerator = np.where(random > 0) [0]
print(numerator)
        
print(len(numerator) /points)



    
    






