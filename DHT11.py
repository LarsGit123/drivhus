import RPi.GPIO as GPIO
import time
import Adafruit_DHT
import sys

hum, temp= Adafruit_DHT.read_retry(11,4)
print "temp:   "+str(temp)
print "hum:   "+str(hum)
