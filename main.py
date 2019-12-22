import pygame as pg
import sys
from astar import astar
pg.init()

# Global variables
black = 0, 0, 0  # Black color
white = 255, 255, 255  # White color
red = 255, 0, 0  # Red color
green = 0, 255, 0  # Green color
blue = 0, 0, 255  # Blue color
grey = 30, 30, 30  # Grey color
menuBG = 108, 169, 223  # Menu background
colorInactive = black  # Inactive input color
colorActive = white  # Active input color
colorBtn = black  # Button color
colorOver = 30, 18, 138  # Button hover color
colorClick = 255, 255, 255  # Button click color
font = pg.font.Font(None, 26)  # Default font
End = False  # End flag

class Button:
    '''Button class'''
    def __init__(self, image, index, color=colorBtn):
        self.srfc = pg.image.load(image)
        self.srfc = pg.transform.rotozoom(
            self.srfc, 0, (0.12*(screen.get_width()/701+screen.get_height()/601))/2)
        self.x = int(screen.get_width() / 2-self.srfc.get_size()[0]/2)
        self.y = int((index + 2) * screen.get_height() /
                     10 - self.srfc.get_size()[1] / 2)
        self.color = color

    '''Check for collision'''
    def collide(self, pos):
        return self.srfc.get_rect().collidepoint([pos[0] - self.x, pos[1] - self.y])

    '''Draw button'''
    def draw(self):
        fill(self.srfc, self.color)
        screen.blit(self.srfc, [self.x, self.y])


def fill(surface, color):
    '''Fill all pixels of the surface with color, preserve transparency.'''
    w, h = surface.get_size()
    r, g, b = color
    for x in range(w):
        for y in range(h):
            a = surface.get_at((x, y))[3]
            surface.set_at((x, y), pg.Color(r, g, b, a))


