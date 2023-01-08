from main import getCoordinatesOfNumber


# this file is used to calculate the h_score using the Manhattan approach

# function that calculates the distances each number needs to take till it reaches its goal position
def checkDistanceFromGoalState(currentState, goalState):
    # the inputs are the state (puzzle) of the Node currently looked at and the goal array (the solution)
    # distance calculated starts with zero
    distance = 0
    # for each number in array (0-8)
    for i in range(0, 9):
        # get coordinates from number in State of the current node
        coordinates_current = getCoordinatesOfNumber(currentState, i)
        # get coordinates from number in goal array
        coordinates_goal = getCoordinatesOfNumber(goalState, i)
        # calculate the distances between both coordinates
        distance += (abs(coordinates_current[0] - coordinates_goal[0])) + (
            abs(coordinates_current[1] - coordinates_goal[1]))
    # return calculated distance
    return distance
