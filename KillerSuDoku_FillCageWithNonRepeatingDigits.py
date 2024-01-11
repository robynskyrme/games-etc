# 7.1.2024
# Given a cage in Killer SuDoku of n cells adding up to a total m,
# find the first possible solution within the rules (numbers 1-9 only, and no repeats within a cage)

# note on 7.1 @ 1739: This works, sometimes, but not always; for certain inputs it gets caught in a loop


import math

# The zeroth cell in the list gives the total sum
# The rest of the list is the cells in the cage on the grid:
# 1-9 only, and no repeated numbers within a cage
# e.g. [23,0,0,0] will find the first (and only) set of 3 distinct integers which sum to 23 [6+8+9]

test = [30,0,0,0,0]

def ValidArea(list):

    # check for zeroes
    has_zero = False
    cell = 1
    while has_zero == False:
        if list[cell] == 0:
            has_zero = True
            return False
        cell += 1
        if cell == len(list):
            has_zero = True

    # check for n>9
    has_toobig = False
    cell = 1
    while has_toobig == False:
        if list[cell] > 9:
            has_toobig = True
            return False
        cell += 1
        if cell == len(list):
            has_toobig = True

    # check for repeats
    ints_used = [0,0,0,0,0,0,0,0,0,0]
    for cell in range (1,len(list)):
        ints_used[list[cell]] += 1
        if max(ints_used) > 1:
            return False

    if not CorrectTotal(list):
        return False

    return True

def CorrectTotal(list):
    correct = False

    goal = list[0]
    total = sum(list)-goal

    if goal == total:
        correct = True

    return correct


def AdjustOneHigher(list):
    total = list[0]
    list[0] = 999

    cell = 1

    while cell < len(list):
        if list[cell] < 9:
            if list.count(list[cell]+1) == 0:
                list[cell] +=1
        cell += 1

    list[0] = total
    return list




def AdjustOneLower(list):
    total = list[0]
    list[0] = 999

    cell = 1

    while cell < len(list):
        if list[cell] > 1:
            if list.count(list[cell]-1) == 0:
                list[cell] -=1
                list[0] = total
                return list
        cell += 1

    list[0] = total
    return list


def Fix(list):
    FillWithAverage(list)

    cells = len(list)-1
    total = list[0]
    current_sum = sum(list) - list[0]

    while not ValidArea(list):
        print(list)
#        print(ValidArea(list))
        current_sum = sum(list) - total


        if current_sum < total:
            list = AdjustOneHigher(list)
        else:
            AdjustOneLower(list)

    return list

def FillWithAverage(list):
    cells = len(list)-1
    total = list[0]

    avg = math.floor(total/cells)

    for cell in range (1,cells):
        list[cell] = avg

    remainder = total-(avg*(cells-1))

    list[cells] = remainder

    return list



if __name__ == "__main__":

    print(test)
    test = Fix(test)
    print("\nSolution:")
    print(test)
