import config as g
import pygame as pg
import sys

def quitGame():
    pg.quit()
    sys.exit()

def multiLineText(text, surface, pos):
    text = text.split('\n')
    yOff = 0
    for line in text:
        if text.index(line) == 0:
            textSurface = g.infoH2.render(line, True, g.colorBtn)
            textSize = g.infoH2.size(line)
        else:
            textSurface = g.infoBody.render(line, True, g.colorBtn)
            textSize = g.infoBody.size(line)
        if pos == 'center':
            position = surface.get_width() / 2 - textSize[0] / 2, surface.get_height() / 10 + yOff
        elif pos == 'left':
            position = surface.get_width() / 12, surface.get_height() / 10 + yOff

        yOff += textSize[1]

        surface.blit(textSurface, position)


class Button:
    '''Button class'''
    def __init__(self, image, index, screen, color=g.colorBtn):
        self.screen = screen
        self.srfc = pg.image.load(image)
        self.srfc = pg.transform.rotozoom(
            self.srfc,
            0,
            (0.12*(self.screen.get_width() / 701 + self.screen.get_height() / 601)) / 2
        )
        self.x = int(self.screen.get_width()/2 - self.srfc.get_size()[0]/2)
        self.y = int((index + 2) * self.screen.get_height() / 10 - self.srfc.get_size()[1] / 2)
        self.color = color

    def collide(self, pos):
        '''Check for collision'''
        return self.srfc.get_rect().collidepoint([pos[0] - self.x, pos[1] - self.y])

    def fill(self):
        '''Fill all pixels of the surface with color, preserve transparency.'''
        w, h = self.srfc.get_size()
        r, g, b = self.color
        for x in range(w):
            for y in range(h):
                a = self.srfc.get_at((x, y))[3]
                self.srfc.set_at((x, y), pg.Color(r, g, b, a))

    def draw(self):
        '''Draw button'''
        self.fill()
        self.screen.blit(self.srfc, [self.x, self.y])


