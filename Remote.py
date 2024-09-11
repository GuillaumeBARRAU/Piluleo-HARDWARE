from Bouton_Hold import MaintainButton
from Led_Pulse import ClignLED

class Remote:
    def __init__(self, button_pin, led_pin):
        self.led = ClignLED(led_pin)
        self.button = MaintainButton(button_pin, self.handle_remote)
        self.is_active = False

    def handle_remote(self, channel):
        if GPIO.input(self.button.button_pin) == GPIO.LOW:
            self.led.pulse()
        else:
            self.led.stop()

    def cleanup(self):
        self.led.cleanup()
        self.button.cleanup()
