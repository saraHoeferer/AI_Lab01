# this file is used to calculate the h_score using the Hamming approach

# the function checks how many tiles are misplaced in the current state in relation to goal array - solution
def checkMisplacedTiles(currentState, goalState):
    # the inputs are the state (puzzle) of the node currently looked at an the goal array (solution)
    # counter of misplaced tiles starts with zero
    misplacedTilesCounter = 0
    # as long the array goes
    for i in range(3):
        for j in range(3):
            # if the position of the elements is not the same as the goal array
            if currentState[i][j] != goalState[i][j]:
                # increment the counter
                misplacedTilesCounter += 1
    # return the counter
    return misplacedTilesCounter
