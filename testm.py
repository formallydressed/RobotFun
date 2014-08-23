#!/usr/bin/env python

import wiringpi2 as wp
import wiringpi2_helper as wph
import time


wp.wiringPiSetup()

motor=wph.Motor(1,4,5)

motor.enable()

motor.forwards()
time.sleep(5)
motor.backwards()
time.sleep(5)
motor.stop()
motor.disable
