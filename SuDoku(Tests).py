# 18.5.2023
# SUDOKU prep

# a few test methods for handling Sudoku grids, just for fun
# (initialize the grid in memory; fill the grid randomly; partially erase the grid; display the grid)

# To-do: method to check whether it's a valid sudoku, including:
#        -- check whether certain subsets featuring all digits e.g. (1,1)(1,9) or (1,1)-(3,3) are valid



import random


                            # Method to initialize an empty grid as an 'array' (list of lists)
                            # grid[0] is not a list, it's simply the size of the grid
                            # From grid[1] to grid[9], each list has 0 as its zeroth element
                            #   (potentially, later, a running row total?)
                            #   (zeroth row could also store column totals, possibly)

                            # ... but for now, it's just to avoid zero indexing (I want my cells labelled (1-9,1-9))
def init_grid(grid):
                            # The x and y extents are the same, but, it's clearer to split them apart, I think
    x = grid[0]
    y = grid[0]
                            # Iterate through y (rows) first, then x (cols e.g. cells, per row)
    for y_iter in range(1,y+1):
                            # ... and make each row a LIST
        grid.append([])
                            # Add a zeroth element: zero for now, but like I say possibly use them later
        grid[y_iter].append(0)
                            # x-iter ...
        for x_iter in range(x):
                            # ... assign all cells from grid[1][1] to grid[9][9] a null placeholder
            grid[y_iter].append(None)



                            # Method fills a grid with entirely random numbers
                            # Does not create a valid grid (well, it might, but it's very unlikely)
def random_fill(grid,filled):
                            # Get the size; add one because of zero-indexing and forloops
                            # (I actually don't fully understand why it's necessary)
    size = grid[0] + 1
    for x in range (1,size):
        for y in range (1,size):
                            # Iterating over x and y to cover all cells, choose a random number between 1-9...
            n = random.randint(1,9)
                            # And assign it to the given cell
            grid[x][y] = n

                            # Method has now drawn a full grid.
                            # If the "filled %" argument was less than 100, simply erase random cells:
    if filled < 100:
        erase_cells(grid,100-filled)



                            # Method to erase a certain percentage of cells in a grid.
                            # Var 'empty' takes a value between 1 and 100
def erase_cells(grid,empty):
    size = grid[0]
    if empty < 0 or empty > 100:
        return
                            # Calculate a rounded integer value of cells to erase, from the percentage argument
    empty = int(empty/100 * grid[0]**2)
    e = 0
                            # Iterate up to the given value...
    while e < empty:
                            # ... choose a random cell...
        x = random.randint(1,size)
        y = random.randint(1,size)
                            # ... check that a cell hasn't *already* been erased...
        if grid[x][y]:
                            # ... and if not, erase it.
            grid[x][y] = None
                            # And, iterate to acknowledge that it's happened
            e += 1



                            # Method to print the grid as text
def display_grid(grid):
    print("\n")
                            # Get the variable for the size; add 1 because of the for-floops
    size = grid[0] + 1
    asciigrid = ""
                            # Nested iteration to cover every cell
    for x in range (1,size):
        for y in range (1,size):
            n = grid[x][y]
                            # For a start, if it's a blank cell, just draw a space
            if n == None:
                n = " "
                            # Otherwise, add the digit (with some cosmetic padding)
            asciigrid = asciigrid + "   " + str(n)
                            # Each line done, move onto a new line
        asciigrid = asciigrid + "\n"
                            # Finally, output the grid (rather than return it as a string)
    print(asciigrid)




if __name__ == "__main__":
                            # Sudoku will live in this variable
    grid = []
                            # This value -- grid[0] -- stores the side-length of the grid
                            # (grids are assumed to be square)
    grid.append(9)
                            # Initialize an empty grid
    init_grid(grid)
                            # Just testing for output: fill a grid up to the percantage given
                            # with entirely random numbers (not a valid sudoku)
    random_fill(grid,30)
                            # Display the grid laid out in a square
    display_grid(grid)
