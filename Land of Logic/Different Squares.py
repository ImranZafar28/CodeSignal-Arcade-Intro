# Different Squares
'''
Given a rectangular matrix containing only digits, calculate the number of different 2 x 2 squares in it.
'''

# Example
'''
For
matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]

the output should be solution(matrix) = 6.

Here are all 6 different 2 x 2 squares:

->    1 2
      2 2
->    2 1
      2 2
->    2 2
      2 2
->    2 2
      1 2
->    2 2
      2 3
->    2 3
      2 1
'''

# Solution:

def solution(matrix):
    if len(matrix) < 2 or len(matrix[0]) < 2:
        return 0
    l = []
    s = []
    x1, x2, y1, y2, = 0, 2, 0, 2
    a= True
    while a:
        for i in range(x1, x2):
            for j in range(y1, y2):
                s.append(matrix[i][j])
        if s not in l:
            l.append(s)
        s = []
        if y2 < len(matrix[0]):
            y1 += 1
            y2 += 1
        elif x2 < len(matrix):
            x1 += 1
            x2 += 1
            y1, y2 = 0, 2
        else:
            a = False
    return len(l)

matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]

print(solution(matrix))