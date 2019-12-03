import sys, pygame
from astar import astar
pygame.init()

def mazeToScreen(pos):
    '''Take a point on the maze and convert it to coordinates on the screen'''
    global cellSize
    posX = int(pos[1] * cellSize[0] + (cellSize[0]-car.get_size()[0])/2)
    posY = int(pos[0] * cellSize[1])
    return posX, posY

# Global variables
size = width, height = 601, 501
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255

# Pygame window creation
screen = pygame.display.set_mode(size)

# The maze
maze = [[1, 1, 1, 1, 0, 1, 1, 1, 1, 1],  # # = weighted free space
        [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],  # (higher number = more difficult to pass from there)
        [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],  # 0 = wall
        [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 5, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 1, 1, 1]]

# Start and end positions
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

# Size of each cell in the grid
cellSize = int(width/len(maze[0])), int(height/len(maze))

# Car
car = pygame.image.load('car.png')
car = pygame.transform.scale(car, (54, 54))
carPos = mazeToScreen(startPos)

p = 0
while True:
    # Event listener
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

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

    # Delay at the beginning for maze inspection
    if pygame.time.get_ticks() > 3500:
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
            continue

    screen.blit(car, carPos)

    # Update screen
    pygame.display.flip()
