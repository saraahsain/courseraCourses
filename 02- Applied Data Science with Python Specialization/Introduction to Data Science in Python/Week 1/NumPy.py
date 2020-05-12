import numpy as np

mylist = [1, 2, 3]
x = np.array(mylist)
print(x)

m = np.array([[7, 8, 9], [10, 11, 12]])
print(m)

#shape method to find the dimensions of the array. (rows, columns)
m.shape#(2,3)

#`arange` returns evenly spaced values within a given interval.
n = np.arange(0, 30, 2) # start at 0 count up by 2, stop before 30
print(n)#array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28])


#reshape returns an array with the same data with a new shape.
n = n.reshape(3, 5) # reshape array to be 3x5
n
    # array([[ 0,  2,  4,  6,  8],
    #        [10, 12, 14, 16, 18],
    #        [20, 22, 24, 26, 28]])


#linspace returns evenly spaced numbers over a specified interval.
o = np.linspace(0, 4, 9) # return 9 evenly spaced values from 0 to 4
o#array([ 0. ,  0.5,  1. ,  1.5,  2. ,  2.5,  3. ,  3.5,  4. ])


#resize changes the shape and size of array in-place.
o.resize(3, 3)
o


#Create an array using repeating list (or see np.tile)
np.array([1, 2, 3] * 3)#array([1, 2, 3, 1, 2, 3, 1, 2, 3])


#Repeat elements of an array using repeat.
np.repeat([1, 2, 3], 3)#array([1, 1, 1, 2, 2, 2, 3, 3, 3])

