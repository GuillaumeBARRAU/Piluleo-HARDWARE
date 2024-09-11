from Bouton_Toggle import PushButton
from Led_Toggle import ToggleLED

class Power:
    def __init__(self, button_pin, led_pin):
        self.led = ToggleLED(led_pin)
        self.button = PushButton(button_pin, self.toggle_power)
        self.is_on = False

    def toggle_power(self, channel):
        if self.is_on:
            self.led.off()
        else:
            self.led.on()
        self.is_on = not self.is_on

    def cleanup(self):
        self.led.cleanup()
        self.button.cleanup()
