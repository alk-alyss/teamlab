import sys, pygame
pygame.init()

size = width, height = 601, 501
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
green = 0, 255, 0

screen = pygame.display.set_mode(size)

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

startPos = (2, 1)
endPos = (7, 8)

cellSize = int(width/len(maze[0]))-1, int(height/len(maze))-1


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    grid = []

    for i in range(len(maze)):
        grid.append([])
        for j in range(len(maze[i])):
            pos = j * (cellSize[0]+1)+1, i * (cellSize[1]+1)+1
            rect = pygame.Rect(pos, cellSize)
            if maze[i][j]: color = black
            elif i == startPos[0] and j == startPos[1]: color = red
            elif i == endPos[0] and j == endPos[1]: color = green
            else: color = white 
            grid[i].append(pygame.draw.rect(screen, color, rect))

    

    pygame.display.flip()
