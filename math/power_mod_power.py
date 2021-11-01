# So far, we have only heard of python's powers. Now, we will witness them!.
# Power or exponents in Python can be calculated using the built-in power function. Call the power function a^b as shown below:
# >>> pow(a,b)
# or
# >>> a**b
# it's also possible to calculate a^b mod m using the pow function as follows:
# >>> pow(a,b,m)
# this is very helpful in computations where you have to print the results modulo m.
# Note: Here, a and b can be floats or negatives, but, if a third argument is present, b cannot be negative.
# Note: Python has a math module that has its own pow function. It take two arguments and returns a float. it is uncommon to use math.pow().
# Task
# You are given three integers: a, b, and m, respectively. Print two lines.
# On the first line, print the result of pow(a,b). On the second line, print the result of pow(a,b,m). (Recall that this is the same as pow(a,b) mod m.)
# Input Format
# the first line contains the value of a, the second line contains the value of b, and the third line contains the value of m.

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    m = int(input())
    print(pow(a, b))
    print(pow(a, b, m))
