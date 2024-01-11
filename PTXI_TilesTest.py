# 14.4.2023
# Plague Tiles Eleven ------ test code for handling tiles

import random

ptxi = []


class pt:

    def __init__(self, word, y):
        self.word = word
        self.y = y

def random_letters(q):
    string = ""
    for count in range(q):
        r = random.randint(0,25) + 65
        string = string + chr(r)
    return string



def generate_tiles():
    tile_size = ptxi[0]

    for t in range(11):
        word = random_letters(tile_size)
        max = tile_size-2
        min = max-(max*2)
        y = random.randint(min,max)
        ptxi.append(pt(word,y))

    ptxi[1].y = 0


def draw_tiles():
    tile_size = ptxi[0]
    tempgrid = []
    grid = "\n\n"

    origin = 0
    track = 0

    for j in range(11):
        j = j + 1
        track = track + ptxi[j].y
        if track < origin:
            origin = track

    ypos = abs(origin)
    for j in range(11):
        j = j + 1

        word = ""

        word = ptxi[j].word
        ypos = ypos + ptxi[j].y
        word = word.rjust(len(word)+ypos," ")
        tempgrid.append(word)

    # for k in range(11):
    #     print(tempgrid[k]) # + " " + str(ptxi[k+1].y))

    extent = len(min(tempgrid))

    for k in range(11):
        tempgrid[k] = tempgrid[k].ljust(extent," ")

    # for k in range(11):
    #      print(tempgrid[k]) # + " " + str(ptxi[k+1].y))

    for y in range(extent):
        for x in range(11):
            grid = grid +  "   " + tempgrid[x][y]
        grid = grid + "\n"

    print(grid)

if __name__ == "__main__":

    tile_size = 5
    ptxi.append(tile_size)

    generate_tiles()

    draw_tiles()
