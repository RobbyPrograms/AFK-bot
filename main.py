import pyautogui as pag
import random, time, msvcrt

curr_cords = pag.position()                                    # current cords of curser
afk_counter = 0                                                # counts how long we've been afk

def kbfunc():
    #this is boolean for whether the keyboard has bene hit
    x = msvcrt.kbhit()
    if x:
        #getch acquires the character encoded in binary ASCII
        ret = msvcrt.getch()
        ret = True
    else:
        ret = False
    return ret

while True:

    if pag.position() == curr_cords and kbfunc() == False:     # if true this means mouse hasn't moved since last loop   
        afk_counter += 1                                       # starts adding because mouse hasn't moved or keys haven't been pressed 

    else:
        afk_counter = 0                                        # resets to 0 if mouse is moved or keyboard has been clicked
        curr_cords = pag.position()                            # updates curr_cords when we move the mouse 
        kbfunc()                                               # updates to see if there's any new key presses

    if afk_counter > 20:                                       # starts to move mouse after 20 seconds
        x = random.randint(1, 1918)                            # size of screen 
        y = random.randint(1, 1078)                            # y size of screen
        pag.moveTo(x, y, 0.5)                                  # Moves mouse to random cords at a 0.5 speed
        curr_cords = pag.position()                            # updates curr_cords

    print("Afk Counter: {}".format(afk_counter) + " Current Cordinates {}".format(curr_cords))
    time.sleep(0.7)                                            # doesn't execute next loop for 0.7 seconds
        