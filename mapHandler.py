# from pyautogui import *
import os
import pyautogui
import time
import keyboard
import cv2
import numpy as np
import random
import win32api
import win32process
import win32gui
import win32con
import win32com.client
import requests
import common
from common import up, down, left, right, leftButton, rightButton, accept, cancel
from common import start, select, VBADimensions, press, pause
import imgHandler as img
from imgHandler import ULC, LRC, FRAME
from imgHandler import isImgUp, imgCoordinates, compareImages
import Unit
import Tile


# Not tested
def assessMap():
    """
        If I have several units that can level up and/or there are several units that can grant me a level up, how do I choose?

        The bot needs to know which unit(s) to level up. For that it needs to review all the active units of the player.
        (--> On game press leftButton (select first active unit))
        It needs to know :
        - Localization of the blue units
        - The current class, level, amount of experience of the blue units.
        - Localization of the red units The unit(s) it can attack
        - The current class, level of the red units.
        - Which red unit is in range of which blue unit
        - Which attacks/heals grant a level up
        - The path a ul has to take to attack a uk
        - The path a ul has to take to burn random numbers
        - The localization of flying unit to burn random numbers
    """


# Testing...
def generator():
    """
        This function creates a 2D array, representing the map.
        It should know :
        - The terrain is on each tile (to calculate pathing)
        - The coordinates of each units
        - The bot should update it each time there is an action (movement, death, reinforcement, recruit, ...)
    """
    # u1 = Unit('Roy', 'Lord', 1, 0)
    # t1 = Tile('Floor', 1, u1)

    # press(cancel)
    # press(start)  # pop in-gamme summary map
    imgPathNoMap = r'img\screenshot\noMap.png'
    img.screenshot(imgPathNoMap, VBADimensions)
    press(start)  # pop in-gamme summary map
    imgPathMap = r'img\screenshot\withMap.png'
    pyautogui.keyDown(leftButton)
    img.screenshot(imgPathMap, VBADimensions)
    pyautogui.keyUp(leftButton)
    img.compareImages(imgPathNoMap, imgPathMap)
    press(cancel)
    lrcCoordinates = pyautogui.locate(FRAME, r'img\screenshot\mapDiff.png', grayscale=False)
    """
    press(start)
    lrcCoordinates = getSummayMapCoordinates(down, right)  # Lower Right Corner
    ulcCoordinates = getSummayMapCoordinates(up, left)  # Upper Left Corner
    press(cancel)
    print('lrcCoordinates : ' + str(lrcCoordinates))
    print('ulcCoordinates : ' + str(ulcCoordinates))
    """
    # img.screenshot(r'img\screenshot\lrcScreenshot.png', (800, 579, 32, 32))
    # img.screenshot(r'img\screenshot\ulcScreenshot.png', (288, 543, 32, 32))


def getSummayMapCoordinates(y_direction, x_direction):

    # Places game screen on the x_direction y_direction corner of the summary map
    pyautogui.keyDown(y_direction)
    time.sleep(0.5)
    pyautogui.keyUp(y_direction)
    pyautogui.keyDown(x_direction)
    time.sleep(0.5)
    pyautogui.keyUp(x_direction)
    # Find the location of the flashing x_direction y_direction frame to know where the summary map is on screen
    imgPath = LRC  # Lower Right Corner
    if y_direction == up:
        imgPath = ULC  # Upper Left Corner

    pause()
    coordinates = imgCoordinates(imgPath, False, 0.9)
    # Not sure this is useful, but I did it because the flashing of the frame make it change color which can mess up image recognition
    tries = 25
    while coordinates is None and tries != 0:
        coordinates = imgCoordinates(imgPath, False, 0.9)
        tries = tries - 1
        time.sleep(0.1)
    pause()
    return coordinates
