import pyautogui as pag
import random
import time

while True:
    x = random.randint(700,1300)
    y = random.randint(200,600)
    pag.moveTo(x,y,0.5)
    time.sleep(60)