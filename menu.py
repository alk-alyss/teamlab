import config as g
import pygame as pg
import sys
pg.init()

def quitGame():
    pg.quit()
    sys.exit()


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

    '''Check for collision'''
    def collide(self, pos):
        return self.srfc.get_rect().collidepoint([pos[0] - self.x, pos[1] - self.y])

    def fill(self):
        '''Fill all pixels of the surface with color, preserve transparency.'''
        w, h = self.srfc.get_size()
        r, g, b = self.color
        for x in range(w):
            for y in range(h):
                a = self.srfc.get_at((x, y))[3]
                self.srfc.set_at((x, y), pg.Color(r, g, b, a))

    '''Draw button'''
    def draw(self):
        self.fill()
        self.screen.blit(self.srfc, [self.x, self.y])


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.mazeSize = 10
        self.mainMenu()

    def mainMenu(self):
        '''Input dialog for determining the maze size'''
        text = ''
        colorInput = g.colorInactive
        activeInputBox = False
        state = 'main'

        while True:
            # Create input box
            inputSize = 300, 50
            inputPosX = int(self.screen.get_width() / 2 - inputSize[0] / 2)
            inputPosY = int(self.screen.get_height() / 2 - inputSize[1] / 2)
            inputBox = pg.Rect(inputPosX, inputPosY, inputSize[0], inputSize[1])

            # Create buttons
            startBtn = Button("img/start.png", 1, self.screen)
            optionsBtn = Button("img/options.png", 2, self.screen)
            helpBtn = Button("img/help.png", 3, self.screen)
            aboutBtn = Button("img/about.png", 4, self.screen)
            exitBtn = Button("img/exit.png", 5, self.screen)
            returnBtn = Button("img/return.png", 5, self.screen)

            # Event listener
            for event in pg.event.get():
                if event.type == pg.QUIT: quitGame()

                # When mouse is pressed change button color, handle events
                if event.type == pg.MOUSEBUTTONDOWN:
                    # When in main menu
                    if state == 'main':
                        # Start button
                        if startBtn.collide(event.pos):
                            startBtn.color = g.colorClick
                            if not text:
                                return
                            elif text.isdigit():
                                self.mazeSize = int(text)
                                return
                            else:
                                print('Invalid. Input only a whole number.')
                            text = ''

                        # Options button
                        elif optionsBtn.collide(event.pos):
                            optionsBtn.color = g.colorClick
                            state = 'options'

                        # Help button
                        elif helpBtn.collide(event.pos):
                            helpBtn.color = g.colorClick
                            # state = 'help'

                        # About button
                        elif aboutBtn.collide(event.pos):
                            aboutBtn.color = g.colorClick
                            # state = 'about'

                        # Exit button
                        elif exitBtn.collide(event.pos):
                            exitBtn.color = g.colorClick
                            sys.exit()

                    # When in options menu
                    elif state == 'options':
                        # Make input box active when clicked
                        if inputBox.collidepoint(event.pos):
                            activeInputBox = not activeInputBox

                        # Rerutn button
                        elif returnBtn.collide(event.pos):
                            returnBtn.color = g.colorClick
                            state = 'main'
                            activeInputBox = False

                        else:
                            activeInputBox = False

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

                    elif returnBtn.collide(event.pos):
                        returnBtn.color = g.colorBtn

                if event.type == pg.KEYDOWN and state == 'options':
                    # When ENTER or ESC is pressed return to main menu
                    if event.key == pg.K_RETURN or event.key == pg.K_KP_ENTER or event.key == pg.K_ESCAPE:
                        state = 'main'
                        activeInputBox = False
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
            self.screen.fill(g.menuBG)

            # Main menu
            if state == 'main':
                # change color of buttons when mouse is on them
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

                # Claim Copyrights
                TextCC1 = g.creditFont.render('Copyright Â© 2019 A.Alyssandrakis, M.Kaipis, L.Konstantellos, M.Lagou, N.Perreas, K.Stratakos.', True, [0,0,0])
                self.screen.blit(TextCC1, (int(self.screen.get_width() / 2 - TextCC1.get_size()[0] / 2),
                                    int(9*self.screen.get_height() / 10-TextCC1.get_size()[1]/2)))

                TextCC2 = g.creditFont.render('All Rights Reserved.', True, [0,0,0])
                self.screen.blit(TextCC2, (int(self.screen.get_width() / 2 - TextCC2.get_size()[0] / 2),
                                    int(9.5*self.screen.get_height() / 10-TextCC2.get_size()[1]/2)))

                # Draw buttons
                startBtn.draw()
                optionsBtn.draw()
                helpBtn.draw()
                aboutBtn.draw()
                exitBtn.draw()

            # Options screen
            elif state == 'options':
                mousePos = pg.mouse.get_pos()
                if returnBtn.collide(mousePos):
                    returnBtn.color = g.colorOver
                else:
                    returnBtn.color = g.colorBtn

                # Draw input box
                colorInput = g.colorActive if activeInputBox else g.colorInactive
                pg.draw.rect(self.screen, colorInput, inputBox, 2)

                # Render the label and text
                textSurface = g.inputFont.render(text, True, g.colorBtn)
                labelSurface = g.inputFont.render('Input maze size', True, g.colorBtn)

                # Move the label and text to correct spot
                textSize = g.inputFont.size(text)
                self.screen.blit(textSurface, (inputBox.x + 5, int(inputBox.y + inputSize[1]/2 - textSize[1]/2)))
                self.screen.blit(labelSurface, (inputBox.x, inputBox.y - 50))

                returnBtn.draw()

            # Update display
            pg.display.flip()
