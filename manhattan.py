# Manhatten Ansatz - h2
# function to calculate the distances form goal State (h2)
def checkDistanceFromGoalState(array1, array2):
    # counter to check each number
    counter = 0
    # distance calculated starts with zero
    distance = 0
    # for each number in array (0-8)
    while counter != 9:
        # get coordinates from number in start array
        coordinatesStart = getCoordinatesOfNumber(array1, counter)
        # get coordinates from number in goal array
        coordinatesGoal = getCoordinatesOfNumber(array2, counter)
        distance += (abs(coordinatesStart[0] - coordinatesGoal[0])) + (
            # calculate the distances between both coordinates
            abs(coordinatesStart[1] - coordinatesGoal[1]))
        # increment the counter to calculate distance for next number
        counter += 1
    # return calculated distance
    return distance

# function to get the coordinates of a certain number
def getCoordinatesOfNumber(array, number):
    # empty array for coordinates
    coordinates = [0, 0]
    # search as long as array goes
    for i in range(3):
        for j in range(3):
            # if array element is the number searched for
            if array[i][j] == number:
                # save coordinates
                coordinates[0] = i
                coordinates[1] = j
                break
    # return coordinates
    return coordinates