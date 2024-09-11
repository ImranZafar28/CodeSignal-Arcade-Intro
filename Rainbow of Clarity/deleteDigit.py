# deleteDigit
'''
Given some integer, find the maximal number you can obtain by deleting exactly one digit of the given number.
'''

# Example
'''
For n = 152, the output should be solution(n) = 52;

For n = 1001, the output should be solution(n) = 101.
'''

# Solution:

def solution(n):
    l = []
    list_n = list(str(n))
    index = 0
    value = ''
    for i in range(len(list_n)):
        value = list_n[i]
        list_n.pop(i)
        l.append(int(''.join(list_n)))
        list_n.insert(i, value)
    return max(l)

print(solution(152))

print(solution(1001))