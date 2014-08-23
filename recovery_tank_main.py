#!/usr/bin/env python

import cwiid
import time
import wiringpi2 as wp
import wiringpi2_helper as wph
import wii_helper as wh

wp.wiringPiSetup()

wp.mcp23s08Setup(70,0,0)


x_motor=wph.StepperMotor(71,73,70,72,f="x_motor.txt")
y_motor=wph.StepperMotor(75,77,74,76,f="y_motor.txt")

r_motor=wph.Motor(15,1,16)
l_motor=wph.Motor(15,5,4)
r_motor.enable()

def control():
    wm=wh.WiiMote()
    wm.led_set(1,1)
    wm.rumble(1)
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
    
def main():
    try:
        while True:
            try:
                control()
            except RuntimeError:
                print "Remote not connected. Try again."
    except KeyboardInterrupt:
        r_motor.disable()
        exit(1)
    
if __name__=="__main__":
    main()
