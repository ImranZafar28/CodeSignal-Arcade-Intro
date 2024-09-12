# longestWord
'''
Define a word as a sequence of consecutive English letters. Find the longest word from the given string.
'''

# Example
'''
For text = "Ready, steady, go!", the output should be solution(text) = "steady".
'''

# Solution:

def solution(text):
    import string
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    word = ''
    longest = ''
    for i in text:
        if i in lowercase or i in uppercase:
            word += i
            if len(word) == len(text):
                return word
            elif len(word) > len(longest):
                longest = word
        else:
            if len(word) > len(longest):
                longest = word
            word = ''
    return longest

print(solution("Ready, steady, go!"))