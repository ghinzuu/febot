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
import Unit

# VBA control config
# This needs to match the player's config (default are developer controls)
# Valid keys for keyboard :
# https://pyautogui.readthedocs.io/en/latest/keyboard.html#keyboard-keys
up = 'w'
down = 's'
left = 'a'
right = 'd'
leftButton = 'q'
rightButton = 'e'
accept = 'k'
cancel = 'l'
start = 'enter'
select = 'backspace'
speedVBA = 'space'

# Client dimensions (left, top, width, height) of the VBA. This is set up in VBASetUp.
# These dimensions are equal to setting VBA size using the window menu with
# VisualBoyAdvance --> Options --> Gameboy --> Border on a 1920x1080 monitor
# having the window located at left=100, top=100
VBADimensions = (108, 151, 959, 639)


# /!\ Sleep times need to be reviewed
# This function press a key on the keyboard
def press(char):
    pyautogui.keyDown(char)
    time.sleep(0.01)
    pyautogui.keyUp(char)
    time.sleep(0.25)


def saveState():
    pyautogui.hotkey('ctrl', 's')
    time.sleep(0.1)
    press('enter')
    time.sleep(0.1)
    press(cancel)


def loadSavedState():
    pyautogui.hotkey('ctrl', 'l')
    time.sleep(0.1)
    press('enter')
    time.sleep(0.1)
    press(cancel)


def pause():
    pyautogui.hotkey('ctrl', 'p')


def VBASetUp():
    """
        Set the VBA as main app in Windows
        Check documentation to understand the functions :
        https://docs.microsoft.com/en-us/windows/win32/api/winuser/
    """
    # First we need a handle (hwnd) on the VBA window
    VBAWindowHandle = win32gui.FindWindow(None, 'VisualBoyAdvance-100%')
    # As the speed of the VBA may vary its process name changes as well,
    # which will make the FindWindow fail, assigning a value of 0
    tries = 25
    while VBAWindowHandle == 0 and tries != 0:
        VBAWindowHandle = win32gui.FindWindow(None, 'VisualBoyAdvance-100%')
        tries = tries - 1
        time.sleep(0.1)

    if tries == 0:
        print("Bot could not find the VBA. Have you started it and launched the ROM?")
        quit(404)  # this is no web app but 404 will always mean "not found" to me

    VBAThreadId = win32process.GetWindowThreadProcessId(VBAWindowHandle)[0]  # [1] is processId
    botThreadId = win32api.GetCurrentThreadId()  # == threading.get_ident()
    # This gives permission to the bot to use the handle of the VBA
    win32process.AttachThreadInput(VBAThreadId, botThreadId, True)
    # Check 'VBADimension' constant higher in this script
    # Note that these dimensions are the window dimensions which are the client dimensions + VBA's menu
    win32gui.SetWindowPos(VBAWindowHandle, win32con.HWND_TOP, 100, 100, 976, 699, 0)
    win32gui.SetActiveWindow(VBAWindowHandle)
    win32gui.SetFocus(VBAWindowHandle)
    # These functions allows the bot to send keyboard inputs to the GBA and not the shell
    # I do not understand them in detail and just said thanks to StackOverflow
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')
    win32gui.SetForegroundWindow(VBAWindowHandle)
    time.sleep(0.5)
