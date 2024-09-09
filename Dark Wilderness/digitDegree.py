# digitDegree
'''
Let's define digit degree of some positive integer as the number of times we need to replace this number with the sum 
of its digits until we get to a one digit number.

Given an integer, find its digit degree.
'''

# Example
'''
For n = 5, the output should be solution(n) = 0;

For n = 100, the output should be solution(n) = 1.
1 + 0 + 0 = 1.

For n = 91, the output should be solution(n) = 2.
9 + 1 = 10 -> 1 + 0 = 1.
'''

# Solution:

def solution(n):
    degree = 0
    while True:
        numList = list(str(n))
        if len(numList) == 1:
            return degree
        else:
            for i in range(len(numList)):
                numList[i] = int(numList[i])
            n = sum(numList)
            degree += 1

print(solution(5))
print(solution(100))
print(solution(91))