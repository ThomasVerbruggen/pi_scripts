import RPi.GPIO as GPIO
import time


led1 = [11, 13, 15, 16]

GPIO.setmode(GPIO.BOARD)
for i in range(4):
    GPIO.setup(led1[i], GPIO.OUT)


while True:
    for i in range(4):
        GPIO.output(led1[i], 1)
    time.sleep(0.5)
    for i in range(4):
        GPIO.output(led1[i], 0)
    time.sleep(0.5)