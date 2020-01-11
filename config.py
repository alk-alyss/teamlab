import pygame as pg
pg.init()

# Global variables
black = 0, 0, 0  # Black color
white = 255, 255, 255  # White color
red = 255, 0, 0  # Red color
green = 0, 255, 0  # Green color
blue = 0, 0, 255  # Blue color
menuBG = 108, 169, 223  # Menu background
colorInactive = black  # Inactive input color
colorActive = white  # Active input color
colorBtn = black  # Button color
colorOver = 30, 18, 138  # Button hover color
colorClick = 255, 255, 255  # Button click color
colorMsg = 45, 31, 171  # Message color

inputFont = pg.font.Font(None, 46)  # Input font
infoH1 = pg.font.Font(None, 52)  # Info Title font
infoH2 = pg.font.Font(None, 46)  # Info header font
infoBody = pg.font.Font(None, 32)  # Info body font

helpText = '''Instructions


Inside the menu under options select the grid size

Inside the grid editor select a tile by clicking on the image in the sidebar

Place the tile on the grid by clicking the desired spot

Clicking on a placed tile removes it if the same tile is selected in the sidebar

The same applies if no tiles are selected in the sidebar

Once the start and finish tiles are placed, 

press the start button to start the navigation

'''

aboutText = '''Virtual car navigation


Team project for "Introduction to Computers" course of the University of Patras
Electical & Computer Engineering Department


Created by:

Alkinoos Alyssadrakis
Michael Kaipis
Lampros Konstantellos
Myrto Lagou
Nickolas Perreas
Kyriakos Stratakos

A* algorithm adapted from:
https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2


Copyright 2019. All rights reserved
'''
