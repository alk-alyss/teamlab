import pygame as pg
import config as g
import sys
import time
import menu
from astar import astar
pg.init()

def mazeToScreen(pos):
    '''Take a point on the maze and convert it to coordinates on the screen'''
    posX = int(pos[1] * cellSize[0] + (cellSize[0]-car.get_size()[0])/2)
    posY = int(pos[0] * cellSize[1])
    return posX, posY

def screenToMaze(pos):
    '''Take coordinates from the screen and convert it to a point on the maze'''
    mazePosX = int(pos[0] / cellSize[0])
    mazePosY = int(pos[1] / cellSize[1])
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

def flip():
    '''Flip the direction of the car horrizontally and toggle flipped flag'''
    global car, flipped
    car = pg.transform.flip(car, True, False)
    flipped = not flipped

def showMessage(text):
    textSurface = g.infoH1.render(text, True, g.colorMsg)
    textSize = g.infoH1.size(text)
    positionX = int(screen.get_width()/2 - textSize[0]/2)
    positionY = int(screen.get_height()/6 - textSize[1]/2)
    screen.blit(textSurface, (positionX, positionY))
    pg.display.flip()

    time.sleep(2)

# Pygame window creation + window name
screen = pg.display.set_mode((901, 701))
pg.display.set_caption("Virtual car navigation")

# Generate maze
mazeSize = menu.Menu(screen).mazeSize
maze = generateMaze(mazeSize)

# Generate empty start and end positions
startPos = None, None
endPos = None, None

# Load car image
car = pg.image.load('img/car.png')

p = 0
started = finished = False
flipped = False
End = False  # End flag

while not End:
    # Size of each cell in the grid
    cellSize = int(screen.get_width() /
                   len(maze[0])), int(screen.get_height() / len(maze))

    # Resize car
    carSize = int(min(cellSize[0], cellSize[1]))
    car = pg.transform.scale(car, (carSize, carSize))

    # Event listener
    for event in pg.event.get():
        if event.type == pg.QUIT:
            End = True

            '''When the left mouse button is pressed toggle the weight 
            for the cell the mouse is currently in between 0 and 1
            If the cell has any other weight clicking will make it a wall'''

        elif event.type == pg.MOUSEBUTTONDOWN and not started:
            if event.button == 1:
                mazePos = screenToMaze(event.pos)
                try:
                    if maze[mazePos[0]][mazePos[1]]:
                        maze[mazePos[0]][mazePos[1]] = 0
                    else:
                        maze[mazePos[0]][mazePos[1]] = 1
                except IndexError:
                    pass

        elif event.type == pg.KEYDOWN:
            mousePos = pg.mouse.get_pos()
            # When s is pressed set the starting point to the cell the mouse is currently in
            if event.key == pg.K_s and not started:
                startPos = screenToMaze(mousePos)
            # When e is pressed set the end point to the cell the mouse is currently in
            elif event.key == pg.K_e and not started:
                endPos = screenToMaze(mousePos)
            # When c is pressed clear the maze
            elif event.key == pg.K_c and not started:
                maze = generateMaze(mazeSize)
                startPos = None, None
                endPos = None, None
            # When ESC is pressed return to Main Menu
            elif event.key == pg.K_ESCAPE and not started:
                mazeSize = menu.Menu(screen).mazeSize
                maze = generateMaze(mazeSize)
                startPos = None, None
                endPos = None, None

            # When 0-9 is pressed (including Numpad) set weigth for the cell the mouse is currently in
            # 0 = wall, 1-9 = increasing difficulty
            elif (event.key in range(48, 58) or event.key in range(256, 266)) and not started:
                weight = int(event.unicode)
                mazePos = screenToMaze(mousePos)
                setWeight(mazePos, weight)
            # When ENTER is pressed start the navigation
            elif event.key == pg.K_RETURN and not started:
                if startPos != (None, None) and endPos != (None, None):
                    path = astar(maze, startPos, endPos)
                    started = True
                else:
                    showMessage('Please specify a start and end point')
            # When the navigation is over pressing ENTER enables editing
            elif (event.key == pg.K_RETURN or event.key == pg.K_KP_ENTER) and finished:
                started = finished = False
                p = 0

    # Erase screen
    screen.fill(g.black)

    # Draw the grid
    grid = []
    for i in range(len(maze)):
        grid.append([])
        for j in range(len(maze[i])):
            pos = j * cellSize[0] + 1, i * cellSize[1] + 1
            dim = cellSize[0]-1, cellSize[1]-1
            rect = pg.Rect(pos, dim)
            if not maze[i][j]:
                color = g.black
            elif i == startPos[0] and j == startPos[1]:
                color = g.red
            elif i == endPos[0] and j == endPos[1]:
                color = g.green
            else:
                weight = maze[i][j]**0.5
                color = list(map(int, (g.white[0] / weight, g.white[1] / weight, g.white[2]/weight)))
            grid[i].append(pg.draw.rect(screen, color, rect))

    # Check if the user has finished drawing the maze
    if started:
        if type(path) == list:
            # Draw the path
            newPath = []
            for point in path:
                y = int(point[0] * cellSize[1] + cellSize[1]/2)
                x = int(point[1] * cellSize[0] + cellSize[0]/2)
                newPoint = x, y
                newPath.append(newPoint)

            drawPath = pg.draw.lines(screen, g.blue, False, newPath, 3)

            # Draw/animate the car
            try:
                newPos = mazeToScreen(path[p])
                if startPos[1] < endPos[1] and flipped:
                    flip()
                elif startPos[1] > endPos[1] and not flipped:
                    flip()
                try:
                    if newPos[0] < carPos[0] and not flipped:
                        flip()
                    if newPos[0] > carPos[0] and flipped:
                        flip()
                except NameError:
                    pass
                carPos = newPos
                p += 1
                pg.time.delay(int(500/(mazeSize/5)))
            except IndexError:
                finished = True

            screen.blit(car, carPos)

        # If there is no path print error message
        else:
            showMessage('No path found')
            started = False

    # Update screen
    pg.display.flip()

pg.quit()
sys.exit()
