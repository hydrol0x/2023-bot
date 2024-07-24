import wpilib
import rev

class Agitator:
    agitator_motor: rev._rev.CANSparkMax

    def __init__(self):
        self.enabled = False

    def enable(self):
        # Agitator spins
        self.enabled = True

    def execute(self):
        """This gets called at the end of the control loop"""
        if self.enabled:
            self.agitator_motor.set(0.8)  # set motor to spin
            print("HIGH")
        else:
            self.agitator_motor.set(0)
            print("LOW")
        self.enabled = False
