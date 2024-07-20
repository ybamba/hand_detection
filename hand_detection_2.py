#!/usr/bin/env python3
from time import sleep
from vilib import Vilib

def main():
    Vilib.camera_start(vflip=False,hflip=False)
    Vilib.display(local=True,web=True)
    
    Vilib.hands_detect_switch(True)
    Vilib.hands_detect_fuc(Vilib.img) # added

    while True:
        print(Vilib.detect_obj_parameter['hands_joints']) # Print finger joint coordinates
        print("===========================")
        sleep(0.5)
        
        if Vilib.detect_obj_parameter['hands_joints'][8][0] > 0.7:
            print("Alert")
            break
        
    Vilib.hands_detect_switch(False)
    Vilib.camera_close()
            
        
if __name__ == "__main__":
    main()