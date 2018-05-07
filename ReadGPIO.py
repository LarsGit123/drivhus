import RPi.GPIO as GPIO
import time

def Read(PinIn):
    GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
    GPIO.setup(PinIn, GPIO.IN) # output rf
    result=GPIO.input(PinIn)    
    GPIO.cleanup()
    print("Reset GPIO pins")
    return result
