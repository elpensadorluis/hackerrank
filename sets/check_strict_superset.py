# You are given a set A and n other sets.
# Your job is to find whether set A is a strict superset of each of the N sets.
# Print True, if A is a strict superset of each of the N sets. Otherwise, print False.
# A strict superset has at least one element that does not exist in its subset.
# Example:
# Set([1, 3, 4]) is a strict superset of set([1, 3]).
# Set([1, 3, 4]) is not a strict superset of set([1, 3, 4]).
# Set([1, 3, 4]) is not a strict superset of set([1, 3, 5]).
# Input Format
# The first line contains the space separated elements of set A.
# The second line contains integer N, the number of other sets.
# The next N lines contains the space separated elements of the other N sets.
# Constraints
# 0<len(A)<501
# 0<N<21
# 0<len(other_set)<101
# Output Format
# Print True if set A is a strict superset of all other N sets. Otherwise, print False.

# Enter your code here. Read input from STDIN. Print output to STDOUT

def check_strict_superset(setA, other_sets):
    for other_set in other_sets:
        if not setA.issuperset(other_set):
            return False
    return True


if __name__ == '__main__':
    setA = set(map(int, input().split()))
    N = int(input())
    other_sets = []
    for _ in range(N):
        other_sets.append(set(map(int, input().split())))
    print(check_strict_superset(setA, other_sets))
