class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours % 24
        self.minutes = minutes % 60
        self.seconds = seconds % 60

    def increment_second(self):
        self.seconds += 1
        if self.seconds >= 60:
            self.seconds = 0
            self.minutes += 1
            if self.minutes >= 60:
                self.minutes = 0
                self.hours = (self.hours + 1) % 24

    def decrement_second(self):
        self.seconds -= 1
        if self.seconds < 0:
            self.seconds = 59
            self.minutes -= 1
            if self.minutes < 0:
                self.minutes = 59
                self.hours = (self.hours - 1) % 24
print(Time)

