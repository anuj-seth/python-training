class Robot(object):
    WHEELS = {'2-wheeled':2, '4-wheeled':4}

    def __init__(self, type):
        ..

    def charge_battery(self, increment):
        ..

    def is_battery_low(self):
        ..

    def number_of_wheels(self):
        return Robot.WHEELS.get(self.type, None)
