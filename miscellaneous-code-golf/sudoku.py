# https://www.hackerrank.com/challenges/sudoku

def find_next_cell(grid, i, j):
    for x in range(i, 9):
        for y in range(j, 9):
            if grid[x][y] == 0:
                return x, y
    for x in range(0, 9):
        for y in range(0, 9):
            if grid[x][y] == 0:
                return x, y
    return -1, -1

def is_valid(grid, i, j, e):
    if not all([e != grid[i][x] for x in range(9)]):
        return False

    if not all([e != grid[x][j] for x in range(9)]):
        return False

    top_x, top_y = 3 * (i // 3), 3 * (j // 3)
    for x in range(top_x, top_x + 3):
        for y in range(top_y, top_y + 3):
            if grid[x][y] == e:
                return False

    return True

def solve_sudoku(grid, i=0, j=0):
    i, j = find_next_cell(grid, i, j)
    if i == -1:
        return True
    for e in range(1,10):
        if is_valid(grid, i, j, e):
            grid[i][j] = e
            if solve_sudoku(grid, i, j):
                return True
            grid[i][j] = 0
    return False

n = int(input())
for x in range(0, n):
    puzzle = []
    for line_num in range(0, 9):
        puzzle.append(list(map(int, input().split())))

    solve_sudoku(puzzle)
    for row in puzzle:
        print(' '.join(list(map(str, row))))
