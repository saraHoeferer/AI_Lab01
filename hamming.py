# Hemming Ansatz - h1
# check how many tiles are misplaced in start array in relation to goal array (h1)
def checkMisplacedTiles(array1, array2):
    # counter of misplaced tiles starts with zero
    counter = 0
    # as long the array goes
    for i in range(3):
        for j in range(3):
            # if the position of the elements is not the same as the goal array
            if array1[i][j] != array2[i][j]:
                # increment the counter
                counter += 1
    # return the counter
    return counter