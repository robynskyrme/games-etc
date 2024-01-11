# 25.3.2023
# Plague Tiles Eleven [sketch]
#
# "Plague Tiles Eleven" is a game which arrived (with that name) in a dream, a few months ago.
# This code is a warm-up for how to store, alter, and output the states of that game, without much actual gameplay yet.
#
# I don't think the game, as I dreamt it, will be interesting. It only has one solution and it's probably not fun to get to it.
# But won't find out until I can play it, so that's the reason for coding it. Perhaps then tweak it later so make it more enjoyable.
#
# This code is practice for output and moves -- it generates a set of tiles of size n (given in __main__) entirely randomly,
# and just lets you move them up and down.
#
# Limits/goals of this version are:
# -- that the 'grid space' is entirely fixed from the start, and tiles can be moved only within that space
# -- no attention paid to overlap with neighbour tiles; if I'd done that, the prior remark wouldn't be true
# -- does not generate a playable game: the letters are random, there's no attempt to create a tile-set with a solution
#
#
# -------------------------------------------
#
# THE GAME
#
#   Setup:
#
#   In Plague Tiles Eleven a 'tile' is a vertical concatenation of n distinct letters
# (as if n Scrabble tiles have been sellotaped together)
# e.g. for n = 3
#
#      j
#      f
#      b
#
# is one tile.
#
# Eleven such tiles are placed next to each other randomly such that they overlap by at least one letter,
# e.g. for n = 5
#
#                        f                   u    j    h
#              n         t         c         a    d    s    a
#              r    k    c         s         g    p    q    d
#         s    x    e    c    c    o         u    d    c    b
#         k    g    y    c    m    z    i    p    i    n    l
#         a    h    h         z    w    y                   r
#         a         m         g         m
#         b                   i         z
#                                       n
#
#
# Gameplay:
#
#   Tiles can be individually shifted up or down but MUST overlap horizontally with a neighbour tile.
#
#
# Goal:
#
#   Tiles are generated such that there is _exactly one_ configuration with two horizontal words which:
# 1) overlap by 1 letter; and
# 2) reach to both edges, e.g.
#
# (solution for this game is this configuration showing "DISTANT"/"FOXES", solutions from here on in uppercase)
#
#                                  g                        c
#                                  u                        a
#         b              p         d              w    i    s
#         d    k    k    s    D    I    S    T    A    N    T
#         F    O    X    E    S    m    f    a    p    f    q
#         l    y    u    c    a         u    m    f    b
#         c    z    b    m    i         t    u    g    z
#              b    f         r         h    e
#
#
# ... and the goal of the game (as dreamt) was:
# Achieve that unique solution in the fewest moves.
#
# Once I can actually play the game, that goal will need to be tightened up, I expect.
#
#
# Notes:
#
#   Letters which are not part of the solution can be generated, using a wordlist, to be red herrings:
# it should _look like there are other solutions_. But it's crucial that there should not be any other solutions
# so that will need checking somehow.
#
#   There are always eleven tiles; that's non-negotiable. The dream said so! But a possible upgrade would be:
# Play the game first with tiles of size 2 (fairly easy):
#
#                             b         a    t    y         e
#         i    s    j    B    U    I    L    D    I    N    G
#         T    R    A    P         k                   l
#
#
# Then move on to size 3, a little harder:
#
#                             y    b              p
#         B    E    A    R    D    S         d    t    f    w
#         v    y    d    g    a    C    A    T    N    I    P
#         u    l    j    b              i    e         e    f
#                                       n
#
# Then move on to size 5 (harder). Then, move on to size 7. The five tile sizes are the primes to 11, so,
# the final stage would be to play Plague Tiles Eleven with tiles of size 11: really ridiculously hard.
#
# You can resign at any point. But for each success at a given level of difficulty (tile size)
# you add to your score. Maybe?
#
# The game should _know_ the fewest moves required for the solution to a given set of tiles.
# Perhaps if you achieve exactly that, your score is doubled: I don't know yet. Things like that I'll figure out
# when the game is playable.
#
# Possible rules for the game's dictionary (it'll need one):
# -- words must be at least letters 3 long (?? i think 2 may also be ok, but that would involve recognizing 10-letter words)
# -- no proper nouns
# -- no hyphenated or apostrophized words




import random

plague_tiles = []
pt_memory = []

class plague_tile:
                            # Class for a tile includes the letters of the tile (word); its vertical shift from the top (zero);
                            # and godown is a boolean for whether it, currently, is moving upward or downward
                            #
                            # (in this warm-up of the game with a single keystroke input per tile, that's necessary --
                            # -- in some possible version where you can move up or down at will, it wouldn't be)
    def __init__(self,word,pos,godown):
        self.word = word
        self.pos = pos
        self.godown = godown

def generate_tiles(q):
                            # Create array of 11 blank strings
    for pte in range(11):
        plague_tiles.append(plague_tile("",0,True))
        pt_memory.append(plague_tile("", 0, True))

    word = ""
    for pte in range(11):
        word = ""
        for c in range(q):
            word = word + chr(random.randint(97,122))
            plague_tiles[pte].word = word

    plague_tiles.append(q)



def randomize_positions():
    grid_height = plague_tiles[11]
    ppos = grid_height-1

    for pte in range(11):
        r = random.randint(0,ppos)
        plague_tiles[pte].pos = r
        #print(plague_tiles[pte].pos)
        if len(plague_tiles[pte].word) + r > grid_height:
            grid_height = len(plague_tiles[pte].word) + r

    plague_tiles[11] = grid_height


def shift_position(tile):
    tile = tile - 1
    if plague_tiles[tile].pos == 0:
        plague_tiles[tile].godown = True
    if plague_tiles[tile].pos == plague_tiles[11]-len(plague_tiles[0].word):
        plague_tiles[tile].godown = False

    if plague_tiles[tile].godown:
        plague_tiles[tile].pos = plague_tiles[tile].pos + 1
    else:
        plague_tiles[tile].pos = plague_tiles[tile].pos - 1



def draw_tiles():
    grid = "\n\n     Plague Tiles Eleven (layout only)\n\n     1    2    3    4    5    6    7    8    9    0    -    (keys)\n     1    2    3    4    5    6    7    8    9   10   11\n\n\n"
    for pte in range(11):
        pt_memory[pte].word = plague_tiles[pte].word
        plague_tiles[pte].word = plague_tiles[pte].word.rjust(plague_tiles[pte].pos+len(plague_tiles[pte].word))

    for pte in range(11):
        plague_tiles[pte].word = plague_tiles[pte].word.ljust(plague_tiles[11])
        #print(plague_tiles[pte].word)

    for rows in range(plague_tiles[11]):
        grid = grid + "     "
        for cols in range(11):
            #print(str(rows)+", " + str(cols))
            grid = grid + plague_tiles[cols].word[rows] + "    "
        grid = grid + "\n"

    print(grid)
    for pte in range(11):
        plague_tiles[pte].word = pt_memory[pte].word






if __name__ == "__main__":

    tile_size = 5

    generate_tiles(tile_size)

    randomize_positions()

    draw_tiles()

    whatnext = ""
    acceptable = ["1","2","3","4","5","6","7","8","9","0","-"]

    while whatnext != "q":
        whatnext = input()
        if whatnext in acceptable:
            if whatnext == "0":
                whatnext = "10"
            if whatnext == "-":
                whatnext = "11"
            shift_position(int(whatnext))
            draw_tiles()