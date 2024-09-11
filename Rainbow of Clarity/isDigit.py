# isDigit
'''
Determine if the given character is a digit or not.
'''

# Example
'''
For symbol = '0', the output should be solution(symbol) = true;

For symbol = '-', the output should be solution(symbol) = false.
'''

# Solution:

def solution(symbol):
    import string
    if symbol in string.digits:
        return True
    else:
        return False

symbol = '0'
print(solution(symbol))

symbol = '-'
print(solution(symbol))