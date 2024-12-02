# week13_B_car.py

from datetime import datetime as dt

class Car1:
    def __init__(self, number, intime, outtime=None):
        self.number = number
        self.intime = intime
        self.outtime = outtime

    def diff_seconds(self):
        if self.outtime == None:
            outtime = dt.now()
        else:
            outtime = self.outtime
        return (self.outtime - self.intime).total_seconds()
