import RPi.GPIO as GPIO
import time

class ClignLED:
    def __init__(self, led_pin):
        self.led_pin = led_pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.led_pin, GPIO.OUT)

    def pulse(self, interval=0.5):
        while True:
            GPIO.output(self.led_pin, GPIO.HIGH)
            time.sleep(interval)
            GPIO.output(self.led_pin, GPIO.LOW)
            time.sleep(interval)

    def stop(self):
        GPIO.output(self.led_pin, GPIO.LOW)

    def cleanup(self):
        GPIO.cleanup(self.led_pin)
