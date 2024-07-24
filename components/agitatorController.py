from magicbot import StateMachine, state
from components.agitator import Agitator


class AgitatorController(StateMachine):
    agitator: Agitator

    def agitate(self):
        # called to turn on agitator
        self.engage()

    @state(first=True)
    def prepare_agitate(self):

        self.agitator.enable()

        # Check some condition like there is intake piece then:
        # self.next_state_now("firing")
