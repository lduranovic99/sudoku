import pprint

def solve(grid):
    """
    Solves the sudoku board using backtracking

    Parameters
    ----------
    grid: 2x2 int array
        the actual sudoku board

    Returns
    ---------- 
    boolean:
        True if board was solved
        False otherwise
    """
    empty_cell = find_empty(grid)
    if empty_cell:
        row, col = empty_cell
    else:
        return True

    for num in range(1,10):
        if (valid(grid, (row, col), num)):
            grid[row][col] = num
            
            if solve(grid):
                return True

            # backtrack if the number was wrong
            grid[row][col] = 0

    return False

def valid(grid, pos, num):
    """
    Checks whether the given value is valid to put in the given position

    Parameters
    ----------
    grid: 2x2 int array
        the actual sudoku board
    pos: tuple with coordinates of the position
    num: value to put in the given position

    Returns
    ---------- 
    boolean:
        true if the position is valid
        false otherwise
    """
    this_row = pos[0]
    this_col = pos[1]
    
    # Check column
    for row in range(9):
        if this_row == row:
            continue
        if grid[row][this_col] == num:
            return False

    # Check row
    for col in range(9):
        if this_col == col:
            continue
        if grid[this_row][col] == num:
            return False

    # Check the smaller box
    initial_row = int(this_row//3) * 3
    initial_col = int(this_col//3) * 3
    for row in range(initial_row, initial_row+3):
        for col in range(initial_col, initial_col+3):
            if row == this_row and col == this_col:
                continue
            field = grid[row][col]
            if field == num:
                return False
    
    return True


def find_empty(grid):
    """
    Finds an empty cell in the provided sudoku grid

    Parameters
    ----------
    grid: 2x2 int array
        the actual sudoku board

    Returns
    ----------  
    tuple with the empty position
    None if all positions are taken
    """
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col

    return None

board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 2],
    [6, 1, 0, 3, 0, 0, 0, 0, 0],
    [0, 2, 8, 4, 1, 0, 0, 0, 0],
    [0, 3, 4, 0, 2, 5, 6, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

printer = pprint.PrettyPrinter(width=41, compact=True)
print(solve(board))
printer.pprint(board)