import sys
import pyautogui
import time
import pyperclip
import os
import random

conf = 0.90
def click_img(imagePath):
    location = pyautogui.locateCenterOnScreen(imagePath, confidence = conf)
    x, y = location
    pyautogui.click(x, y)
img_path = os.path.dirname(os.path.realpath(__file__)) + '/img/'

click_img(img_path + 'chat2.png')