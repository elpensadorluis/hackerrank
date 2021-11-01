# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.
# Example:
# marks key:value pairs are
# 'alpha':[20,30,40]
# 'beta':[30,50,70]
#query_name = 'beta'
# the query_name is 'beta'. beta's average score is (30+50+70)/3 = 50.0.
# Input Format
# The first line contains an integer, N, the number of students' records. The next N lines contains the name and marks obtained by that student separated by a space. The final line contains query_name, the name of a student to query.
# Constraints
#2 <= N <= 10
#0 <= marks[i] <= 100
# length of marks array = 3
# output format
# Print one line: the average of the marks obtained by the particular student correct to 2 decimal places.
# Sample Input 0
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika
# samble Output 0
# 56.00

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print("{0:.2f}".format(
        sum(student_marks[query_name])/len(student_marks[query_name])))
