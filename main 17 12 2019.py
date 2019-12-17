import pygame as pg
from astar import astar
pg.init()


############################################################################ functions ############################################################################
def fill(surface, color):
    """Fill all pixels of the surface with color, preserve transparency."""
    w, h = surface.get_size()
    r, g, b= color
    for x in range(w):
        for y in range(h):
            a = surface.get_at((x, y))[3]
            surface.set_at((x, y), pg.Color(r, g, b, a))

def getDimmensions():
    '''Input dialog for determining the maze size'''
    global colorActive, colorInactive, End,maze
    text= ''
    color= colorInactive
    colorBox= colorInactive
    activeinputBox= False
    optionsL=False
    startL=False
    aboutL=False
    exitL=False
    helpL=False

    colorStart= 0,0,0
    colorStart1= 0,0,0
    colorUp= 30,18,138
    colorClick= 255,255,255
    while not End:
 
        # Create the input box 
        inputBox = pg.Rect(int(screen.get_width() / 2 - 85), int(screen.get_height() / 2 - 18), 140, 32)

        # Create the start button (NEW) 
        start = pg.image.load("start.png")
        start=pg.transform.rotozoom(start,0, (0.12*(screen.get_width()/701 + screen.get_height()/601))/2)
        startX=int(screen.get_width() / 2-start.get_size()[0]/2)
        startY=int(4*screen.get_height() / 10-start.get_size()[1]/2)

        # Create the options button (NEW) 
        options = pg.image.load("options.png")
        options=pg.transform.rotozoom(options,0, (0.12*(screen.get_width()/701 + screen.get_height()/601))/2)
        optionsX=int(screen.get_width() / 2-options.get_size()[0]/2)
        optionsY=int(5*screen.get_height() / 10-options.get_size()[1]/2)

        # Create the help button (NEW) 
        help = pg.image.load("help.png")
        help=pg.transform.rotozoom(help,0, (0.12*(screen.get_width()/701 + screen.get_height()/601))/2)
        helpX=int(screen.get_width() / 2-help.get_size()[0]/2)
        helpY=int(6*screen.get_height() / 10-help.get_size()[1]/2)

        # Create the about button (NEW) 
        about = pg.image.load("about.png")
        about=pg.transform.rotozoom(about,0, (0.12*(screen.get_width()/701 + screen.get_height()/601))/2)
        aboutX=int(screen.get_width() / 2-about.get_size()[0]/2)
        aboutY=int(7*screen.get_height() / 10-about.get_size()[1]/2)

        # Create the exit button (NEW) 
        exit = pg.image.load("exit.png")
        exit=pg.transform.rotozoom(exit,0, (0.12*(screen.get_width()/701 + screen.get_height()/601))/2)
        exitX=int(screen.get_width() / 2-exit.get_size()[0]/2)
        exitY=int(8*screen.get_height() / 10-exit.get_size()[1]/2)

                    
        # Background color
        background_color=108,169,223
        screen.fill(background_color)
        #####################################################################   (NEW)
        if not optionsL and not startL and not helpL and not aboutL :
            
            for event in pg.event.get():
                if event.type == pg.QUIT: End=True            

                #StartButton                                            
                if event.type==4: # change color of buttos when mouse if on them     
                    x,y=event.pos                                                   
                    if start.get_rect().collidepoint([x-startX,y-startY]) :         
                        colorStart = colorUp        
                    else:                                                           
                        colorStart =  colorStart1

                if event.type == 5: 
                    x,y=event.pos
                    if start.get_rect().collidepoint([x-startX, y-startY]):
                        colorStart= colorClick  
                
                if event.type==6:
                    x,y=event.pos
                    if start.get_rect().collidepoint([x-startX, y-startY]):
                        colorStart= colorUp
                        startL=not startL
                #OptionsButton
                if event.type==4: # change color of buttos when mouse if on them     
                    x,y=event.pos                                                   
                    if options.get_rect().collidepoint([x-optionsX,y-optionsY]) :         
                        colorOptions = colorUp        
                    else:                                                           
                        colorOptions =  colorStart1

                if event.type == 5: 
                    x,y=event.pos
                    if options.get_rect().collidepoint([x-optionsX, y-optionsY]):
                        colorOptions= colorClick  
                
                if event.type==6:
                    x,y=event.pos
                    if options.get_rect().collidepoint([x-optionsX, y-optionsY]):
                        colorOptions= colorUp
                        optionsL=not optionsL
                #HelpButton
                if event.type==4: # change color of buttos when mouse if on them     
                    x,y=event.pos                                                   
                    if help.get_rect().collidepoint([x-helpX,y-helpY]) :         
                        colorHelp = colorUp        
                    else:                                                           
                        colorHelp =  colorStart1

                if event.type == 5: 
                    x,y=event.pos
                    if help.get_rect().collidepoint([x-helpX, y-helpY]):
                        colorHelp= colorClick  
                
                if event.type==6:
                    x,y=event.pos
                    if help.get_rect().collidepoint([x-helpX, y-helpY]):
                        colorHelp= colorUp   
                        helpL=not helpL

                #AboutButton
                if event.type==4: # change color of buttos when mouse if on them     
                    x,y=event.pos                                                   
                    if about.get_rect().collidepoint([x-aboutX,y-aboutY]) :         
                        colorAbout = colorUp        
                    else:                                                           
                        colorAbout =  colorStart1

                if event.type == 5: 
                    x,y=event.pos
                    if about.get_rect().collidepoint([x-aboutX, y-aboutY]):
                        colorAbout= colorClick  
                
                if event.type==6:
                    x,y=event.pos
                    if about.get_rect().collidepoint([x-aboutX, y-aboutY]):
                        colorAbout= colorUp
                        aboutL=not aboutL

                #ExitButton
                if event.type==4: # change color of buttos when mouse if on them     
                    x,y=event.pos                                                   
                    if exit.get_rect().collidepoint([x-exitX,y-exitY]) :         
                        colorExit = colorUp        
                    else:                                                           
                        colorExit =  colorStart1

                if event.type == 5: 
                    x,y=event.pos
                    if exit.get_rect().collidepoint([x-exitX, y-exitY]):
                        colorExit= colorClick  
                
                if event.type==6:
                    x,y=event.pos
                    if exit.get_rect().collidepoint([x-exitX, y-exitY]):
                        colorExit= colorUp  
                        exitL = not exitL

            #Claim Copyrights
            TextCC1 = font.render('Copyright © 2019 A.Alyssandrakis, M.Kaipis, L.Konstantellos, M.Lagou, N.Perreas, K.Stratakos.', True, [0,0,0])
            screen.blit(TextCC1, (screen.get_width() / 2-TextCC1.get_size()[0]/2,9*screen.get_height() / 10-TextCC1.get_size()[1]/2))

            TextCC2 = font.render('All Rights Reserved.', True, [0,0,0])
            screen.blit(TextCC2, (screen.get_width() / 2-TextCC2.get_size()[0]/2,9.5*screen.get_height() / 10-TextCC2.get_size()[1]/2))

            # Drow the start button                                          
            fill(start,colorStart)    
            screen.blit(start,[startX,startY])   

            # Drow the options button                                          
            fill(options,colorOptions)    
            screen.blit(options,[optionsX,optionsY])  

            # Drow the help button                                          
            fill(help,colorHelp)    
            screen.blit(help,[helpX,helpY])  

            # Drow the about button                                          
            fill(about,colorAbout)    
            screen.blit(about,[aboutX,aboutY])  
            
            # Drow the exit button                                          
            fill(exit,colorExit)    
            screen.blit(exit,[exitX,exitY]) 

        elif optionsL:
            for event in pg.event.get():
                if event.type == pg.QUIT: End=True
                if event.type == pg.KEYDOWN and activeinputBox:
                    # When ENTER is pressed return the inputed text if valid or diplay error message if not
                    if event.key == pg.K_RETURN or event.key == pg.K_KP_ENTER:
                        if text.isdigit():
                            return int(text)
                        else:
                            print('Invalid. Input only a whole number.')
                        text = ''
                    # When BACKSPACE is pressed erase characters from the text input
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    # When any other character key is pressed add the character to the text input
                    else:
                        text += event.unicode

                #ExitButton
                if event.type==4: # change color of buttos when mouse if on them     
                    x,y=event.pos                                                   
                    if exit.get_rect().collidepoint([x-exitX,y-exitY]) :         
                        colorExit = colorUp        
                    else:                                                           
                        colorExit =  colorStart1

                if event.type == 5: 
                    x,y=event.pos
                    if exit.get_rect().collidepoint([x-exitX, y-exitY]):
                        colorExit= colorClick  
                    
                    # When the input box is clicked toggle active flag
                    if inputBox.collidepoint(x,y):
                        activeinputBox= True
                        colorBox=colorActive
                    else:
                        activeinputBox= False
                        colorBox=colorInactive

                if event.type==6:
                    x,y=event.pos
                    if exit.get_rect().collidepoint([x-exitX, y-exitY]):
                        colorExit= colorUp  
                        exitL = not exitL
                        optionsL=not optionsL

                    
                
                #  Window resizing
                if event.type == pg.VIDEORESIZE:
                    surface = pg.display.set_mode((event.w, event.h), pg.RESIZABLE)
            # Draw input box
            pg.draw.rect(screen, colorBox, inputBox, 2)

            # Drow the exit button                                          
            fill(exit,colorExit)    
            screen.blit(exit,[exitX,exitY]) 
            # Render the label and text
            textSurface = font.render(text, True, color)
            # Resize the box if the text is too long
            inputBox.w = max(80, textSurface.get_width()+10)

            labelSurface = font.render('Input maze size', True, colorBox)

            # Move the label and text to correct spot
            screen.blit(textSurface, (inputBox.x + 5, inputBox.y + 8))
            screen.blit(labelSurface, (inputBox.x, inputBox.y - 50))





        #####################################################################


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

