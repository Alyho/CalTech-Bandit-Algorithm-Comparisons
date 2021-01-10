# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 13:35:26 2019

@author: dchangho
"""

import numpy as np

#1 How would you initialize (in one line of code) a length-500 NumPy array in which all of the elements are equal to 8?

array = np.full(500, 8)
print (array)

#5 Generate 5 random numbers uniformly-distributed between 0 and 1.

array = np.random.rand(5)
print (array)

#6 - Generate 7 random numbers uniformly-distributed between 0 and 18.

array = np.random.rand(7) + np.random.randint(0,18,7)
print (array)

#7 - Generate 3 random numbers uniformly-distributed between -5 and 4.

array = np.random.rand(3) + np.random.randint(-5,4,3)
print (array)

#8 Generate 4 random integers between 6 and 12.

array = np.random.randint(6,13,4)
print (array)

#9 Three ways to choose a random element from an array:
#Initialize (using whichever method you think makes most sense) an array with elements: [18, 16, 14, 12, 10, 8, 6, 4]. 
#Randomly select an element from it, using np.random.rand(…) as the source of randomness.
#Randomly select an element from it, using np.random.randint(…) as the source of randomness.
#Randomly select an element from it, using np.random.choice(…) as the source of randomness.

array = np.arange(18, 2, -2)
print(array)

array2 = np.random.rand(8)   
random_element = np.argmax(array2)
print (array[random_element])

random_element = np.random.randint(0,8)
print (array[random_element])

print (np.random.choice(array))

max_min_array = [np.min(array), np.max(array)]
print (max_min_array)

print (np.random.choice(max_min_array))
#10 Initialize (using whichever method you think makes most sense) an array with elements: [7, 4, 6, 5, 8, 9, 14, -4]. 
#With a single call to np.random.choice, draw 8 random elements from the array in a), with replacement.
#With a single call to np.random.choice, draw 8 random elements from the array in a), without replacement.


array = np.array([7, 4, 6, 5, 8, 9, 14, -4])
print (array)

print (np.random.choice(array, 8, replace = True))

print (np.random.choice(array, 8, replace = False))

#np.where
array3 = np.array([0, 5, 8, 0, 8, 1])
array4 = np.where(array3 == 0) [0]
print (array4)

array5 = np.where(array3 == np.max(array3))[0]
print (array5)

print (np.random.choice(array5))