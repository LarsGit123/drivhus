import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme

GPIO.setup(26, GPIO.OUT) # output rf

# Initial state for LEDs:
print("Testing RF out, Press CTRL+C to exit")

try:
     while True:    
          try:
               print("set GIOP high")
               GPIO.output(26, GPIO.HIGH)
               time.sleep(1)
               print("set GIOP low")
               GPIO.output(26, GPIO.LOW)
               time.sleep(1)
          except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
               print("Keyboard interrupt")
               break
          except:
               print("some error")
               break
finally:
     print("clean up") 
     GPIO.cleanup() # cleanup all GPIO
