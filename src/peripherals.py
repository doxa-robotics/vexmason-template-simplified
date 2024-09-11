from vex import *


class Peripherals:
    brain: Brain
    inertial: Inertial
    left_motors_list: list[Motor]
    left_motors: MotorGroup
    right_motors_list: list[Motor]
    right_motors: MotorGroup

    WHEEL_TRAVEL_MM: int
    WHEEL_TRACK_WIDTH_MM: int


class RobotPeripherals(Peripherals):
    """Peripheral config for the robot.

    This is a _subclass_ of Peripherals. This is because there can be many
    different _types_ of Peripherals (for example, we had a test bot last year
    as well as a real one), so subclasses let us express that relationship.
    """

    WHEEL_TRAVEL_MM = 460
    WHEEL_TRACK_WIDTH_MM = 305

    def __init__(self) -> None:
        self.brain = Brain()
        self.controller = Controller()
        self.inertial = Inertial(Ports.PORT6)

        self.left_motors_list = [
            # Left motors list here
        ]
        self.left_motors = MotorGroup(*self.left_motors_list)
        self.right_motors_list = [
            # Right motors list here
        ]
        self.right_motors = MotorGroup(*self.right_motors_list)