import magicbot
import wpilib
import rev

from components.agitator import Agitator
from components.agitatorController import AgitatorController

class MyRobot(magicbot.MagicRobot):

    controller: AgitatorController
    agitator: Agitator

    def createObjects(self):
        # 16
        # self.agitator_motor = wpilib.PWMSparkMax(0)
        

        self.agitator_motor = rev.CANSparkMax(12, rev.CANSparkMax.MotorType.kBrushless)
        
        self.driver_controller = wpilib.XboxController(0)

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        try:
            if self.driver_controller.getAButton():
                self.controller.agitate()
        except:
            self.onException()

# print(type(rev.CANSparkMax(16, rev.CANSparkMax.MotorType.kBrushless)))