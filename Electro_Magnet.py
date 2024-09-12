# ELECTRO.py

import RPi.GPIO as GPIO



class ElectroMagnetControl:
    def __init__(self, pin):
        GPIO.setmode(GPIO.BCM)
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)
        self.turn_off()

    def turn_on(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def turn_off(self):
        GPIO.output(self.pin, GPIO.LOW)

    def cleanup(self):
        GPIO.cleanup(self.pin)
