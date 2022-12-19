# This is a sample Python script.
import random

import numpy as np


def initialiseStartArray(start_array):  # function to create random start state
    list = [0, 1, 2, 3, 4, 5, 6, 7, 8]  # list of available numbers to fill array with

    for i in range(3):  # create 3 rows
        row = []
        for j in range(3):  # fill rows with 3 entries each
            counter = random.choice(list)  # choose random number from list
            row.append(counter)  # put number chosen into row
            list.remove(counter)  # remove chosen number from array so it does not get chosen twice
        start_array.append(row)  # append the start array with completed row
    return start_array  # return created array


# Hemming Ansatz - h1
def checkmisplacedTiles(array1, array2):  # check how many tiles are misplaced in start array in relation to goal array (h1)
    counter = 0  # counter of misplaced tiles starts with zero
    for i in range(3):  # as long the array goes
        for j in range(3):
            if array1[i][j] != array2[i][j]:  # if the position of the elements is not the same as the goal array
                counter += 1  # increment the counter
    return counter  # return the counter

# Manhatten Ansatz - h2
def checkDistancefromGoalState(array1, array2):  # function to calculate the distances form goal State (h2)
    counter = 0  # counter to check each number
    distance = 0  # distance calculated starts with zero

    while counter != 9:  # for each number in array (0-8)
        coordinatesStart = getCoordinatesOfNumber(array1, counter)  # get coordinates from number in start array
        coordinatesGoal = getCoordinatesOfNumber(array2, counter)  # get coordinates from number in goal array
        distance += (abs(coordinatesStart[0] - coordinatesGoal[0])) + (abs(coordinatesStart[1] - coordinatesGoal[1]))  # calculate the distances between both coordinates
        counter += 1  # increment the counter to calculate distance for next number
    return distance  # return calculated distance

def getCoordinatesOfNumber(array, number):  # function to get the coordinates of a certain number
    coordinates = [0, 0]  # empty array for coordinates
    for i in range(3):  # search as long as array goes
        for j in range(3):
            if array[i][j] == number:  # if array element is the number searched for
                coordinates[0] = i  # save coordinates
                coordinates[1] = j
                break
    return coordinates  # return coordinates

def swapElements(array, index1, index2):  # function to swap to array items
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp
    return array

def printArrays(array):  # function to print arrays
    for i in range(3):
        for j in range(3):
            if j == 2:
                print(array[i][j])
            else:
                print(array[i][j], end=" ")

def algorithmHemmning (array1, array2, f_score, g_score, h_score):
    # TODO implement algorithm
    return "";

def algorithmManhatten (array1, array2, f_score, g_score, h_score):
    # TODO implement algorithm
    return "";

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    goal_array = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]  # goal array - solution
    start_array = []  # empty start array
    closedList = []  # empty close list
    openList = []  # empty open list
    start_array = initialiseStartArray(start_array)  # fill start array with random numbers
    coordinatesZero = getCoordinatesOfNumber(start_array, 0)  # get coordinates for element 0
    misplacedTiles = checkmisplacedTiles(start_array, goal_array)  # check how many tiles are misplaced in start array
    distance = checkDistancefromGoalState(start_array, goal_array)  # check how many distances the tiles need to make to get form start array to goal array
    g_score = 0  # score of how step the algorithm already took - not sure how it works
    f_score_h1 = misplacedTiles + g_score  # f_score like used in https://blog.goodaudience.com/solving-8-puzzle-using-a-algorithm-7b509c331288
    f_score_h2 = distance + g_score

    printArrays(start_array)  # print start array
    print("Coordinates of Zero: ", coordinatesZero[0], " ", coordinatesZero[1])
    print("Misplaced Tiles: ", misplacedTiles)
    print("Sum of the distances of the tiles from their goal positions: ", distance)
    print("F-score for Misplaced Tiles: ", f_score_h1)
    print("F-score for Manhattan Distance: ", f_score_h2)
    print("\n")
    printArrays(goal_array)  # print goal array