class Menu:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((901, 701))
        pg.display.set_caption("Virtual Car Navigation")
        self.mazeSize = 10
        self.text = ''
        self.main()

    def main(self):
        '''Main menu'''

        # Create buttons
        startBtn = Button("img/start.png", 1, self.screen)
        optionsBtn = Button("img/options.png", 2, self.screen)
        helpBtn = Button("img/help.png", 3, self.screen)
        aboutBtn = Button("img/about.png", 4, self.screen)
        exitBtn = Button("img/exit.png", 5, self.screen)

        while True:
            # Event listener
            for event in pg.event.get():
                if event.type == pg.QUIT: quitGame()

                # When mouse is pressed change button color, handle events
                if event.type == pg.MOUSEBUTTONDOWN:
                    # Start button
                    if startBtn.collide(event.pos):
                        startBtn.color = g.colorClick
                        if not self.text:
                            pg.display.quit()
                            return
                        elif self.text.isdigit():
                            self.mazeSize = int(self.text)
                            pg.display.quit()
                            return
                        else:
                            print('Invalid. Input only a whole number.')
                        self.text = ''

                    # Options button
                    elif optionsBtn.collide(event.pos):
                        optionsBtn.color = g.colorClick
                        self.optionsScreen()

                    # Help button
                    elif helpBtn.collide(event.pos):
                        helpBtn.color = g.colorClick
                        self.helpScreen()

                    # About button
                    elif aboutBtn.collide(event.pos):
                        aboutBtn.color = g.colorClick
                        self.aboutScreen()

                    # Exit button
                    elif exitBtn.collide(event.pos):
                        exitBtn.color = g.colorClick
                        quitGame()                    

                # When mouse is released revert button color
                if event.type == pg.MOUSEBUTTONUP:
                    if startBtn.collide(event.pos):
                        startBtn.color = g.colorBtn

                    elif optionsBtn.collide(event.pos):
                        optionsBtn.color = g.colorBtn

                    elif helpBtn.collide(event.pos):
                        helpBtn.color = g.colorBtn

                    elif aboutBtn.collide(event.pos):
                        aboutBtn.color = g.colorBtn

                    elif exitBtn.collide(event.pos):
                        exitBtn.color = g.colorBtn
                

            # Background color
            self.screen.fill(g.menuBG)

            # Change color of buttons when mouse is on them
            mousePos = pg.mouse.get_pos()
            if startBtn.collide(mousePos):
                startBtn.color = g.colorOver
            else:
                startBtn.color = g.colorBtn

            if optionsBtn.collide(mousePos):
                optionsBtn.color = g.colorOver
            else:
                optionsBtn.color = g.colorBtn

            if helpBtn.collide(mousePos):
                helpBtn.color = g.colorOver
            else:
                helpBtn.color = g.colorBtn

            if aboutBtn.collide(mousePos):
                aboutBtn.color = g.colorOver
            else:
                aboutBtn.color = g.colorBtn

            if exitBtn.collide(mousePos):
                exitBtn.color = g.colorOver
            else:
                exitBtn.color = g.colorBtn

            # Draw buttons
            startBtn.draw()
            optionsBtn.draw()
            helpBtn.draw()
            aboutBtn.draw()
            exitBtn.draw()

            # Update display
            pg.display.flip()


    def optionsScreen(self):
        '''Options screen'''
        colorInput = g.colorInactive
        activeInputBox = False

        # Create input box
        inputSize = 300, 50
        inputPosX = int(self.screen.get_width() / 2 - inputSize[0] / 2)
        inputPosY = int(self.screen.get_height() / 2 - inputSize[1] / 2)
        inputBox = pg.Rect(inputPosX, inputPosY, inputSize[0], inputSize[1])

        # Create button
        returnBtn = Button("img/return.png", 5, self.screen)

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT: quitGame()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    # Make input box active when clicked
                    if inputBox.collidepoint(event.pos):
                        activeInputBox = not activeInputBox

                    # Return button
                    elif returnBtn.collide(event.pos):
                        returnBtn.color = g.colorClick
                        activeInputBox = False
                        return

                    else:
                        activeInputBox = False

                elif event.type == pg.MOUSEBUTTONUP:
                    if returnBtn.collide(event.pos):
                        returnBtn.color = g.colorBtn

                elif event.type == pg.KEYDOWN:
                    # When ENTER or ESC is pressed return to main menu
                    if event.key == pg.K_RETURN or event.key == pg.K_KP_ENTER or event.key == pg.K_ESCAPE:
                        activeInputBox = False
                        return
                    # When BACKSPACE is pressed erase characters from the text input
                    elif event.key == pg.K_BACKSPACE and activeInputBox:
                        self.text = self.text[:-1]
                    # When any other character key is pressed add the character to the text input
                    elif (event.key in range(48, 58) or event.key in range(256, 266)) and activeInputBox:
                        self.text += event.unicode
        

            # Background color
            self.screen.fill(g.menuBG)

            mousePos = pg.mouse.get_pos()
            if returnBtn.collide(mousePos):
                returnBtn.color = g.colorOver
            else:
                returnBtn.color = g.colorBtn

            # Draw input box
            colorInput = g.colorActive if activeInputBox else g.colorInactive
            pg.draw.rect(self.screen, colorInput, inputBox, 2)

            # Render the label and text
            textSurface = g.inputFont.render(self.text, True, g.colorBtn)
            labelSurface = g.inputFont.render('Input maze size', True, g.colorBtn)

            # Move the label and text to correct spot
            textSize = g.inputFont.size(self.text)
            self.screen.blit(textSurface, (inputBox.x + 5, int(inputBox.y + inputSize[1]/2 - textSize[1]/2)))
            self.screen.blit(labelSurface, (inputBox.x, inputBox.y - 50))

            # Draw button
            returnBtn.draw()

            # Update display
            pg.display.flip()

    
    def helpScreen(self):
        '''Help screen'''

        # Create button
        returnBtn = Button("img/return.png", 7, self.screen)

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT: quitGame()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    # Return button
                    if returnBtn.collide(event.pos):
                        returnBtn.color = g.colorClick
                        activeInputBox = False
                        return

                elif event.type == pg.MOUSEBUTTONUP:
                    if returnBtn.collide(event.pos):
                        returnBtn.color = g.colorBtn

            # Background color
            self.screen.fill(g.menuBG)

            # Change color of buttons when mouse is on them
            mousePos = pg.mouse.get_pos()
            if returnBtn.collide(mousePos):
                returnBtn.color = g.colorOver
            else:
                returnBtn.color = g.colorBtn

            # Draw text
            multiLineText(g.helpText, self.screen, 'left')

            # Draw button
            returnBtn.draw()

            # Update display
            pg.display.flip()


    def aboutScreen(self):
        '''Help screen'''

        # Create button
        returnBtn = Button("img/return.png", 7, self.screen)

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT: quitGame()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    # Return button
                    if returnBtn.collide(event.pos):
                        returnBtn.color = g.colorClick
                        activeInputBox = False
                        return

                elif event.type == pg.MOUSEBUTTONUP:
                    if returnBtn.collide(event.pos):
                        returnBtn.color = g.colorBtn

            # Background color
            self.screen.fill(g.menuBG)

            # Change color of buttons when mouse is on them
            mousePos = pg.mouse.get_pos()
            if returnBtn.collide(mousePos):
                returnBtn.color = g.colorOver
            else:
                returnBtn.color = g.colorBtn

            # Draw text
            multiLineText(g.aboutText, self.screen, 'center')

            # Draw button
            returnBtn.draw()

            # Update display
            pg.display.flip()
