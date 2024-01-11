# 30.8.2023
# Basic TicTacToe

# Just ASCII for now, to get the code working; next step will be to make a GUI for it


                            # This is the grid
TTT = []
                            # set characters to draw with
cells = [" ", "O", "X"]

                            # Fill it with blank squares
def initialize_TTT():

    for cell in range (9):
        TTT.append(0)


                            # FUNCTION to display current grid
def display_TTT():
                            # init some variables
    grid = ""
    across = 0
    down = 0

                            # traverse grid row by row col by col
    while down < 3:
        while across < 3:
            cell = down * 3 + across
                            # add to a string whatever is in the cell
            grid += cells[TTT[cell]]
            across += 1
        down += 1
                            # newline when necessary; and reset 'across' to 0 for each row
        grid += "\n"
        across = 0

                            # output string
    print(grid)


                            # FUNCTION to check if there are any lines of 3 identical symbols

def isline(a,b,c):
    player = 0
    line = False
    if TTT[a] == TTT[b] and TTT[b] == TTT[c] and TTT[c] != 0:
        player = TTT[a]
        line = True

    return line,player


                            # FUNCTION to check if a completed line exists
def check_lines():
    player = 0
                            # Manually check each row....
    ABC = isline(0,1,2)
    if ABC[0]:
        player = ABC[1]

    DEF = isline(3,4,5)
    if DEF[0]:
        player = DEF[1]

    GHI = isline(6,7,8)
    if GHI[0]:
        player = GHI[1]
                            # And each column...
    ADG = isline(0,3,6)
    if ADG[0]:
        player = ADG[1]

    BEH = isline(1,4,7)
    if BEH[0]:
        player = BEH[1]

    CFI = isline(2,5,8)
    if CFI[0]:
        player = CFI[1]

    AEI = isline(0,4,8)
    if AEI[0]:
        player = AEI[1]

    CEG = isline(2,4,6)
    if CEG[0]:
        player = CEG[1]

    if player > 0:
        print(cells[player] + " wins!")

    return player

def playmove(cell):
                        # Assume for now, user is player 1 (noughts; O rather than X)
    TTT[cell] = 1

if __name__ == "__main__":
    initialize_TTT()

    won = False

    while not won:
        display_TTT()
        play = input("? ")
        play = int(play)-1
        playmove(play)
        display_TTT()
        if check_lines() != 0:
            won = True
