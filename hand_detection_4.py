from time import sleep
import RPi.GPIO as GPIO
from vilib import Vilib
# import numpy as np
# import cv2

# Set GPIO17 as LED pin
LedPin_red = 17
LedPin_green = 27
# Set GPIO17 as buzzer pin
BeepPin = 22

def setup():
    # Set the GPIO modes to BCM Numbering
    GPIO.setmode(GPIO.BCM)
    # Set LedPin's mode to output,and initial level to High(3.3v)
    GPIO.setup(LedPin_red, GPIO.OUT, initial=GPIO.HIGH)
    GPIO.setup(LedPin_green, GPIO.OUT, initial=GPIO.HIGH)
    # Set BeepPin's mode to output,and initial level to High(3.3v)
    GPIO.setup(BeepPin, GPIO.OUT, initial=GPIO.HIGH)

def destroy():
    # Turn off LED
    GPIO.output(LedPin_red, GPIO.HIGH)
    GPIO.output(LedPin_green, GPIO.HIGH)
    # Turn off buzzer
    GPIO.output(BeepPin, GPIO.HIGH)
    # Release resource
    GPIO.cleanup()
    Vilib.hands_detect_switch(False)
    Vilib.camera_close()

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
        # Turn off LED
        GPIO.output(LedPin_red, GPIO.HIGH)
        GPIO.output(LedPin_green, GPIO.HIGH)
        # Turn off buzzer
        GPIO.output(BeepPin, GPIO.HIGH)
        # get hands_joints' cordination
        x = Vilib.detect_obj_parameter['hands_joints']
        
        if x == None:
            print("out of the range")
            sleep(0.1) # check interval
            continue # go to the next loop

        elif x[8][0] > thr: # index finger
            print("Alert")
            # break # go out of the loop
            # Turn on red LED
            GPIO.output(LedPin_red, GPIO.LOW)
            # Buzzer on (Beep)
            GPIO.output(BeepPin, GPIO.LOW)
            sleep(0.1) # check interval

        else:
            print(Vilib.detect_obj_parameter['hands_joints']) # Print finger joint coordinates
            print("===========================")
            # Turn on green LED
            GPIO.output(LedPin_green, GPIO.LOW)
            sleep(0.1) # check interval
        
if __name__ == "__main__":
    setup()
    try:
        main()
    # When 'Ctrl+C' is pressed, the program destroy() will be executed.
    except KeyboardInterrupt:
        destroy()