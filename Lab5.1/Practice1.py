import RPi.GPIO as GPIO
import time

led1 = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led1, GPIO.OUT)

while True:
    GPIO.output(led1, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(led1, GPIO.LOW)
    time.sleep(0.1)