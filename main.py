import sys, pygame
from astar import astar
pygame.init()

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
maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # 0 = free space
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # 1 = wall
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]]

# Start and end positions
startPos = (2, 1)
endPos = (7, 8)

path = astar(maze, startPos, endPos)
print(path)

# Console print out of the found path
if type(path) == list:
    for step in path:
        maze[step[0]][step[1]] = 'x'

for line in maze:
    for e in line:
        print(e, end=' ')
    print()

# Size of each cell in the grid
cellSize = int(width/len(maze[0]))-1, int(height/len(maze))-1


while True:
    # Event listener
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # Grid drawing
    grid = []

    for i in range(len(maze)):
        grid.append([])
        for j in range(len(maze[i])):
            pos = j * (cellSize[0]+1)+1, i * (cellSize[1]+1)+1
            rect = pygame.Rect(pos, cellSize)
            if maze[i][j] == 1: color = black
            elif maze[i][j] == 'x': color = blue
            elif i == startPos[0] and j == startPos[1]: color = red
            elif i == endPos[0] and j == endPos[1]: color = green
            else: color = white 
            grid[i].append(pygame.draw.rect(screen, color, rect))

    

    pygame.display.flip()
