#!/usr/bin/env python3
from time import sleep
from vilib import Vilib
import numpy as np
import cv2

def main():
    thr = 0.8 # threshold
    Vilib.camera_start(vflip=False,hflip=False)
    Vilib.show_fps()
    Vilib.show_thr_line(thr=thr, line_color=(0,255,255), line_thickness=5) # newly coded, line color:yellow
    #Vilib.show_thr_line(thr=thr, line_color=(0,0,255), line_thickness=5) # newly coded, line color:red
    Vilib.display(local=True,web=True)
    
    Vilib.hands_detect_switch(True)    
    Vilib.img = Vilib.hands_detect_fuc(Vilib.img)

    while True:
        x = Vilib.detect_obj_parameter['hands_joints']
        if x == None:
            print("out of the range")
            continue # go to the next loop
        elif x[8][0] > thr: # index finger
            print("Alert")
            break # go out of the loop
        else:
            print(Vilib.detect_obj_parameter['hands_joints']) # Print finger joint coordinates
            print("===========================")
            sleep(0.1) # check interval
        
    Vilib.hands_detect_switch(False)
    Vilib.camera_close()
            
        
if __name__ == "__main__":
    main()