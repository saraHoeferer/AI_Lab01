import random
import time
import math
from node import *
from hamming import *
from manhattan import *


# function to create random a start state
def initialiseStartArray():
    # no inputs needed
    # list of available numbers to fill array with
    numbersToBeChosen = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    # empty array that is used to create start array - Two Dimensional
    TD_startArray = []
    # empty array used to check the inversion - One Dimensional
    OD_startArray = []
    # first we create 3 rows
    for i in range(3):
        # and an empty row array
        row = []
        # then we fill the rows with 3 entries each
        for j in range(3):
            # choose random number from list
            randomNumber = random.choice(numbersToBeChosen)
            # put number chosen into row
            row.append(randomNumber)
            # check that the number chosen is not zero, since zero is not included in the inversion calculation
            if randomNumber != 0:
                # if any other number than zero we add it to the inversion array
                OD_startArray.append(randomNumber)
            # remove chosen number from list so it does not get chosen twice
            numbersToBeChosen.remove(randomNumber)
        # after a whole row was created it gets appended to start array
        TD_startArray.append(row)
    # after whole array was created we check the inversion with the one dimensional copy of the array
    inversion_score = checkInversion(OD_startArray)
    # then we return the array and the inversion score
    return TD_startArray, inversion_score


# function to check the inversion score of a given random start state the inversion score is needed since a puzzle
# with an uneven inversion score is not solvable - therefore this function actually checks
# if a puzzle is solvable or not
def checkInversion(OD_startArray):
    # the input is the start state reformatted into a one dimensional array instead of an two dimensional array
    # we set the inversion_score to zero
    inversion_score = 0
    # we want to check if the neighbors of number is smaller than the one inspected
    # therefore we check the whole array
    for i in range(0, 8):
        # and check each neighbor
        for j in range(i + 1, 8):
            # if the number currently inspected (i) is larger than their neighbors
            if OD_startArray[j] < OD_startArray[i]:
                # the score is increased by one
                inversion_score += 1
    # after checking the whole array we return th inversion score
    return inversion_score


# function to print arrays
def printArrays(array):
    # the input is the array which should be printed
    # for each row
    for i in range(3):
        # and for each collum
        for j in range(3):
            # we check if the array is at the end of the row
            if j == 2:
                # if so we print the respective value with a "\n" included next to it
                print(array[i][j])
            else:
                # if the respective value is not at the end we print it with a " " included next to it
                print(array[i][j], end=" ")
    # there is no return values since this function only prints arrays


# function to get the coordinates of a certain number
def getCoordinatesOfNumber(array, number):
    # the inputs are the array in which a certain number should be found and the number to be found
    # empty array for coordinates
    coordinates = [0, 0]
    # search as long as array goes
    for i in range(3):
        for j in range(3):
            # if array element is the number searched for
            if array[i][j] == number:
                # save coordinates and return them
                coordinates[0] = i
                coordinates[1] = j
                return coordinates
    # if no such coordinates were found we return False
    return False


# function to check if a node created has the same state (start_array) as one created before
def checkAppearance(list, node):
    # the inputs are the list with certain states that should be checked and the node that was newly created
    # for each item in the list
    for item in list:
        # we check if the item has a state that is equal to the state from the node being checked
        if node.state == item.state:
            # if a already existent item and the newly created node share the same state - True is returned
            return True
    # if no such item could be found which shares the same state with the newly created node - False is returned
    return False


