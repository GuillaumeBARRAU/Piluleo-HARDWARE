import RPi.GPIO as GPIO

class Electromagnet:
    def __init__(self, pin):
        if not isinstance(pin, int):
            raise ValueError("pin must be an integer.")
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)

    def activate(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def deactivate(self):
        GPIO.output(self.pin, GPIO.LOW)

    def cleanup(self):
        GPIO.cleanup(self.pin)
