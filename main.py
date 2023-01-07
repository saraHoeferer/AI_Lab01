# This is a sample Python script.
import random
import time
from node import *
from hamming import *
from manhattan import *


# function to create random start state
def initialiseStartArray():
    # list of available numbers to fill array with
    list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    inversion = 0
    array = []
    inv = []
    # create 3 rows
    for i in range(3):
        row = []
        # fill rows with 3 entries each
        for j in range(3):
            # choose random number from list
            counter = random.choice(list)
            # put number chosen into row
            row.append(counter)
            if counter != 0:
                inv.append(counter)
            # remove chosen number from array so it does not get chosen twice
            list.remove(counter)
        # check inversion score
        # append the start array with completed row
        array.append(row)
    inversion = checkInversion(inv)
    return array, inversion


def checkInversion(inv):
    inversion = 0
    # check inversion score from neighbors
    for i in range(0, 8):
        for j in range(i + 1, 8):
            # if a number is larger than the following ones inversion score increases
            if inv[j] < inv[i]:
                inversion += 1
    return inversion


# function to print arrays
def printArrays(array):
    for i in range(3):
        for j in range(3):
            if j == 2:
                print(array[i][j])
            else:
                print(array[i][j], end=" ")

def checkAppearance(list, node):
    for nodes in list:
        if node.state == nodes.state:
            return True
    return False

def searchAlgorithm(start_array, goal_array, h_score, algorithm):
    # create start node
    current = Node(start_array, h_score, 5)
    openList = [current, ]
    closedList = []
    # create openList and append start node
    # access current element - first element of open List
    cnt = 0
    # as long as current matrix and goal matrix are not the same
    while current.h_score != 0:
        # for every child created
        for i in current.createChild(algorithm, goal_array):
            # check if matrix is already in open List
            alreadyOpen = checkAppearance(openList, i)
            alreadyClosed = checkAppearance(closedList, i)
            # if not
            if not alreadyOpen and not alreadyClosed:
                # append open list with new matrix
                openList.append(i)
        # move current list into closed list
        closedList.append(current)
        # delete current state from open list
        del openList[0]
        # sort open list according to lowest f_score
        openList.sort(key=lambda x:x.h_score, reverse=False)
        current = openList[0]
        cnt += 1
    # return solution
    return len(openList) + len(closedList)


def do100(goal_array):
    time_ham = 0
    time_man = 0
    sum_ham = 0
    sum_man = 0
    for i in range(100):
        start_array, inversion = initialiseStartArray()
        misplacedTiles = checkMisplacedTiles(start_array, goal_array)
        distance = checkDistanceFromGoalState(start_array, goal_array)

        while inversion % 2 != 0:
            start_array, inversion = initialiseStartArray()

        start_time_ham = time.time()
        sum_ham += searchAlgorithm(start_array, goal_array, misplacedTiles, "ham")
        end_time_ham = time.time()
        time_ham += end_time_ham-start_time_ham
        print("Ham:", i + 1)

        start_time_man = time.time()
        sum_man += searchAlgorithm(start_array, goal_array, distance, "man")
        end_time_man = time.time()
        time_man += end_time_man - start_time_man
        print("Man: ", i + 1)

    print("time Hamming: ", time_ham)
    print("time Manhattan: ", time_man)
    print ("Average nodes Ham: ", sum_ham/100)
    print("Average nodes Man: ", sum_man/100)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # goal array - solution
    goal_array = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    do100(goal_array)
