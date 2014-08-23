#!/usr/bin/env python

import wiringpi2 as wp
import wiringpi2_helper as wph
import time


wp.wiringPiSetup()

wp.mcp23s08Setup(70,0,0)

stepper1=wph.StepperMotor(71,73,70,72,f="x_motor.txt")
stepper2=wph.StepperMotor(75,77,74,76,f="y_motor.txt")

r_motor=wph.Motor(15,1,16)
l_motor=wph.Motor(15,5,4)
r_motor.enable()

r_motor.forwards()
l_motor.forwards()
time.sleep(2)
r_motor.stop()
l_motor.stop()
#time.sleep(2)
#r_motor.backwards()
#l_motor.forwards()
#time.sleep(2)
#r_motor.stop()
#l_motor.stop()
#time.sleep(2)
#l_motor.backwards()
#r_motor.forwards()
#time.sleep(2)
#r_motor.stop()
#l_motor.stop()
#time.sleep(2)
#r_motor.backwards()
#l_motor.backwards()
#time.sleep(2)
#r_motor.stop()
#l_motor.stop()



r_motor.disable()
