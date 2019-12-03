import sys, pygame
from astar import astar
pygame.init()

def mazeToScreen(pos):
    '''Take a point on the maze and convert it to coordinates on the screen'''
    global cellSize
    posX = int(pos[1] * cellSize[0] + (cellSize[0]-car.get_size()[0])/2)
    posY = int(pos[0] * cellSize[1])
    return posX, posY

def screenToMaze(pos):
    '''Take coordinates from the screen and convert it to a point on the maze'''
    global cellSize
    mazePosX = int(mousePos[0] / cellSize[0])
    mazePosY = int(mousePos[1] / cellSize[1])
    return mazePosY, mazePosX

def setWeight(pos, weight):
    '''Set the weight of the selected point in the maze'''
    maze[pos[0]][pos[1]] = weight

def generateMaze(size):
    '''Generate empty maze of dimension size x size'''
    maze = []
    for i in range(size):
        maze.append([])
        for j in range(size):
            maze[i].append(1)
    return maze


# Global variables
size = width, height = 601, 501
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255

# Pygame window creation
screen = pygame.display.set_mode(size)

# Generate maze
mazeSize = 10
maze = generateMaze(mazeSize)

# Generate empty start and end positions
startPos = None, None
endPos = None, None

# Size of each cell in the grid
cellSize = int(width/len(maze[0])), int(height/len(maze))

# Car
car = pygame.image.load('car.png')
car = pygame.transform.scale(car, (54, 54))

p = 0
started = finnished = False
while True:
    # Event listener
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not started:
            mousePos = pygame.mouse.get_pos()
            mazePos = screenToMaze(mousePos)
            if maze[mazePos[0]][mazePos[1]] == 1:
                maze[mazePos[0]][mazePos[1]] = 0
            else:
                maze[mazePos[0]][mazePos[1]] = 1
        elif event.type == pygame.KEYDOWN:
            mousePos = pygame.mouse.get_pos()
            if event.key == pygame.K_s and not started: startPos = screenToMaze(mousePos)
            elif event.key == pygame.K_e and not started: endPos = screenToMaze(mousePos)
            elif event.key == pygame.K_RETURN and not started:
                path = astar(maze, startPos, endPos)
                started = True
            elif event.key == pygame.K_RETURN and finnished:
                started = finnished = False
                p = 0
            elif (event.key in range(48, 58) or event.key in range(256, 266)) and not started:
                if event.key in range(48, 58): weight = event.key - 48
                else: weight = event.key - 256
                mazePos = screenToMaze(mousePos)
                setWeight(mazePos, weight)
            elif event.key == pygame.K_c and not started:
                maze = generateMaze(mazeSize)
                startPos = None, None
                endPos = None, None
            elif event.key == pygame.K_ESCAPE: sys.exit()

    # Erase screen
    screen.fill(black)

    # Draw the grid
    grid = []

    for i in range(len(maze)):
        grid.append([])
        for j in range(len(maze[i])):
            pos = j * cellSize[0] + 1, i * cellSize[1] + 1
            dim = cellSize[0]-1, cellSize[1]-1
            rect = pygame.Rect(pos, dim)
            if not maze[i][j]: color = black
            elif i == startPos[0] and j == startPos[1]: color = red
            elif i == endPos[0] and j == endPos[1]: color = green
            else:
                weight = maze[i][j]**0.5
                color = list(map(int, (white[0]/weight, white[1]/weight, white[2]/weight)))
            grid[i].append(pygame.draw.rect(screen, color, rect))

    # Check if the user has finnished drawing the maze
    if started:
        # Draw the path
        newPath = []

        for point in path:
            y = int(point[0] * cellSize[1] + cellSize[1]/2)
            x = int(point[1] * cellSize[0] + cellSize[0]/2)
            newPoint = x, y
            newPath.append(newPoint)

        drawPath = pygame.draw.lines(screen, blue, False, newPath, 3)

        # Draw the car
        try:
            carPos = mazeToScreen(path[p])
            p += 1
            pygame.time.delay(500)
        except IndexError:
            finnished = True

        screen.blit(car, carPos)

    # Update screen
    pygame.display.flip()
