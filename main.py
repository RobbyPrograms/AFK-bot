import pyautogui as pag
import random, time

curr_cords = pag.position()    # current cords of curser
afk_counter = 0                # counts how long we've been afk

while True:
    if pag.position() == curr_cords:     # if true this means mouse hasn't moved since last loop   
        afk_counter += 1                 # starts adding because mouse hasn't moved
    else:
        afk_counter = 0                  # resets to 0 if mouse is moved
        curr_cords = pag.position()      # updates curr_cords when we move the mouse 
    if afk_counter > 5:              # starts to move mouse after 5 seconds
        x = random.randint(1, 1918)  # size of screen 
        y = random.randint(1, 1078)  # y size of screen
        pag.moveTo(x, y, 0.5)        # Moves mouse to random cords at a 0.5 speed
        curr_cords = pag.position()  # updates curr_cords
    print("Afk Counter: {}".format(afk_counter) + " Current cordinates {}".format(curr_cords))
    time.sleep(2)                    # doesn't execute next loop for 2 seconds
        