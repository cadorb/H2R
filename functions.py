# -*- coding: UTF-8 -*-
import RPi.GPIO as GPIO
import time

filename = "status.txt"


def writefile(position):
    """
    @usage:
    writefile(message)
    """
    logfile = file(filename, "w")
    logfile.write(str(position))
    logfile.close()


def readfile():
    entete = file(filename, "r").readline().rstrip('\n\r')
    return int(entete)

def rotor(old_step,new_step):
    try:
        if new_step == old_step: #
            StepDir = -1
            cnt = 0
        elif new_step < old_step: # 60 < 360
            StepDir = 1
            cnt = old_step - new_step  # cnt = 360 - 60 = 300
        elif new_step > old_step:
            StepDir = -1
            cnt = new_step - old_step

        print "####\n"
        print cnt
        print "####\n"


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
        """
        StepDir = 1 # Set to 1 or 2 for clockwise
                    # Set to -1 or -2 for anti-clockwise
        """

        # Read wait time from command line
        tmr = 5
        WaitTime = int(tmr)/float(1000)

        # maxCounter 100°
        maxCounter = int(cnt) * 11.4
        if maxCounter > 4100: maxCounter = 4100


        print "####\n"
        print maxCounter
        print "####\n"


        # Initialise variables
        StepCounter = 0
        counter = 0

        # Start main loop
        while counter <= 4100:
            if counter == maxCounter: break
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

        # Couper le moteur
        for pin in range(0,4):
            xpin=StepPins[pin]# Get GPIO
            GPIO.output(xpin, False)

        return True
    except :
        return False