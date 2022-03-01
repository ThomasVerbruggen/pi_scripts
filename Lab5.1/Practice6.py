import RPi.GPIO as GPIO
import time


led1 = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led1, GPIO.OUT)

while True:
        GPIO.output(led1, 1)
        time.sleep(0.5)
        GPIO.output(led1, 0)
        time.sleep(0.5)
        GPIO.output(led1, 1)
        time.sleep(1.5)
        GPIO.output(led1, 0)
        time.sleep(0.5)
        GPIO.output(led1, 1)
        time.sleep(0.5)
        GPIO.output(led1, 0)
        time.sleep(0.5)