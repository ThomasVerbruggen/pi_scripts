#!/usr/bin/python3

import RPi.GPIO as GPIO
import time


led1 = 11
led2 = 13
led3 = 15
led4 = 16

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(led4, GPIO.OUT)

for i in range(10):
    GPIO.output(led1, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(led2, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(led3, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(led4, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(led1, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(led2, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(led3, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(led4, GPIO.LOW)
    time.sleep(0.1)