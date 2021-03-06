#!/usr/bin/env python

import wiringpi2 as wp
import time

wp.wiringPiSetup()

class StepperMotor():
  def __init__(self, p1,p2,p3,p4,f=False, pos=False, delay=2):
    self.p1=p1
    self.p2=p2
    self.p3=p3
    self.p4=p4
    self.f=f
    self.pos=pos
    self.delay=delay/1000.0
    wp.pinMode(self.p1, 1)
    wp.pinMode(self.p2, 1)
    wp.pinMode(self.p3, 1)
    wp.pinMode(self.p4, 1)
    self.position=0
    if self.f:
      with open(self.f, "r") as pos_file:
        self.position=int(pos_file.read())
    if self.pos:
      self.position=self.pos
    
  def forwards(self, steps=1):
    for i in range(0, steps):
      self.setStep(1, 0, 1, 0)
      time.sleep(self.delay)
      self.setStep(0, 1, 1, 0)
      time.sleep(self.delay)
      self.setStep(0, 1, 0, 1)
      time.sleep(self.delay)
      self.setStep(1, 0, 0, 1)
      time.sleep(self.delay)
      self.setStep(0, 0, 0, 0)
      self.position+=1

  def backwards(self, steps=1):
    for i in range(0, steps):
      self.setStep(1, 0, 0, 1)
      time.sleep(self.delay)
      self.setStep(0, 1, 0, 1)
      time.sleep(self.delay)
      self.setStep(0, 1, 1, 0)
      time.sleep(self.delay)
      self.setStep(1, 0, 1, 0)
      time.sleep(self.delay)
      self.setStep(0, 0, 0, 0)
      self.position-=1
  
  def setStep(self,w1, w2, w3, w4):
    wp.digitalWrite(self.p1, w1)
    wp.digitalWrite(self.p2, w2)
    wp.digitalWrite(self.p3, w3)
    wp.digitalWrite(self.p4, w4)

  def specific(self,p):
    diff=p-self.position
    if diff>0:
      self.forward(steps=diff)
    elif diff<0:
      self.backwards(steps=(diff*-1))

  def save(self):
    with open(self.f, "w") as pos_file:
      pos_file.write(str(x_motor.position))

class Led():
  def __init__(self,p):
    self.p=p
    wp.pinMode(self.p,1)
    self.state=0

  def on(self):
    if not self.state:
      wp.digitalWrite(self.p,1)
      self.state=1

  def off(self):
    if self.state:
      wp.digitalWrite(self.p,0)
      self.state=0

class Motor():
  def __init__(self,e,f,b):
    self.e=e
    self.f=f
    self.b=b
    wp.pinMode(self.e, 1)
    wp.pinMode(self.f, 1)
    wp.pinMode(self.b, 1)
  def enable(self):
    wp.digitalWrite(self.e,1)
  def disable(self):
    wp.digitalWrite(self.e,0)
  def forwards(self):
    wp.digitalWrite(self.f,1)
    wp.digitalWrite(self.b,0)
  def backwards(self):
    wp.digitalWrite(self.f,0)
    wp.digitalWrite(self.b,1)
  def stop(self):
    wp.digitalWrite(self.f,0)
    wp.digitalWrite(self.b,0)
