# from pyautogui import *
import os
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api
import win32process
import win32gui
import win32con
import win32com.client
import requests
import common
from common import *
import imgHandler as img
import mapHandler as map
import Unit
import Tile


"""
    REQUIREMENTS :
        VisualBoyAdvance 1.7.2
        Windows (can vba run on other OS?)
        All imports ?
        * VBA on main display (if several)
        * VBA with border config (the bot can do it)
        English text on VBA ROM

    NOTES :
        Tests made on FE6 (English patched), FE7, FE8, Last Promise, Storge
"""


def RNGManipulatorLvlUp():
    """
        /!\ Need an arena handler and a staff user scenario as well
        Kill unit scenario :
        1. Locate unit to level up (ul)
        2. Locate unit to kill (uk)
        3. Select ul
        4. Kill uk (! boss dialog)
        5. Check level up (if ok --> save and done)
        6. Reload save state
        7. RNG increment --> 3.
        End turn scenario :
        1. End turn
        2. Check level up (if ok let turn go)
        3. Reload save state
        4. RNG increment

        The bot needs to perform the following action :
        Assess the map
        Define it in bot memory
        Find which unit can level up
        Do it
    """


def main():
    print("The bot needs your VBA to be running with your FE ROM on, and you should start the current chapter you want to play")
    print("Press 'o' to confirm that everything is ready")

    userInput = input()
    while userInput.lower() != 'o':
        print("Press 'o' to confirm that everything is ready")
        userInput = input()

    common.VBASetUp()
    print('The bot has set your VBA up, waiting for chapter to start...')
    # Finding out if the chapter has started
    while not img.hasChapterStarted():
        time.sleep(1)
    print('Chapter has started, assessing the map...')
    map.generator()
    # Creating map in bot memory
    # Dictionnary of blue and red units
    # Checking range
    #   if in range: Check experiencelvlup
    #       if experiencelvlup : save state + attack
    #           if lvlup not good : load save state + rngIncrement + attack


if __name__ == "__main__":
    main()
