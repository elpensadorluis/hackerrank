# the included code stub will read a list of integers, n, from stdin. Without using any string methods, try to print the following:
# 123...n
# note that "..." represents any number of consecutive integers

if __name__ == '__main__':
    n = int(input())
    for i in range(1, n+1):
        print(i, end='')
