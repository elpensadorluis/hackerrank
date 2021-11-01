# Integers in Python can be as big as the bytes in your machine's memory. There is no limit in size as there is: 2^31 - 1(c++ int) or 2^63 - 1(c++ long long int).
# As we know, the result of a^b grows really fast with b:
# Let's do some calculations on very big numbers.
# Task
# Read four numbers, a, b, c, and d, and print the result of a^b + c^d.
# Input Format
# integer a, b, c, and d given on four separate lines, respectively.
# Constraints
#1 <= a <= 1000
#1 <= b <= 1000
#1 <= c <= 1000
#1 <= d <= 1000
# Output Format
# print the result of a^b + c^d on one line.

# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    print(pow(a, b) + pow(c, d))
