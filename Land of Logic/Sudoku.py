# Sudoku
'''
Sudoku is a number-placement puzzle. The objective is to fill a 9 x 9 grid with digits so that each column, 
each row, and each of the nine 3 x 3 sub-grids that compose the grid contains all of the digits from 1 to 9.

This algorithm should check if the given grid of numbers represents a correct solution to Sudoku.
'''

# Example
'''
For
grid = [[1, 3, 2, 5, 4, 6, 9, 8, 7],
        [4, 6, 5, 8, 7, 9, 3, 2, 1],
        [7, 9, 8, 2, 1, 3, 6, 5, 4],
        [9, 2, 1, 4, 3, 5, 8, 7, 6],
        [3, 5, 4, 7, 6, 8, 2, 1, 9],
        [6, 8, 7, 1, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 3, 6, 5, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5]]

the output should be solution(grid) = true;

For
grid = [[1, 3, 4, 2, 5, 6, 9, 8, 7],
        [4, 6, 8, 5, 7, 9, 3, 2, 1],
        [7, 9, 2, 8, 1, 3, 6, 5, 4],
        [9, 2, 3, 1, 4, 5, 8, 7, 6],
        [3, 5, 7, 4, 6, 8, 2, 1, 9],
        [6, 8, 1, 7, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 5, 6, 3, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5]]

the output should be solution(grid) = false.

The output should be false: each of the nine 3 x 3 sub-grids should contain all of the digits from 1 to 9.

These examples are represented on the image below.
'''

# Solution 1:

def solution1(grid):
    repeat = 0
    for val in range(1,10):
        for i in range(9):
            for j in range(9):
                if grid[i][j] == val:
                    repeat += 1
                    if repeat > 1:
                        return False
            repeat = 0
    
    for val in range(1,10):
        for i in range(9):
            for j in range(9):
                if grid[j][i] == val:
                    repeat += 1
                    if repeat > 1:
                        return False
            repeat = 0
    
    for val in range(1,10):
        for i in range(3):
            for j in range(3):
                if grid[i][j] == val:
                    repeat += 1
                    if repeat > 1:
                        return False
        repeat = 0
    for val in range(1,10):
        for i in range(3, 6):
            for j in range(3, 6):
                if grid[i][j] == val:
                    repeat += 1
                    if repeat > 1:
                        return False
        repeat = 0
    for val in range(1,10):
        for i in range(6, 9):
            for j in range(6, 9):
                if grid[i][j] == val:
                    repeat += 1
                    if repeat > 1:
                        return False
        repeat = 0
    
    return True

grid = [[1, 3, 2, 5, 4, 6, 9, 8, 7],
        [4, 6, 5, 8, 7, 9, 3, 2, 1],
        [7, 9, 8, 2, 1, 3, 6, 5, 4],
        [9, 2, 1, 4, 3, 5, 8, 7, 6],
        [3, 5, 4, 7, 6, 8, 2, 1, 9],
        [6, 8, 7, 1, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 3, 6, 5, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5]]
print(solution1(grid))

grid = [[1, 3, 4, 2, 5, 6, 9, 8, 7],
        [4, 6, 8, 5, 7, 9, 3, 2, 1],
        [7, 9, 2, 8, 1, 3, 6, 5, 4],
        [9, 2, 3, 1, 4, 5, 8, 7, 6],
        [3, 5, 7, 4, 6, 8, 2, 1, 9],
        [6, 8, 1, 7, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 5, 6, 3, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5]]
print(solution1(grid))

# Solution 2:

def solution2(grid):
    for row in grid:
        if not is_repeat(row):
            return False
   
    for col in range(9):
        column = [grid[row][col] for row in range(9)]
        if not is_repeat(column):
            return False

    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            subgrid = [grid[r][c] for r in range(row, row+3) for c in range(col, col+3)]
            if not is_repeat(subgrid):
                return False

    return True

def is_repeat(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return False
        seen.add(num)
    return True

grid = [[1, 3, 2, 5, 4, 6, 9, 8, 7],
        [4, 6, 5, 8, 7, 9, 3, 2, 1],
        [7, 9, 8, 2, 1, 3, 6, 5, 4],
        [9, 2, 1, 4, 3, 5, 8, 7, 6],
        [3, 5, 4, 7, 6, 8, 2, 1, 9],
        [6, 8, 7, 1, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 3, 6, 5, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5]]
print(solution2(grid))

grid = [[1, 3, 4, 2, 5, 6, 9, 8, 7],
        [4, 6, 8, 5, 7, 9, 3, 2, 1],
        [7, 9, 2, 8, 1, 3, 6, 5, 4],
        [9, 2, 3, 1, 4, 5, 8, 7, 6],
        [3, 5, 7, 4, 6, 8, 2, 1, 9],
        [6, 8, 1, 7, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 5, 6, 3, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5]]
print(solution2(grid))