from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

# 593, 540
# 688, 582
# 774, 555
# 857, 574


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    


while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(593, 430)[0] == 0:
        click(593, 430)
    if pyautogui.pixel(688, 430)[0] == 0:
        click(688, 430)
    if pyautogui.pixel(774, 430)[0] == 0:
        click(774, 430)
    if pyautogui.pixel(857, 430)[0] == 0:
        click(857, 430)
