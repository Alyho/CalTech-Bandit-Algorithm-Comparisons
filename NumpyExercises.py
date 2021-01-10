# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 14:58:42 2019

@author: student-minecraft
"""
import numpy as np

#6

array = np.empty(4)
print (array)

#7

array = np.zeros(10)
print (array)

#8

array = np.ones([3,5])
print (array)

#9

array = np.array([10, 10, 10, 10, 10])
print (array)

#10

array = np.arange(0,6)
print (array)

#11

array = np.arange(-4, 9, 2)
print(array)

#12

array = np.arange(10, -3, -3)
print(array)

#13

array = np.array([7, 6, -2, 0, 5, 8, -1, -0.5])
print (array)

#14

max_a = np.max(array)
argmax_a = np.argmax(array)

print ("Max: " + str(max_a) + " Argmax: " + str(argmax_a))

max_b = 0

for i in range(0, len(array)):
    if (max_b < array[i]):
        max_b = array[i]
        argmax_b = i
        
print ("Max: " + str(max_b) + " Argmax: " + str(argmax_b))

