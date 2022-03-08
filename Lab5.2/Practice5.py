import RPi.GPIO as GPIO
import time

led1 = [37, 35, 33, 31]
button = 29

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(button, GPIO.IN)

while True:
    if GPIO.input(button) == 0:
        for i in range(4):
            GPIO.output(led1[i], 1)
            time.sleep(0.2)
            GPIO.output(led1[i], 0)
    else:
        for i in range(4):
            GPIO.output(led1[3-i], 1)
            time.sleep(0.2)
            GPIO.output(led1[3-i], 0)