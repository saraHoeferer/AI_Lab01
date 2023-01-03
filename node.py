class Node:
    # class constructor
    def __init__(self, state, depth, f_score):
        self.state = state
        self.depth = depth
        self.f_score = f_score

    # generate child nodes
    def generateChild(self):
        # get coordinates of Zero
        positions = getCoordinatesOfNumber(self.state, 0)

        # create a list of possible coordinates by moving Zero up, down, left right
        val_list = [[positions[0], positions[1] - 1], [positions[0], positions[1] + 1],
                    [positions[0] - 1, positions[1]], [positions[0] + 1, positions[1]]]

        # create an array for all the children
        children = []
        # for every single move the zero can do
        for i in val_list:
            # check if move is possible and if possible do the move
            child = self.shuffle(self.state, positions[0], positions[1], i[0], i[1])
            # if move was possible
            if child is not None:
                # create child with new state
                child_node = Node(child, self.depth + 1, 0)
                # append child to list
                children.append(child_node)
        # return children array
        return children

    # check if move is possbile
    def shuffle(self, data, x1, y1, x2, y2):
        # if possible
        if x2 >= 0 and x2 < len(self.state) and y2 >= 0 and y2 < len(self.state):
            # change position of zero
            temp_data = []
            temp_data = self.copy(data)
            temp = temp_data[x2][y2]
            temp_data[x2][y2] = temp_data[x1][y1]
            temp_data[x1][y1] = temp
            # return switched puzzle
            return temp_data
        else:
            # if move was not possbile return none
            return None

    # function to copy one matrix from another
    def copy(self, root):
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp

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