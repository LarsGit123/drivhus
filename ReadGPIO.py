import RPi.GPIO as GPIO
import time

def Read(PinIn):
    GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
    GPIO.setup(26, GPIO.IN) # output rf
    result=GPIO.input(26)    
    GPIO.cleanup()
    return result
