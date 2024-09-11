import RPi.GPIO as GPIO
import time
import Config

class RotateStepMotor:
    def __init__(self, in1, in2, in3, in4):
        self.IN1 = in1
        self.IN2 = in2
        self.IN3 = in3
        self.IN4 = in4

        # Configurer les broches GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.IN1, GPIO.OUT)
        GPIO.setup(self.IN2, GPIO.OUT)
        GPIO.setup(self.IN3, GPIO.OUT)
        GPIO.setup(self.IN4, GPIO.OUT)

        # Séquence pour le moteur pas à pas (demi-pas)
        self.step_sequence = [
            [1, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 1, 1],
            [0, 0, 0, 1],
            [1, 0, 0, 1],
        ]

        # Nombre de pas par position
        self.steps_per_position = [73, 73, 73, 73, 73, 73, 73, 74]

    def set_step(self, step):
        GPIO.output(self.IN1, step[0])
        GPIO.output(self.IN2, step[1])
        GPIO.output(self.IN3, step[2])
        GPIO.output(self.IN4, step[3])

    def move_one_step(self):
        for step in self.step_sequence:
            self.set_step(step)
            time.sleep(0.01)

    def move_automatically(self):
        while True:
            for position in range(len(self.steps_per_position)):
                print(f"Déplacement vers la position {position}")
                steps = self.steps_per_position[position]
                for _ in range(steps):
                    self.move_one_step()
                time.sleep(5)

    def cleanup(self):
        GPIO.cleanup()
