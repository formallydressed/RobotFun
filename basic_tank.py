#!/usr/bin/env python

import cwiid
import time
import wiringpi2 as wp
import wiringpi2_helper as wph
import wii_helper as wh

wp.wiringPiSetup()

r_motor=wph.Motor(0,1,2)
l_motor=wph.Motor(0,3,4)

def control():
    wm=wh.WiiMote()
    wm.led_set(1,1)
    wm.rumble(1)
    r_motor.enable()
    while not (wm.button_plus() and wm.button_minus()):
        if wm.button_up():
            r_motor.forwards()
            l_motor.backwards()
        elif wm.button_down():
            r_motor.backwards()
            l_motor.forwards()
        elif wm.button_right():
            r_motor.forwards()
            l_motor.forwards()
        elif wm.button_left():
            l_motor.backwards()
            r_motor.backwards()
        else:
            l_motor.stop()
            r_motor.stop()
    wm.rumble(1)
    print "Closing connection..."
    wm.led_set()
    r_motor.disable()
    
def main():
    try:
        while True:
            try:
                control()
            except RuntimeError:
                print "Remote not connected. Try again."
    except KeyboardInterrupt:
        exit(1)
    
if __name__=="__main__":
    main()
