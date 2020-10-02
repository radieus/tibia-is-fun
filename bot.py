import pyautogui
import time
import threading
import sys
import datetime

delay = 1
running = True
mx = 0
my = 0
hotkey = 'f9'
food_delay = 144

pyautogui.FAILSAFE = False

def findImage(image):
    global mx
    global my
    image = image + ".png"
    try:
        mx, my = pyautogui.locateCenterOnScreen(image, region=(960, 0, 1920, 1080))
        print("true for " + image)
        return True
    except:
        print("false for " + image)
        return False  


def eatFood():
    meat = ['meat1', 'meat2', 'meat3', 'meat4', 'meat5']
    for item in reversed(meat):
        if findImage(item):
            pyautogui.click(x=mx, y=my, button='right', clicks=5, interval=0.5)
            time.sleep(delay)
        if item != meat[-1]:
            del meat[-1]


def makeRunes(custom_key):
    try:
        if findImage('mana'):
            if findImage('blank'):
                runex = mx
                runey = my
                print(runex, runey)
                pyautogui.keyDown(custom_key)
                pyautogui.keyUp(custom_key)
    except:
        print("no blanks in bp")
        return False  


def isLast(li, item):
        if item == li[-1]:
            return True
        else:
            return False

print("palson powah")

script_local_time = 0
while running:
    try:
        makeRunes(hotkey)

        if script_local_time >= food_delay:
            eatFood()
            script_local_time = 0
        else:
            script_local_time += 5

        print(script_local_time)
    except Exception:
        print(Exception)
        
sys.exit()