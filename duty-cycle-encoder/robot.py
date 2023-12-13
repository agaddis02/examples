import wpilib
from wpilib import DutyCycleEncoder, TimedRobot

class   Robot(TimedRobot):
    def robotInit(self):
        self.dutyCycleEncoder = DutyCycleEncoder(0)

        # Set to 0.5 units per rotation
        self.dutyCycleEncoder.setDistancePerRotation(0.5)

    def robotPeriodic(self):
        # Connected can be checked, and uses the frequency of the encoder
        connected = self.dutyCycleEncoder.isConnected()

        # Duty Cycle Frequency in Hz
        frequency = self.dutyCycleEncoder.getFrequency()

        # Output of encoder
        output = self.dutyCycleEncoder.get()

        # Output scaled by DistancePerPulse
        distance = self.dutyCycleEncoder.getDistance()
        
        wpilib.SmartDashboard.putBoolean("Connected", connected)
        wpilib.SmartDashboard.putNumber("Frequency", frequency)
        wpilib.SmartDashboard.putNumber("Output", output)
        wpilib.SmartDashboard.putNumber("Distance", distance)

if __name__ == "__main__":
    wpilib.run(Robot)
