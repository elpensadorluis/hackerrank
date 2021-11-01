"""
 min

The tool min returns the minimum value along a given axis.

import numpy

my_array = numpy.array([[2, 5], 
                        [3, 7],
                        [1, 3],
                        [4, 0]])

print numpy.min(my_array, axis = 0)         #Output : [1 0]
print numpy.min(my_array, axis = 1)         #Output : [2 3 1 0]
print numpy.min(my_array, axis = None)      #Output : 0
print numpy.min(my_array)                   #Output : 0

By default, the axis value is None. Therefore, it finds the minimum over all the dimensions of the input array.

max

The tool max returns the maximum value along a given axis.

import numpy

my_array = numpy.array([[2, 5], 
                        [3, 7],
                        [1, 3],
                        [4, 0]])

print numpy.max(my_array, axis = 0)         #Output : [4 7]
print numpy.max(my_array, axis = 1)         #Output : [5 7 3 4]
print numpy.max(my_array, axis = None)      #Output : 7
print numpy.max(my_array)                   #Output : 7

By default, the axis value is None. Therefore, it finds the maximum over all the dimensions of the input array.

Task
You are given a 2-D array with dimensions N X M.
Your task is to perform the min function over axis 1 and then find the max of that.

Input Format
The first line of input contains the space separated values of N and M.
The next N lines contains the space separated elements of the array.

Output Format
Compute the min along axis 1 and then print the max of that result.

"""

import numpy

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = numpy.array([input().split() for _ in range(n)], int)
    print(numpy.max(numpy.min(arr, axis=1), axis=None))
