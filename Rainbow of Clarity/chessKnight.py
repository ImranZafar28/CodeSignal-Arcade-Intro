# chessKnight
'''
Given a position of a knight on the standard chessboard, find the number of different moves the knight can perform.

The knight can move to a square that is two squares horizontally and one square vertically, or two squares vertically 
and one square horizontally away from it. The complete move therefore looks like the letter L. Check out the image 
below to see all valid moves for a knight piece that is placed on one of the central squares.
'''

# Example
'''
For cell = "a1", the output should be solution(cell) = 2.

For cell = "c2", the output should be solution(cell) = 6.
'''

# Solution:

def solution(cell):
    d = {'a': 1, 'b': 2, 'c': 3, 'd': 4,
        'e': 5, 'f': 6, 'g': 7, 'h': 8}
    one = d.get(cell[0])
    two = int(cell[1])
    eight = [1, 2 , 3 , 4 , 5 , 6 , 7 , 8]
    count = 0
    if one + 1 in eight and two + 2 in eight:
        count += 1
    if one + 2 in eight and two + 1 in eight:
        count += 1
    if one + 2 in eight and two - 1 in eight:
        count += 1
    if one + 1 in eight and two - 2 in eight:
        count += 1
    if one - 1 in eight and two - 2 in eight:
        count += 1
    if one - 2 in eight and two - 1 in eight:
        count += 1
    if one - 2 in eight and two + 1 in eight:
        count += 1
    if one - 1 in eight and two + 2 in eight:
        count += 1
    return count

print(solution("a1"))

print(solution("c2"))