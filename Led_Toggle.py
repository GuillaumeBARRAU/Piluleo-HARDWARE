import RPi.GPIO as GPIO

class ToggleLED:
    def __init__(self, led_pin):
        self.led_pin = led_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.led_pin, GPIO.OUT)

    def on(self):
        GPIO.output(self.led_pin, GPIO.HIGH)

    def off(self):
        GPIO.output(self.led_pin, GPIO.LOW)

    def cleanup(self):
        GPIO.cleanup(self.led_pin)
