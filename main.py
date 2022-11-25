import random, time
import pyautogui as pag

curr_cords = pag.position()
afk_counter = 0                # counts how long we've been afk

while True:
    if pag.position() == curr_cords:
        afk_counter += 1
    else:
        afk_counter = 0
        curr_cords = pag.position()
    if afk_counter > 5:
        x = random.randint(2560, 5120)
        y = random.randint(1, 1440)
        