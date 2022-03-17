# from pyautogui import *
import pyautogui
import cv2
import numpy as np
import requests
from common import VBADimensions

VERSION = ''
DEFAVO7 = r'img\defavo\fe7.jpg'  # fe7 defense avoid terrain pop up
DEFAVO8 = r'img\defavo\fe8.jpg'
ULC = r'img\map\ulc.png'  # summary map flashing Upper Left Corner : 32x32 px
LRC = r'img\map\lrc.png'  # summary map flashing Lower Right Corner : 32x32 px
FRAME = r'img\map\frame.png'  # summary map frame : 248 x 168 px


# Needs to be retested (VERSION behavior)
def hasChapterStarted():
    """
        This function states if current chapter has started and sets the ROM VERSION (FE6-7 or FE8)
    """
    global VERSION
    try:
        if pyautogui.locateOnScreen(
            DEFAVO7,
            grayscale=True,
            confidence=0.8,
            region=VBADimensions
        ) is not None:
            print('This is an FE6-7 based ROM')
            VERSION = 'FE7'
            return True
        if pyautogui.locateOnScreen(
            DEFAVO8,
            grayscale=True,
            confidence=0.8,
            region=VBADimensions
        ) is not None:
            print('This is an FE8 based ROM')
            VERSION = 'FE8'
            return True
    except pyautogui.ImageNotFoundException as infe:
        print(infe.message)
        return False
    return False


# Not tested
def isImgUp(imgPath, grayscale=True):
    """
        This function states if an image is on screen.
    """
    try:
        if pyautogui.locateOnScreen(
            imgPath,
            grayscale=grayscale,
            confidence=0.8,
            region=VBADimensions
        ) is not None:
            return True
    except pyautogui.ImageNotFoundException as infe:
        print(infe.message)
        return False
    return False


def imgCoordinates(imgPath, grayscale=True, confidence=0.8):
    """
        This function returns the pixel coordinates of the center of an image, if found.
        Coordinates is a 4-integer tuple: (left, top, width, height)
    """
    try:
        return pyautogui.locateOnScreen(
            imgPath,
            grayscale=grayscale,
            confidence=confidence,
            region=VBADimensions
        )
    except pyautogui.ImageNotFoundException as infe:
        print(infe.message)
        return None


def screenshot(imgPath=r'img\screenshot\newScreenshot.png', region=VBADimensions):
    pyautogui.screenshot(imgPath, region)


def compareImages(imgPathNoMap, imgPathMap):
    imgNoMap = cv2.imread(imgPathNoMap)
    imgMap = cv2.imread(imgPathMap)
    diff = cv2.absdiff(imgNoMap, imgMap)
    mask = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    th = 1
    imask = mask > th

    canvas = np.zeros_like(imgMap, np.uint8)
    canvas[imask] = imgMap[imask]

    cv2.imwrite(r'img\screenshot\mapDiff.png', canvas)


# Not tested
def isLevelUpGood():
    """
        This function checks if a level up is good and load the last save state if not.
    """


# Not tested. Lots of testing needed (VBA picture quality/background)
def extractText(imgPath):
    """
        This function extract text from pictures using a free OCR.
    """
    url = "https://freeocrapi.com/api"
    # filename = r"C:\Users\lance\OneDrive\Bureau\test.PNG"
    data = {'file': open(imgPath, 'rb')}
    response = requests.request("POST", url, files=data)
    print(response.text)
