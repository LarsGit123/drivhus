import RPi.GPIO as GPIO
import time
import Adafruit_DHT
import sys

def HumTemp(GPIOpin):
    hum, temp= Adafruit_DHT.read_retry(11, 19)
    humTemp= "temp: "+str(temp) + "  hum:"+str(hum)
    print humTemp    
    return humTemp
