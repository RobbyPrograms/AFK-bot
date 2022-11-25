import random, time
import pyautogui as pag

curr_cords = pag.position()    # current cords of curser
afk_counter = 0                # counts how long we've been afk

while True:
    if pag.position() == curr_cords:
        afk_counter += 1
    else:
        afk_counter = 0
        curr_cords = pag.position()
    if afk_counter > 5:
        x = random.randint(0, 1919)  # size of screen 
        y = random.randint(0, 1079)  # y size of screen
        pag.moveTo(x, y, 0.5)        # 0.5 is the speed
        curr_cords = pag.position()  # updates curr_cords
    print("Afk Counter: {}".format(afk_counter) + " Current cordinates {}".format(curr_cords))
    time.sleep(2)
        