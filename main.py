import sys
import pygame as pg
from astar import astar
pg.init()

def mazeToScreen(pos):
    '''Take a point on the maze and convert it to coordinates on the screen'''
    global cellSize
    posX = int(pos[1] * cellSize[0] + (cellSize[0]-car.get_size()[0])/2)
    posY = int(pos[0] * cellSize[1])
    return posX, posY

def screenToMaze(pos):
    '''Take coordinates from the screen and convert it to a point on the maze'''
    global cellSize
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

# Global variables
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
colorInactive = pg.Color('lightskyblue3')
colorActive = pg.Color('dodgerblue2')
font = pg.font.Font(None, 32)

# Pygame window creation
screen = pg.display.set_mode((601, 501), pg.RESIZABLE)

text = ''
color = colorInactive
active = False
done = False
while not done:
    inputBox = pg.Rect(int(screen.get_width()/2-85), int(screen.get_height()/2-18), 140, 32)
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input box
            if inputBox.collidepoint(event.pos):
                # Toggle the active variable.
                active = not active
            else:
                active = False
            # Change the current color of the input box.
            if active: color = colorActive 
            else: color = colorInactive
        elif event.type == pg.KEYDOWN and active:
            if event.key == pg.K_RETURN or event.key == pg.K_KP_ENTER:
                if text.isdigit():
                    mazeSize = int(text)
                    done = True
                else:
                    print('Invalid. Input only a whole number.')
                text = ''
            elif event.key == pg.K_BACKSPACE:
                text = text[:-1]
            else:
                text += event.unicode
        elif event.type == pg.VIDEORESIZE:
            surface = pg.display.set_mode((event.w, event.h), pg.RESIZABLE)


    screen.fill((30, 30, 30))

    # Render the text.
    textSurface = font.render(text, True, color)
    labelSurface = font.render('Input maze size', True, color)

    # Resize the box if the text is too long.
    inputBox.w = max(200, textSurface.get_width()+10)

    # Draw label and input box
    screen.blit(textSurface, (inputBox.x + 5, inputBox.y + 5))
    screen.blit(labelSurface, (inputBox.x, inputBox.y-50))
    pg.draw.rect(screen, color, inputBox, 2)

    pg.display.flip()


# Generate maze
maze = generateMaze(mazeSize)

# Generate empty start and end positions
startPos = None, None
endPos = None, None

# Load car image and scale
car = pg.image.load('car.png')
car = pg.transform.scale(car, (54, 54))

p = 0
started = finnished = False
flipped = False
while True:
    # Size of each cell in the grid
    cellSize = int(screen.get_width()/len(maze[0])), int(screen.get_height()/len(maze))

    # Event listener
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
        elif event.type == pg.MOUSEBUTTONDOWN and not started:
            if event.button == 1:
                mazePos = screenToMaze(event.pos)
                if maze[mazePos[0]][mazePos[1]] == 1:
                    maze[mazePos[0]][mazePos[1]] = 0
                else:
                    maze[mazePos[0]][mazePos[1]] = 1
        elif event.type == pg.KEYDOWN:
            mousePos = pg.mouse.get_pos()
            if event.key == pg.K_s and not started: startPos = screenToMaze(mousePos)
            elif event.key == pg.K_e and not started: endPos = screenToMaze(mousePos)
            elif event.key == pg.K_RETURN and not started:
                path = astar(maze, startPos, endPos)
                started = True
            elif (event.key == pg.K_RETURN or event.key == pg.K_KP_ENTER) and finnished:
                started = finnished = False
                p = 0
            elif (event.key in range(48, 58) or event.key in range(256, 266)) and not started:
                if event.key in range(48, 58): weight = event.key - 48
                else: weight = event.key - 256
                mazePos = screenToMaze(mousePos)
                setWeight(mazePos, weight)
            elif event.key == pg.K_c and not started:
                maze = generateMaze(mazeSize)
                startPos = None, None
                endPos = None, None
            elif event.key == pg.K_ESCAPE: sys.exit()
        elif event.type == pg.VIDEORESIZE:
            surface = pg.display.set_mode((event.w, event.h), pg.RESIZABLE)

    # Erase screen
    screen.fill(black)

    # Draw the grid
    grid = []

    for i in range(len(maze)):
        grid.append([])
        for j in range(len(maze[i])):
            pos = j * cellSize[0] + 1, i * cellSize[1] + 1
            dim = cellSize[0]-1, cellSize[1]-1
            rect = pg.Rect(pos, dim)
            if not maze[i][j]: color = black
            elif i == startPos[0] and j == startPos[1]: color = red
            elif i == endPos[0] and j == endPos[1]: color = green
            else:
                weight = maze[i][j]**0.5
                color = list(map(int, (white[0]/weight, white[1]/weight, white[2]/weight)))
            grid[i].append(pg.draw.rect(screen, color, rect))

    # Check if the user has finnished drawing the maze
    if started:
        # Draw the path
        newPath = []

        for point in path:
            y = int(point[0] * cellSize[1] + cellSize[1]/2)
            x = int(point[1] * cellSize[0] + cellSize[0]/2)
            newPoint = x, y
            newPath.append(newPoint)

        drawPath = pg.draw.lines(screen, blue, False, newPath, 3)

        # Draw the car
        try:
            newPos = mazeToScreen(path[p])
            if startPos[1] < endPos[1] and flipped: flip()
            elif startPos[1] > endPos[1] and not flipped: flip()
            try:
                if newPos[0] < carPos[0] and not flipped: flip()
                if newPos[0] > carPos[0] and flipped: flip()
            except NameError:
                pass
            carPos = newPos
            p += 1
            pg.time.delay(500)
        except IndexError:
            finnished = True

        screen.blit(car, carPos)

    # Update screen
    pg.display.flip()
