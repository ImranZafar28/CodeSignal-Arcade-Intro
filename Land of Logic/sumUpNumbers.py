# sumUpNumbers
'''
CodeMaster has just returned from shopping. He scanned the check of the items he bought and gave the resulting string 
to Ratiorg to figure out the total number of purchased items. Since Ratiorg is a bot he is definitely going to 
automate it, so he needs a program that sums up all the numbers which appear in the given input.

Help Ratiorg by writing a function that returns the sum of numbers that appear in the given inputString.
'''

# Example
'''
For inputString = "2 apples, 12 oranges", the output should be solution(inputString) = 14.
'''

# Solution:

def solution(inputString):
    import string
    digits = string.digits
    d_str = '0'
    total = 0
    for i in range(len(inputString)):
        if inputString[i] in digits:
            d_str += inputString[i]
            if i == len(inputString) - 1 and type(int(d_str)) == int:
                total += int(d_str)
        else:
            total += int(d_str)
            d_str = '0'
    return total

print(solution("2 apples, 12 oranges"))