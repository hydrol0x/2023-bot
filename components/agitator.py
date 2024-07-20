import wpilib


class Agitator:
    agitator_motor: wpilib.PWMSparkMax

    def __init__(self):
        self.enabled = False

    def enable(self):
        # Agitator spins
        self.enabled = True

    def execute(self):
        """This gets called at the end of the control loop"""
        if self.enabled:
            self.agitator_motor.set(0.5)  # set motor to spin
        else:
            self.agitator_motor.set(0)

        self.enabled = False