################################################################################ main ################################################################################

# Global variables
End = False # Fixed issue when exiting the app
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255
grey = 30, 30, 30
colorInactive = pg.Color('black')
colorActive = pg.Color('white')
font = pg.font.Font(None, 26)

# Pygame window creation
screen = pg.display.set_mode((901, 701), pg.RESIZABLE)

# Pygame window name 
pg.display.set_caption("Fast Car")

# Generate maze

#try:
mazeSize = getDimmensions()
maze = generateMaze(mazeSize)
#except :
 #   End=True


# Generate empty start and end positions
startPos = None, None
endPos = None, None

# Load car image
car = pg.image.load('car.png')

p = 0
started = finnished = False
flipped = False

while not End:
    # Size of each cell in the grid
    cellSize = int(screen.get_width() / len(maze[0])), int(screen.get_height() / len(maze))
    
    # Resize car
    carSize = int(min(cellSize[0], cellSize[1]))
    car = pg.transform.scale(car, (carSize, carSize))

    # Event listener
    for event in pg.event.get():
        if event.type == pg.QUIT: 
            End=True

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
            if event.key == pg.K_s and not started: startPos = screenToMaze(mousePos)
            # When e is pressed set the end point to the cell the mouse is currently in
            elif event.key == pg.K_e and not started: endPos = screenToMaze(mousePos)
            # When c is pressed clear the maze
            elif event.key == pg.K_c and not started:
                maze = generateMaze(mazeSize)
                startPos = None, None
                endPos = None, None
            # When r is pressed clear maze and display dialog for maze size
            elif event.key == pg.K_r and not started:
                
                maze = generateMaze(6)
                mazeSize = getDimmensions()
                startPos = None, None
                endPos = None, None
                


            # When 0-9 is pressed (including Numpad) set weigth for the cell the mouse is currently in
            # 0 = wall, 1-9 = increasing difficulty
            elif (event.key in range(48, 58) or event.key in range(256, 266)) and not started:
                if event.key in range(48, 58): weight = event.key - 48
                else: weight = event.key - 256
                mazePos = screenToMaze(mousePos)
                setWeight(mazePos, weight)
            # When ENTER is pressed start the navigation
            elif event.key == pg.K_RETURN and not started:
                if startPos != (None, None) and endPos != (None, None):
                    path = astar(maze, startPos, endPos)
                    started = True
                else: print('Please specify a start and end point')
            # When the navigation is over pressing ENTER enables editing
            elif (event.key == pg.K_RETURN or event.key == pg.K_KP_ENTER) and finnished:
                started = finnished = False
                p = 0
            # Pressing ESC closes the window
            elif event.key == pg.K_ESCAPE: end=True
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
            if not maze[i][j]: color = black
            elif i == startPos[0] and j == startPos[1]: color = red
            elif i == endPos[0] and j == endPos[1]: color = green
            else:
                weight = maze[i][j]**0.5
                color = list(map(int, (white[0]/weight, white[1]/weight, white[2]/weight)))
            grid[i].append(pg.draw.rect(screen, color, rect))

    # Check if the user has finnished drawing the maze
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
                if startPos[1] < endPos[1] and flipped: flip()
                elif startPos[1] > endPos[1] and not flipped: flip()
                try:
                    if newPos[0] < carPos[0] and not flipped: flip()
                    if newPos[0] > carPos[0] and flipped: flip()
                except NameError:
                    pass
                carPos = newPos
                p += 1
                pg.time.delay(int(500/(mazeSize/5)))
            except IndexError:
                finnished = True

            screen.blit(car, carPos)

        # If there is no path print error message
        else:
            print('No path found')
            started = False

    # Update screen
    pg.display.flip()