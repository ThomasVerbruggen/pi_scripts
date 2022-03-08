import RPi.GPIO as GPIO
import time

led1 = 37
button = 29

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(button, GPIO.IN)

while True:
    if GPIO.input(button) == 0:
        GPIO.output(led1, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(led1, GPIO.LOW)
        time.sleep(0.1)
        print("led blinks")
    else:
        GPIO.output(led1, GPIO.LOW)
        print("Led not flashing")