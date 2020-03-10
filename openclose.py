import RPi.GPIO as GPIO
import time

def openClose(pin, time = 3):
    
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

GPIO.output(12, GPIO.HIGH)

time.sleep(3)

GPIO.output(12, GPIO.LOW)

GPIO.cleanup()