# function to solve the 8 puzzle by expanding the tree with children and checking if one of them is the solution
# this function is the core of the whole programme - the algorithm
def searchAlgorithm(start_array, goal_array, heuristic):
    # the inputs are the random start_array, the goal_Array which holds the solution, and the heuristic chosen to
    # calculate with first we create a node to start with

    # first we check which heuristic was chosen to determine which h_score to calculate
    # the h_score is the factor on which we choose the next node to work with
    # at the beginning only one node is created therefore we immediately choose this one
    if heuristic == "Hamming":
        # if hamming was chosen we calculate the h_score as how many tiles are misplaced in the current state
        current = Node(start_array, checkMisplacedTiles(start_array, goal_array), 5)
    else:
        # if manhattan was chosen we calculate the h_score as how many distances each tile needs to make till it
        # reaches its final position
        current = Node(start_array, checkDistanceFromGoalState(start_array, goal_array), 5)
    # the we create a list with all nodes that have been created but no checked yet
    # (checked means that we look if the node we created is already the solution)
    openList = [current, ]
    # and a list with all nodes that have already been checked
    closedList = []
    # as long as the current h_score of the node we look at is not zero (no solution found yet)
    while current.h_score != 0:
        # we create as many children as possible (max. 4)
        # a child is determined by the movement of the zero position
        for i in current.createChild(heuristic, goal_array):
            # for every child created by the current/parent node
            # we check if state (array) is already in open List
            alreadyOpen = checkAppearance(openList, i)
            # or if its already in the closed list
            alreadyClosed = checkAppearance(closedList, i)
            # if it is not found in either one of them
            if not alreadyOpen and not alreadyClosed:
                # append open list with node
                openList.append(i)
        # then we move current node into closed list - since it is now checked
        closedList.append(current)
        # and delete current node from open list
        del openList[0]
        # then we sort open list according to lowest h_score
        openList.sort(key=lambda x: x.h_score, reverse=False)
        # and the current node becomes the first node in the open list - so the one with the lowest h_score
        current = openList[0]
    # after a node was found which h_score equals zero we return the amount of created nodes
    return len(openList) + len(closedList)


# this function is used to solve 100 random puzzles using the hamming and manhattan method and measuring the time
# needed to solve them
def do100(goal_array, heuristics):
    # the inputs are the goal_array - the solution and an array of the heuristics being used
    # for each heuristic that is used
    for heu in heuristics:
        # we create a sum of nodes created and set it to zero
        sumOfNodesCreated = 0
        # we create an array to time all the puzzles
        arrayTimes = []
        # an create variables for the mean deviation and the variance (used for standard deviation)
        sumMeanDeviation = 0
        sumVariance = 0
        # the we run our searchAlgorithm 100 times
        for i in range(100):
            # we set a start array and an inversion_score
            start_array, inversion_score = initialiseStartArray()
            # as long as a puzzle randomly created is not solvable
            while inversion_score % 2 != 0:
                # we create a new one and check the inversion_score again
                start_array, inversion_score = initialiseStartArray()
            # we time the solving of one puzzle
            start_time_one = time.time()
            # after we found a solvable puzzle we start the algorithm by handing over the start_array, the goal_array
            # and the heuristic being used
            sumOfNodesCreated += searchAlgorithm(start_array, goal_array, heu)
            # we stop the time for one puzzle
            end_time_one = time.time()
            # and expand the array with the duration needed for solving one puzzle
            arrayTimes.append(end_time_one-start_time_one)
        # After solving 100 puzzles we then calculate the sum of Mean Deviation
        for i in range(len(arrayTimes)):
            sumMeanDeviation += arrayTimes[i]
        # and divide it by 100 (the amount of puzzles solved
        sumMeanDeviation = sumMeanDeviation/100
        # and then we calculate the sum of variance
        for i in range(len(arrayTimes)):
            sumVariance += (arrayTimes[i]-sumMeanDeviation)**2
        # and divide it by 100
        sumVariance = sumVariance/100

        # then we print the time used and the average nodes created
        print("Time needed to solve 100 8-Puzzles using ", heu, ": %.3f" % (sumMeanDeviation*100), "seconds. Average nodes created: ", sumOfNodesCreated / 100)
        # the Mean deviation
        print("Mean deviation in ", heu, ": %.3f" %(sumMeanDeviation))
        # and the Standard deviation
        print("standard deviation in", heu, ": %.3f" %math.sqrt(sumVariance/100))


# the main is only used to run the do100 function
if __name__ == '__main__':
    # we create a goal array - solution
    goal_array = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    # and start the function by handing over the goal array and the heuristics we want to use
    do100(goal_array, ["Hamming", "Manhattan"])