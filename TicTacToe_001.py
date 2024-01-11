# 12.9.2023
# Tic Tac Toe, using classes and primes

# Using this as an excuse to experiment with classes -- especially since they didn't seem an obvious choice
# (and, as an excuse to try something using prime numbers -- especially since they didn't seem an obvious choice)

# Default is a 3x3 grid, use these keys to play:

#   •  •  •    =    q  w  e
#   •  •  •    =    a  s  d
#   •  •  •    =    z  x  c




                            # Okay, some useful globals

                            # grid size (eventually I want to experiment with larger grids)
size = 3
                            # we'll add players in a bit
players = []
                            # list of primes for analyzing the grid
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
                            # To be generated: the prime products which encode winning lines
gold = []
                            # Empty cell in the ASCII grid (non-space helpful for testing, also, looks pretty)
empty_cell = "•"
                            # Has the game been won? Not yet, obviously:
over = False



                            # each player's moves to be stored separately, in their own class
class Moves:
    def __init__(self,piece):
        self.piece = piece

        self.moves = []
        self.encoding = 1

                            # Make the list in which the player's moves will be stored an appropriate length
        for cell in range(size * size):
            self.moves.append(0)


def generate_codes():
    sum = 1
                            # List of winning lines will go: columns, rows, NW-SE diag, NE-SW diag
                            # each line will have a number associated to it: the product of the primes assigned it
                            # once list of codenumbers is generated, any grid which divides one perfectly is a winner

                            # Columns:
    for cols in range (size):
        for rows in range (size):
            pos = rows * size + cols
            sum = sum * primes[pos]
        gold.append(sum)
        sum = 1

                            # Rows:
    for rows in range(size):
        for cols in range(size):
            pos = rows * size + cols
            sum = sum * primes[pos]
        gold.append(sum)
        sum = 1

                            # NW-SE diagonal:
    for diag in range(size):
        pos = diag * size + diag
        sum = sum * primes[pos]
    gold.append(sum)
    sum = 1
                            # NE-SW diagonal:
    for diag in range(size):
        pos = diag * size + (size-1-diag)
        sum = sum * primes[pos]
    gold.append(sum)

    # print(gold)
    #


                            # Draw it out in ASCII
def display_board():
                            # Initial string to house it; empty
    output_board = ""
    cell = 0
                            # Traverse the board, across then down, checking each cell at a time
    for rows in range (size):
        output_board += " "
        for cols in range (size):
            output_board += " "
            output_board += get_cell(cell)
            output_board += " "
            cell += 1
        output_board += "\n"

    return output_board

                            # Function to report what a cell is on the board

def get_cell(cell):
    check = 0
    piece = ""
                            # Go through all players ...
    for player in range(len(players)):
        check += players[player].moves[cell]
        if players[player].moves[cell] == 1:
            piece = players[player].piece
                            # ... making sure only one occupies the given cell ...
    if check > 1:
        print ("ERROR")
        return
                            # ... returning a space for an empty cell ...
    if check == 0:
        return empty_cell
                            # ... or, for an occupied cell, the piece occupying it -- as a string
    if check == 1:
        return piece


                            # Add to the list of players a new player-object of class Moves, playing the specified piece
def add_player(piece):
                            # Another check for things that may come later: we are only playing with single characters
    if len(piece) > 1:
        return
                            # The character (playing piece) being acceptable, add that player!
    players.append(Moves(piece))


                            # Function to get the specified player to input their move
def get_move(player):
                            # for a 3x3 grid use the letters in vaguely the right shape, the left of the keyboard
    if size == 3:
        valid = "qweasdzxc"
        move = " "
        cell = 0
                            # i.e., keep asking until user inputs one of the nine relevant letters
                            # [THIS BIT IS BROKEN ACTUALLY but too annoying to fix rn; it doesn't matter really]
        while valid.count(move) == 0:
            move = input("Player " + players[player].piece + " plays...    ")
            cell = valid.index(move)
                            # also, refuse (invalidate) input if cell already occupied
            if get_cell(cell) != empty_cell:
                move = " "

        return cell
    else:
                            # to be ignored for now -- experimental "just numbers" input for exotic (non-3) grids lol
        move = input("Player " + players[player].piece + " plays...    ")
        cell = int(move)
        return cell-1

                            # Play a move! Takes a player, and the cell, and alters the player's grid accordingly
                            # and: returns TRUE if that move is a winning move
def play_move(player,cell):
    win = False
    players[player].moves[cell] = 1
                            # and, updates the prime product encoding of the player's grid
    players[player].encoding *= primes[cell]
                            # ... and if that new encoding divides any of the winning lines...
    win = did_it_win(player)
                            # then that's returned to the main module, which ends the game
    return win


def did_it_win(player):
    answer = False
                            # Let's check that, though...
    for line in gold:
                        # if the player's grid encoding exactly divides one of the prime products, they've won
        if players[player].encoding % line == 0:
            answer = True
            return answer




                            # Function to output *something* at the end of everything

def winner(player):
    print("==============")
    print("PLAYER " + players[player].piece + " WINS!")
    print("==============")


def gameplay():
    over = False
    player = len(players)-1
    generate_codes()

    while not over:
        player += 1
        player = player % len(players)
        move = get_move(player)
        over = play_move(player,move)
        # print("Player " + players[player].piece + " played " + str(move))
        print("\n" + display_board() + "\n\n")


    player = player % len(players)

    winner(player)


if __name__ == "__main__":
                            # Let's be a bit hospitable: tell the user what we/they are up to, and show the empty board
    print("TIC TAC TOE")
    print("\n" + display_board())

                            # Just two players, for now
    add_player("O")
    add_player("X")


                            # Haway the lads
    gameplay()