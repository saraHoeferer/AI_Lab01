from hamming import *
from manhattan import *


class Node:
    # class constructor
    def __init__(self, state, h_score, move):
        self.state = state
        self.h_score = h_score
        self.previousMove = move

    # generate child nodes
    def createChild(self, heu, goal_array):
        # get coordinates of Zero
        positions = getCoordinatesOfNumber(self.state, 0)

        # create a list of possible coordinates by moving Zero up, down, left right
        moveList = [[positions[0] - 1, positions[1]], [positions[0] + 1, positions[1]],
                    [positions[0], positions[1] - 1], [positions[0], positions[1] + 1]]

        # create an array for all the children
        children = []
        # for every single move the zero can do
        cnt = 0
        for i in moveList:
            # check if move is possible and if possible do the move
            if self.checkMove(i, cnt):
                child = self.swapZero(self.state, positions[0], positions[1], i[0], i[1])
                # create child with new state
                if heu == "ham":
                    child_node = Node(child, checkMisplacedTiles(child, goal_array), cnt)
                else:
                    child_node = Node(child, checkDistanceFromGoalState(child, goal_array), cnt)
                # append child to list
                children.append(child_node)
            cnt += 1
        # return children array
        return children

    def checkMove(self, moveList, move):
        if 0 <= moveList[0] < len(self.state) and 0 <= moveList[1] < len(self.state):
            # move 0 - up, 1 - down, 2 - left, 3 - right
            if move == 0 and self.previousMove == 1:
                return False
            elif move == 1 and self.previousMove == 0:
                return False
            elif move == 2 and self.previousMove == 3:
                return False
            elif move == 3 and self.previousMove == 2:
                return False
            else:
                return True
        else:
            return False

    def swapZero(self, data, x1, y1, x2, y2):
        temp_data = self.copy(data)
        temp = temp_data[x2][y2]
        temp_data[x2][y2] = temp_data[x1][y1]
        temp_data[x1][y1] = temp
        # return switched puzzle
        return temp_data

    # function to copy one matrix from another
    def copy(self, root):
        array = []
        for i in root:
            row = []
            for j in i:
                row.append(j)
            array.append(row)
        return array


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
                return coordinates
    # return coordinates
    return False
