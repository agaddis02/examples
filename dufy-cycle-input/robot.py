import wpilib
from wpilib import DigitalInput, DutyCycle, TimedRobot

class Robot(TimedRobot):
    def robotInit(self):
        self.dutyCycle = DutyCycle(DigitalInput(0))

    def robotPeriodic(self):
        # Duty Cycle Frequency in Hz
        frequency = self.dutyCycle.getFrequency()

        # Output of duty cycle, ranging from 0 to 1
        # 1 is fully on, 0 is fully off
        output = self.dutyCycle.getOutput()

        wpilib.SmartDashboard.putNumber("Frequency", frequency)
        wpilib.SmartDashboard.putNumber("Duty Cycle", output)

if __name__ == "__main__":
    wpilib.run(Robot)