def mainMenu():
    '''Input dialog for determining the maze size'''
    text = ''
    colorInput = colorInactive
    activeInputBox = False
    state = 'main'

    while not End:
        # Create input box
        inputBox = pg.Rect(int(screen.get_width() / 2 - 85),
                           int(screen.get_height() / 2 - 18), 140, 32)

        # Create buttons
        startBtn = Button("start.png", 1)
        optionsBtn = Button("options.png", 2)
        helpBtn = Button("help.png", 3)
        aboutBtn = Button("about.png", 4)
        exitBtn = Button("exit.png", 5)

        # Event listener
        for event in pg.event.get():
            if event.type == pg.QUIT: quitGame()

            # When mouse is pressed change button color, handle events
            if event.type == pg.MOUSEBUTTONDOWN:
                # When in main menu
                if state == 'main':
                    # Start button
                    if startBtn.collide(event.pos):
                        startBtn.color = colorClick
                        if not text:
                            return 10
                        elif text.isdigit():
                            return int(text)
                        else:
                            print('Invalid. Input only a whole number.')
                        text = ''

                    # Options button
                    elif optionsBtn.collide(event.pos):
                        optionsBtn.color = colorClick
                        state = 'options'

                    # Help button
                    elif helpBtn.collide(event.pos):
                        helpBtn.color = colorClick
                        # state = 'help'

                    # About button
                    elif aboutBtn.collide(event.pos):
                        aboutBtn.color = colorClick
                        # state = 'about'

                    # Exit button
                    elif exitBtn.collide(event.pos):
                        exitBtn.color = colorClick
                        sys.exit()

                # When in options menu
                elif state == 'options':
                    # Make input box active when clicked
                    if inputBox.collidepoint(event.pos):
                        activeInputBox = not activeInputBox
                    else:
                        activeInputBox = False

            # When mouse is released revert button color
            if event.type == pg.MOUSEBUTTONUP:
                if startBtn.collide(event.pos):
                    startBtn.color = colorBtn

                elif optionsBtn.collide(event.pos):
                    optionsBtn.color = colorBtn

                elif helpBtn.collide(event.pos):
                    helpBtn.color = colorBtn

                elif aboutBtn.collide(event.pos):
                    aboutBtn.color = colorBtn

                elif exitBtn.collide(event.pos):
                    exitBtn.color = colorBtn

            if event.type == pg.KEYDOWN and state == 'options':
                # When ENTER or ESC is pressed return to main menu
                if event.key == pg.K_RETURN or event.key == pg.K_KP_ENTER or event.key == pg.K_ESCAPE:
                    state = 'main'
                # When BACKSPACE is pressed erase characters from the text input
                elif event.key == pg.K_BACKSPACE and activeInputBox:
                    text = text[:-1]
                # When any other character key is pressed add the character to the text input
                elif (event.key in range(48, 58) or event.key in range(256, 266)) and activeInputBox:
                    text += event.unicode

            #  Window resizing
            elif event.type == pg.VIDEORESIZE:
                surface = pg.display.set_mode((event.w, event.h), pg.RESIZABLE)

        # Background color
        screen.fill(menuBG)

        # Draw main menu
        if state == 'main':
            # change color of buttons when moubackground_color = 108, 169, 223se is on them
            mousePos = pg.mouse.get_pos()
            if startBtn.collide(mousePos):
                startBtn.color = colorOver
            else:
                startBtn.color = colorBtn

            if optionsBtn.collide(mousePos):
                optionsBtn.color = colorOver
            else:
                optionsBtn.color = colorBtn

            if helpBtn.collide(mousePos):
                helpBtn.color = colorOver
            else:
                helpBtn.color = colorBtn

            if aboutBtn.collide(mousePos):
                aboutBtn.color = colorOver
            else:
                aboutBtn.color = colorBtn

            if exitBtn.collide(mousePos):
                exitBtn.color = colorOver
            else:
                exitBtn.color = colorBtn

            # Claim Copyrights
            TextCC1 = font.render('Copyright © 2019 A.Alyssandrakis, M.Kaipis, L.Konstantellos, M.Lagou, N.Perreas, K.Stratakos.', True, [0,0,0])
            screen.blit(TextCC1, (int(screen.get_width() / 2 - TextCC1.get_size()[0] / 2),
                                int(9*screen.get_height() / 10-TextCC1.get_size()[1]/2)))

            TextCC2 = font.render('All Rights Reserved.', True, [0,0,0])
            screen.blit(TextCC2, (int(screen.get_width() / 2 - TextCC2.get_size()[0] / 2),
                                int(9.5*screen.get_height() / 10-TextCC2.get_size()[1]/2)))

            # Draw buttons
            startBtn.draw()
            optionsBtn.draw()
            helpBtn.draw()
            aboutBtn.draw()
            exitBtn.draw()

        # Draw maze size input dialog
        elif state == 'options':
            # Draw input box
            colorInput = colorActive if activeInputBox else colorInactive
            pg.draw.rect(screen, colorInput, inputBox, 2)

            # Render the label and text
            textSurface = font.render(text, True, colorInput)
            labelSurface = font.render('Input maze size', True, colorInput)

            # Move the label and text to correct spot
            screen.blit(textSurface, (inputBox.x + 5, inputBox.y + 5))
            screen.blit(labelSurface, (inputBox.x, inputBox.y - 50))

        # Update display
        pg.display.flip()


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

def quitGame():
    pg.quit()
    sys.exit()

# Pygame window creation + window name
screen = pg.display.set_mode((901, 701), pg.RESIZABLE)
pg.display.set_caption("Fast Car")

# Generate maze
mazeSize = mainMenu()
maze = generateMaze(mazeSize)

# Generate empty start and end positions
startPos = None, None
endPos = None, None

# Load car image
car = pg.image.load('car.png')

p = 0
started = finished = False
flipped = False

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
            # When r is pressed clear maze and display dialog for maze size
            elif event.key == pg.K_r and not started:

                mazeSize = mainMenu()
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
                    print('Please specify a start and end point')
            # When the navigation is over pressing ENTER enables editing
            elif (event.key == pg.K_RETURN or event.key == pg.K_KP_ENTER) and finished:
                started = finished = False
                p = 0
            # Pressing ESC closes the window
            elif event.key == pg.K_ESCAPE:
                End = True
        #  Window resizing
        elif event.type == pg.VIDEORESIZE and not started:
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
            if not maze[i][j]:
                color = black
            elif i == startPos[0] and j == startPos[1]:
                color = red
            elif i == endPos[0] and j == endPos[1]:
                color = green
            else:
                weight = maze[i][j]**0.5
                color = list(
                    map(int, (white[0]/weight, white[1]/weight, white[2]/weight)))
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

            drawPath = pg.draw.lines(screen, blue, False, newPath, 3)

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
            print('No path found')
            started = False

    # Update screen
    pg.display.flip()

quitGame()