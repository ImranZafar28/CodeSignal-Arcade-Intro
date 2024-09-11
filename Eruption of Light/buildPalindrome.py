# buildPalindrome
'''
Given a string, find the shortest possible string which can be achieved by adding characters to the end of 
initial string to make it a palindrome.
'''

# Example
'''
For st = "abcdc", the output should be solution(st) = "abcdcba"
'''

# Solution:

def solution(st):
    st_list = list(st)
    replace = ''
    req = ''
    if st_list == st_list[::-1]:
        return st
    else:
        for i in range(len(st_list)):
            if st_list[i:] == st_list[:i-1:-1]:
                st += req[::-1]
                return st
            else:
                req += st_list[i]
            
print(solution("abcdc"))