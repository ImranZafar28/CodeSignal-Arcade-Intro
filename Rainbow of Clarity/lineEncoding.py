# lineEncoding
'''
Given a string, return its encoding defined as follows:

First, the string is divided into the least possible number of disjoint substrings consisting of identical characters
    -> for example, "aabbbc" is divided into ["aa", "bbb", "c"]

Next, each substring with length greater than one is replaced with a concatenation of its length and the repeating character
    -> for example, substring "bbb" is replaced by "3b"

Finally, all the new strings are concatenated together in the same order and a new string is returned.
'''

# Example
'''
For s = "aabbbc", the output should be solution(s) = "2a3bc".
'''

# Solution:

def solution(s):
    digit = 0
    alpha = ''
    result = ''
    for i in s:
        if alpha == '':
            alpha = i
            digit += 1
        elif i == alpha:
            digit += 1
        else:
            if digit == 1:
                result += alpha
            else:
                result += str(digit) + alpha
            alpha = i
            digit = 1
    if digit == 1:
        result += alpha
    else:
        result += str(digit) + alpha
    return result

print(solution("aabbbc"))