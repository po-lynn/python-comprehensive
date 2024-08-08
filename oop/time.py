import time


# Define a digital clock class
class Clock(object):
    """Digital clock"""

    def __init__(self, hour=0, minute=0, second=0):
        """initialization method
        :param hour: hour
        :param minute: minute
        :param second: Second
        """
        self.hour = hour
        self.min = minute
        self.sec = second

    def run(self):
        """Walk the word"""
        self.sec += 1
        if self.sec == 60:
            self.sec = 0
            self.min += 1
            if self.min == 60:
                self.min = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0

    def show(self):
        """display time"""
        return f'{self.hour:0>2d}:{self.min:0>2d}:{self.sec:0>2d}'


# Create a clock object
clock = Clock(23, 59, 58)
while True:
    # Send a message to the clock object to read the time
    print(clock.show())
    # Sleep for 1 second
    time.sleep(1)
    # Send a message to the clock object to make it tick
    clock.run()