import RPi.GPIO as GPIO
import time

led1 = 11
button = 13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(button, GPIO.IN)

while True:
    if GPIO.input(button) == 1:
        GPIO.output(led1, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(led1, GPIO.LOW)
        time.sleep(0.1)
    else:
        GPIO.output(led1, GPIO.LOW)