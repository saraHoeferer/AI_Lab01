# This is a sample Python script.
import random
import time
from node import *
from hamming import *
from manhattan import *


# function to create random start state
def initialiseStartArray(start_array):
    # list of available numbers to fill array with
    list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    inversion = 0
    # create 3 rows
    for i in range(3):
        row = []
        # fill rows with 3 entries each
        for j in range(3):
            # choose random number from list
            counter = random.choice(list)
            # put number chosen into row
            row.append(counter)
            # remove chosen number from array so it does not get chosen twice
            list.remove(counter)
        # check inversion score
        inversion = checkInversion(row, inversion)
        # append the start array with completed row
        start_array.append(row)

    return start_array, inversion


def checkInversion(row, inversion):
    # check inversion score from neighbors
    for i in range(0, 2):
        for j in range(i + 1, 3):
            # if a number is larger than the following ones inversion score increases
            if row[i] > row[j] and row[i] != 0 and row[j] != 0:
                inversion += 1
    return inversion


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

# function to print arrays
def printArrays(array):
    for i in range(3):
        for j in range(3):
            if j == 2:
                print(array[i][j])
            else:
                print(array[i][j], end=" ")

# function to check if two matrices are equal
def areEqual(arr1, arr2):
    for i in range(0, 3):
        for j in range(0, 3):
            if arr1[i][j] != arr2[i][j]:
                return False
    return True

def searchAlgorithm(start_array, goal_array, g_score, h_score):
    openList = []
    closedList = []
    # create start node
    start = Node(start_array, 0, g_score + h_score)
    # create openList and append start node
    openList.append(start)
    # access current element - first element of open List
    current = openList[0]
    # as long as current matrix and goal matrix are not the same
    while not areEqual(current.state, goal_array):
        current = openList[0]
        # increase g score
        g = current.depth + 1
        # print progress
        print("")
        print("  | ")
        print("  | ")
        print(" \\\'/ \n")
        printArrays(current.state)
        # for every child created
        for i in current.generateChild():
            cnt = 0
            # calculate distance
            h = checkDistanceFromGoalState(i.state, goal_array)
            # calculate f_score
            i.f_score = h + g
            # check if matrix is already in open List
            for j in range(len(openList)):
                if areEqual(i.state, openList[j].state):
                    cnt = 1
                    break
            for j in range(len(closedList)):
                if areEqual(i.state, closedList[j].state):
                    cnt = 1
                    break
            # if not
            if cnt == 0:
                # append open list with new matrix
                openList.append(i)
        # move current list into closed list
        closedList.append(current)
        # delete current state from open list
        del openList[0]

        # sort open list according to lowest f_score
        openList.sort(key=lambda x: x.f_score, reverse=False)

    # return solution
    return openList[0], len(openList) + len(closedList)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # goal array - solution
    goal_array = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    # empty start array
    start_array = []
    # empty close list
    closedList = []
    # empty open list
    openList = []
    # fill start array with random numbers
    finished_array = []
    start_array, inversion = initialiseStartArray(start_array)
    # print start array
    printArrays(start_array)
    if inversion % 2 == 0:
        # get coordinates for element 0
        coordinatesZero = getCoordinatesOfNumber(start_array, 0)
        # check how many tiles are misplaced in start array
        misplacedTiles = checkMisplacedTiles(start_array, goal_array)
        # check how many distances the tiles need to make to get form start array to goal array
        distance = checkDistanceFromGoalState(start_array, goal_array)

        # Hamming search algorithm
        # timeit.timeit()
        # finished_array = searchAlgorithm(start_array, goal_array, 0, misplacedTiles)
        # end_time = timeit.timeit()

        # Manhattan search algorithm
        start_time = time.time()
        finished_array, int = searchAlgorithm(start_array, goal_array, 0, distance)
        end_time = time.time()

        # print finished array + time
        print("")
        #printArrays(finished_array.state)
        print("")
        print(end_time-start_time)
        print(int)
    else:
        print("Puzzle not solvable")
    # print goal array
    # printArrays(goal_array)
