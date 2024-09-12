# spiralNumbers
'''
Construct a square matrix with a size N x N containing integers from 1 to N * N in a spiral order, 
starting from top-left and in clockwise direction.
'''

# Example
'''
For n = 3, the output should be

solution(n) = [[1, 2, 3],
               [8, 9, 4],
               [7, 6, 5]]
'''

# Solution:


def solution(n):
    matrix = [[0 for j in range(n)] for i in range(n)]
    val = 1
    start_row = 0
    start_col = 0
    end_row = n
    end_col = n
    while (start_row < end_row and start_col < end_col):
        for i in range(start_col, end_col):
            matrix[start_row][i] = val
            val += 1
        start_row += 1
        
        for i in range(start_row, end_row):
            matrix[i][end_col - 1] = val
            val += 1
        end_col -= 1
            
        for i in range(end_col - 1, start_col - 1, -1):
            matrix[end_row - 1][i] = val
            val += 1
        end_row -= 1
        
        for i in range(end_row - 1, start_row - 1, -1):
            matrix[i][start_col] = val
            val += 1
        start_col += 1
                    
    return matrix

print(solution(3))