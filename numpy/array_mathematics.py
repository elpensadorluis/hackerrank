""" 
Problem
Basic mathematical functions operate elementwise on arrays. They are available both as operator overloads and as functions in the NumPy module.
Task
You are given two integer arrays, A and B of dimensions NxM.
Your task is to perform the following operations:
Add (A+B).
Subtract (A-B).
Multiply (A*B).
Integer Division (A/B).
mod (A%B).
Power (A**B).
note
There is a method numpy.floor_divide() that works like numpy.divide() except it performs a floor division.
Input Format
The first line contains two space separated integers, N and M.
The next N lines contains M space separated integers of array A.
The following N lines contains M space separated integers of array B.
Output Format
Print the result of each operation in the given order under Task.
"""

import numpy


def finding_array_mathematics(n, m, a, b):
    print(numpy.add(a, b))
    print(numpy.subtract(a, b))
    print(numpy.multiply(a, b))
    print(numpy.floor_divide(a, b))
    print(numpy.mod(a, b))
    print(numpy.power(a, b))


if __name__ == '__main__':
    n, m = map(int, input().split())
    a = numpy.array([input().split() for _ in range(n)], int)
    b = numpy.array([input().split() for _ in range(n)], int)
    finding_array_mathematics(n, m, a, b)
