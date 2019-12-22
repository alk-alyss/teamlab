import pygame as pg
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
inputFont = pg.font.Font(None, 46)  # Input font
creditFont = pg.font.Font(None, 26)  # Credits font
