class Robot(object):
    WHEELS = {'2-wheeled':2, '4-wheeled':4}

    def __init__(self, type):
        self.type = type
        self.charge = 0

    def charge_battery(self, increment):
        self.charge += increment
        if self.charge > 100:
            self.charge = 100

    def is_battery_low(self):
        return self.charge < 40

    def number_of_wheels(self):
        return Robot.WHEELS.get(self.type, None)

class BiPedal(Robot):
    def __init__(self):
        Robot.__init__(self, 'bi-pedal')

    def is_battery_low(self):
        return self.charge < 60
