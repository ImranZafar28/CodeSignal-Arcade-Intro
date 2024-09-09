# longestDigitsPrefix
'''
Given a string, output its longest prefix which contains only digits.
'''

# Example
'''
For inputString = "123aa1", the output should be solution(inputString) = "123".
'''

# Solution:

def solution(inputString):
    import string
    d = string.digits
    prefix = ''
    for i in range(len(inputString)):
        if inputString[i] not in d:
            return inputString[:i]
        elif inputString[i] in d:
            continue
    return inputString

print(solution("123aa10"))