#!/usr/bin/python
# Import required libraries
import sys
import time
import RPi.GPIO as GPIO


#time.sleep(10) 
# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO signals to use
# Physical pins 11,15,16,18
# GPIO17,GPIO22,GPIO23,GPIO24
StepPins = [17,22,23,24]

# Set all pins as output
for pin in StepPins:
  print "Setup pins"
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin, False)

# Define advanced sequence
# as shown in manufacturers datasheet
Seq = [[1,0,0,1],
       [1,0,0,0],
       [1,1,0,0],
       [0,1,0,0],
       [0,1,1,0],
       [0,0,1,0],
       [0,0,1,1],
       [0,0,0,1]]


StepCount = len(Seq)
StepDir = 1 # Set to 1 or 2 for clockwise
            # Set to -1 or -2 for anti-clockwise

# Read wait time from command line
if len(sys.argv)>1:
  WaitTime = int(sys.argv[1])/float(1000)
else:
  WaitTime = 10/float(1000)

# maxCounter
if len(sys.argv)>2:
  maxCounter = int(sys.argv[2])
else:
  maxCounter = 6000 #= environ 1/2 tour

# sens de rotation
if len(sys.argv)>3:
  rotate = int(sys.argv[3])
else:
  rotate = 1

# Initialise variables
StepCounter = 0
counter = 0
if rotate == 2 : StepDir = StepDir * -1

# Start main loop
while True:
  #if counter == maxCounter: break
  print StepCounter,
  print Seq[StepCounter]

  for pin in range(0,4):
    xpin=StepPins[pin]# Get GPIO
    if Seq[StepCounter][pin]!=0:
      print " Enable GPIO %i" %(xpin)
      GPIO.output(xpin, True)
    else:
      GPIO.output(xpin, False)

  StepCounter += StepDir

  # If we reach the end of the sequence
  # start again
  if (StepCounter>=StepCount):
    StepCounter = 0
  if (StepCounter<0):
    StepCounter = StepCount+StepDir

  counter = counter + 1
  # Wait before moving on
  time.sleep(WaitTime)
  #time.sleep(1)

# Couper le moteur
for pin in range(0,4):
  xpin=StepPins[pin]# Get GPIO
  GPIO.output(xpin, False)
