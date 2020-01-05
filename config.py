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

infoH1 = pg.font.Font(None, 46)  # Info header font
infoBody = pg.font.Font(None, 32)  # Info body font

helpText = '''Instructions


Press s to set the cell the mouse is currently in as the starting point

Press e to set the cell the mouse is currently in as the end point

Press c to clear the maze

Press m to return to the Main Menu

Set the weigth of the cell the mouse is in by pressing the numbers 0-9 
(including Numpad)

0 = wall, 1-9 = increasing difficulty

Press ENTER to start the navigation

When the navigation is over pressing ENTER enables editing

Pressing ESC closes the window

'''

aboutText = '''Virtual car navigation


Team project for Intro to Computers course of the Univercity of Patras
Electical and Computer Engineering Department


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
