import RPi.GPIO as GPIO

class PushButton:
    def __init__(self, button_pin, callback):
        self.button_pin = button_pin
        self.callback = callback
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.button_pin, GPIO.FALLING, callback=self.callback, bouncetime=200)

    def cleanup(self):
        GPIO.cleanup(self.button_pin)