import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

def blink(pin, aantalBlinks, periode, dutyCycle):
    GPIO.setup(pin, GPIO.OUT)
    tijdhoog = periode * dutyCycle/100
    tijdlaag = periode - tijdhoog
    for teller in range (0, aantalBlinks):
        GPIO.output(pin, 1)
        time.sleep(tijdhoog)
        GPIO.output(pin, 0)
        time.sleep(tijdlaag)

blink(11, 20, 0.5, 75)

GPIO.cleanup()