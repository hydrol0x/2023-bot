import magicbot
import wpilib

from components.agitator import Agitator
from components.agitatorController import AgitatorController


class MyRobot(magicbot.MagicRobot):

    controller: AgitatorController
    agitator: Agitator

    def createObjects(self):
        self.agitator_motor = wpilib.PWMSparkMax(0)
        self.driver_controller = wpilib.XboxController(0)

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        try:
            if self.driver_controller.getAButton():
                self.controller.agitate()
        except:
            self.onException()
