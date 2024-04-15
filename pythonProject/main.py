import time

def find_empty_position(sudoku, emptyList):
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:
                emptyList[0] = row
                emptyList[1] = col
                return True
    return False

def used_in_row(sudoku, row, num):
    for i in range(9):
        if sudoku[row][i] == num:
            return True
    return False

def used_in_col(sudoku, col, num):
    for i in range(9):
        if sudoku[i][col] == num:
            return True
    return False

def used_in_box(sudoku, row, col, num):
    for i in range(3):
        for j in range(3):
            if sudoku[i + row][j + col] == num:
                return True
    return False

def check_position_safe(sudoku, row, col, num):
    box_row = row - row % 3
    box_col = col - col % 3
    return (
            (not used_in_row(sudoku, row, num)) and
            (not used_in_col(sudoku, col, num)) and
            (not used_in_box(sudoku, box_row, box_col, num))
    )

def solve_sudoku(sudoku):
    emptyList = [0, 0]

    if not find_empty_position(sudoku, emptyList):
        return True

    [row, col] = emptyList

    for num in range(1, 10):
        if check_position_safe(sudoku, row, col, num):
            sudoku[row][col] = num

            if solve_sudoku(sudoku):
                return True

            sudoku[row][col] = 0
    return False

def print_sudoku(sudoku):
    print("|------|------|------|")
    for i in range(9):
        print("|", end="")
        for j in range(9):
            print(sudoku[i][j], end=" ")
            if j % 3 == 2:
                print("|", end="")
        print()
        if i % 3 == 2:
            print("|------|------|------|")

if __name__ == '__main__':
    startTime = time.time()
    file = open("sudoku_inputs/evil03.txt", "r")
    sudoku = [[0 for x in range(9)] for y in range(9)]
    row = 0
    for line in file:
        if line.strip():
            sudoku[row] = [int(i) for i in line.strip()]
            row += 1

    if solve_sudoku(sudoku):
        print_sudoku(sudoku)
    else:
        print('No solution found')
    print("Execution Time: ", time.time() - startTime)