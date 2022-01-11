from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

while 1:
    # obj = pyautogui.locateAllOnScreen('stickman.png', confidence=0.9)
    # print(list(obj))
    obj = pyautogui.locateOnScreen('stickman.png', confidence=0.8)
    print(obj)
    if obj != None:
        print("I can see it")
        time.sleep(0.5)
    else:
        print("I am unable to see it")
        time.sleep(0.5)