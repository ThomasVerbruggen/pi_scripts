import RPi.GPIO as GPIO
import time


led1 = [11, 15]
led2 = [13, 16]

GPIO.setmode(GPIO.BOARD)
for i in range(2):
    GPIO.setup(led1[i], GPIO.OUT)
for i in range(2):
    GPIO.setup(led2[i], GPIO.OUT)


while True:
    for i in range(2):
        GPIO.output(led1[i], 1)
        GPIO.output(led2[i], 0)
    time.sleep(1)
    for i in range(2):
        GPIO.output(led1[i], 0)
        GPIO.output(led2[i], 1)
    time.sleep(1)