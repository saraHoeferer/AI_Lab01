from hamming import *
from manhattan import *
from main import getCoordinatesOfNumber

# this file is used for all functions and operations used by the Node class
# To create the algorithm and the Node class we oriented us on the structure from:
# https://blog.goodaudience.com/solving-8-puzzle-using-a-algorithm-7b509c331288
# We changed the class as well as the functions to serve the needs of our algorithm

class Node:
    # class constructor
    def __init__(self, state, h_score, move):
        # the inputs are the state (so a certain puzzle state), the h_score (depending on the heuristic used)
        # and the move (its move the zero made to create the state the node has (so basically the previous move))
        self.state = state
        self.h_score = h_score
        self.previousMove = move

    # this function is used to generate the child nodes
    def createChild(self, heu, goal_array):
        # the inputs are the heuristic being used and the goal array (solution)

        # first we get the coordinates of Zero
        positions = getCoordinatesOfNumber(self.state, 0)

        # then we create a list of possible coordinates by moving Zero up, down, left and right
        moveList = [[positions[0] - 1, positions[1]], [positions[0] + 1, positions[1]],
                    [positions[0], positions[1] - 1], [positions[0], positions[1] + 1]]

        # create an array for all the children
        children = []
        # and we initialise the move variable - it is used to track what move the child made
        # 0 - up, 1 - down, 2 - left and 3 - right
        move = 0
        # for every single move the zero can do
        for i in moveList:
            # check if move is possible and if possible do the move
            if self.checkMove(i, move):
                # if the move was possible we change the state of the puzzle by swapping the Zero according to the
                # movement
                child = self.swapZero(self.state, positions[0], positions[1], i[0], i[1])
                # we then create child with new state and calculate the h_score according to the heuristic chosen
                if heu == "Hamming":
                    child_node = Node(child, checkMisplacedTiles(child, goal_array), move)
                else:
                    child_node = Node(child, checkDistanceFromGoalState(child, goal_array), move)
                # and append child to list
                children.append(child_node)
            # and increase the move by one
            move += 1
        # return children array
        return children

    # this function is used to validate the move the zero wants to do
    def checkMove(self, coordinates, move):
        # the inputs are the coordinates to which we want to swap the zero and the move that is done by this swapping
        # (up, down, left or right)

        # we first need to check if the coordinates are inside of the array
        if 0 <= coordinates[0] < 3 and 0 <= coordinates[1] < 3:
            # if the coordinates are not out of bound we need to check if the move we want to do is not the move
            # previously done (so no loops occur)

            # if a move is the exact opposite of the move done before (so up-down and left-right) we return False
            # 0 - up, 1 - down, 2 - left and 3 - right
            if move == 0 and self.previousMove == 1:
                return False
            elif move == 1 and self.previousMove == 0:
                return False
            elif move == 2 and self.previousMove == 3:
                return False
            elif move == 3 and self.previousMove == 2:
                return False
            else:
                # else the move is possible and therefore we return True
                return True
        else:
            # if the coordinates are out of bound of the array we return False
            return False

    # this function is used to swap the placement of the zero to move form the parent state into the child state
    def swapZero(self, state, x1, y1, x2, y2):
        # the inputs give are the state (so how the puzzle looks at the moment) and x1 and y1 the coordinates of zero
        # of new position and x2, y2 the coordinates of zero of the old position

        # first we copy the data from the parent state
        temp_state = self.copy(state)

        # then we perform the swap
        temp = temp_state[x2][y2]
        temp_state[x2][y2] = temp_state[x1][y1]
        temp_state[x1][y1] = temp

        # and return switched puzzle
        return temp_state

    # function to copy one matrix from another
    def copy(self, root):
        # the inputs is the root matrix which is used to copy all values of it into a new array
        # a new array is created
        array = []
        # for how many rows root has
        for i in root:
            # a new row is created
            row = []
            # for how many values a row has
            for j in i:
                # the value is copied
                row.append(j)
            # and the row is append to the array
            array.append(row)
        # the copied array gets returned
        return array
