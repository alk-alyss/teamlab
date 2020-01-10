
class Node():
    '''A class for storing node info'''
    def __init__(self, pos= None, parent= None):
        self.pos = pos  # Position as (row, column) in maze
        self.parent = parent  # Parent node
        self.f = 0 # Sum of g & h
        self.g = 0 # Cost from start to current point
        self.h = 0 # Predicted cost from current point to the end 

    def __eq__(self, other):
        '''Compares the possitions'''
        return self.pos == other.pos


def astar(maze, startPos, endPos):
    '''Returns a list of tuples as a path from the startPos to the endPos in the maze'''
    openList = []  # Create the open list (σημεια που θα κοιταξει στο αμεσο μέλλον - γειτονικα του closeList) 
    closedList = []  # Create the closed list (σημεια που εχει ηδη κοιταξει)

    startNode = Node(startPos) # Define the start node
    endNode = Node(endPos)  # Define the end node

    openList.append(startNode) # Add the start node to the open list

    while len(openList) > 0:  # While the open list is not empty
        # Find the node with the lowest f cost in the open list 
        currentNode = openList[0]
        for node in openList:
            if node.f < currentNode.f:
                currentNode = node
        
        # Remove the current node from the open list and add it to the closed list
        openList.remove(currentNode)
        closedList.append(currentNode)

        # If the current node is the end node return the path that leads to the current node by looking at the parrents
        if currentNode == endNode:
            path = []
            while currentNode.parent is not None:
                path.append(currentNode.pos)
                currentNode = currentNode.parent
            path.append(startNode.pos)
            return path[::-1]

        # Find all the adjacent valid children to the current node
        children = []

        for addPos in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            newPos = (currentNode.pos[0] + addPos[0],
                      currentNode.pos[1] + addPos[1])

            # Check if the child is out of bounds
            if newPos[0] > len(maze) - 1 or newPos[0] < 0 or newPos[1] > (len(maze[len(maze) - 1]) - 1) or newPos[1] < 0:
                continue
            
            # Check if the child is a wall
            if not maze[newPos[0]][newPos[1]]:
                continue

            # Add the child to the children list
            children.append(Node(newPos, currentNode))

        # Calculate G, H and F cost for the children
        for child in children:
            # If the child is in the closed list skip it
            if child in closedList:
                continue

            child.g = currentNode.g + maze[currentNode.pos[0]][currentNode.pos[1]]
            child.h = endNode.pos[0]-child.pos[0]+endNode.pos[1]-child.pos[1]
            child.f = child.g + child.h

            # If the child is already in the open list, but with higher g cost, skip it
            for openNode in openList:
                if child == openNode and child.g >= openNode.g:
                    break

            # Add the child to the open list
            else:
                openList.append(child)

    # If the open list is empty there is no possible path
    return 'No path found'


def main():
    maze = [[1, 1, 1, 1, 0, 1, 1, 1, 1, 1],  # # = weighted free space
            [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],  # (higher number = more difficult to pass from there)
            [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],  # 0 = wall
            [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 3, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 0, 1, 1, 1]]

    startPos = (2, 1)
    endPos = (7, 8)

    path = astar(maze, startPos, endPos)
    print(path)

    # Console print out of the found path
    if type(path) == list:
        for i in range(len(maze)):
            for j in range(len(maze[i])):
                if (i,j) in path:
                    print('x', end=' ')
                else:
                    print(maze[i][j], end=' ')
            print()


if __name__ == '__main__':main()
