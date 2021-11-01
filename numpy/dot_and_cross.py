"""
dot

The dot tool returns the dot product of two arrays.

import numpy

A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])

print numpy.dot(A, B)       #Output : 11

cross

The cross tool returns the cross product of two arrays.

import numpy

A = numpy.array([ 1, 2 ])
B = numpy.array([ 3, 4 ])

print numpy.cross(A, B)     #Output : -2

Task
You are given two arrays: A and B. Both have dimensions of NxN.
Your task is to compute their matrix product.

Input Format
The first line contains the integer, N.
The next N lines contains the N space separated elements of array A.
The following N lines contains the N space separated elements of array B.

Output Format
Print the matrix product of A and B.
"""

import numpy

if __name__ == '__main__':
    n = int(input())
    a = numpy.array([input().split() for _ in range(n)], int)
    b = numpy.array([input().split() for _ in range(n)], int)
    print(numpy.dot(a, b))
