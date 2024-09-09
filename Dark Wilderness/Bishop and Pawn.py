# Bishop and Pawn
'''
Given the positions of a white bishop and a black pawn on the standard chess board, determine whether the bishop can 
capture the pawn in one move.

The bishop has no restrictions in distance for each move, but is limited to diagonal movement. Check out the example 
below to see how it can move:
'''

# Example
'''
For bishop = "a1" and pawn = "c3", the output should be solution(bishop, pawn) = true.

For bishop = "h1" and pawn = "h3", the output should be solution(bishop, pawn) = false.
'''

# Solution:

def solution(bishop, pawn):
    board1 = [['a7','b8'],
            ['a6','b7','c8'],
            ['a5','b6','c7','d8'],
            ['a4','b5','c6','d7','e8'],
            ['a3','b4','c5','d6','e7','f8'],
            ['a2','b3','c4','d5','e6','f7','g8'],
            ['a1','b2','c3','d4','e5','f6','g7','h8'],
            ['b1','c2','d3','e4','f5','g6','h7'],
            ['c1','d2','e3','f4','g5','h6'],
            ['d1','e2','f3','g4','h5'],
            ['e1','f2','g3','h4'],
            ['f1','g2','h3'],
            ['g1','h2']]
    board2 = [['a2','b1'],
            ['a3','b2','c1'],
            ['a4','b3','c2','d1'],
            ['a5','b4','c3','d2','e1'],
            ['a6','b5','c4','d3','e2','f1'],
            ['a7','b6','c5','d4','e3','f2','g1'],
            ['a8','b7','c6','d5','e4','f3','g2','h1'],
            ['b8','c7','d6','e5','f4','g3','h2'],
            ['c8','d7','e6','f5','g4','h3'],
            ['d8','e7','f6','g5','h4'],
            ['e8','f7','g6','h5'],
            ['f8','g7','h6'],
            ['g8','h7']]
    for i in range(len(board1)):
        if bishop in board1[i] and pawn in board1[i]:
            return True
        elif bishop in board2[i] and pawn in board2[i]:
            return True
    return False

print(solution("a1", "c3"))
print(solution("h1", "h3"))