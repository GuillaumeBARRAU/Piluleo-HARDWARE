import Config
from Power import Power
from Remote import Remote
from Alert import Alert
from RotateStepMotor import StepperMotorController

def main():
    # Initialisation des composants
    power = Power(Config.POWER_BUTTON_PIN, Config.POWER_LED_PIN)
    remote = Remote(Config.CONNECT_BUTTON_PIN, Config.CONNECTION_LED_PIN)
    alert = Alert(Config.ALERT_BUTTON_PIN)
    motor = StepperMotorController(Config.MOTOR_PINS[0], Config.MOTOR_PINS[1], Config.MOTOR_PINS[2], Config.MOTOR_PINS[3])

    try:
        # Le moteur tourne en continu (tests)
        motor.move_automatically()
    except KeyboardInterrupt:
        print("Programme interrompu.")
    finally:
        motor.cleanup()

if __name__ == "__main__":
    main()
