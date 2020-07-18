class Robot(object):
    def __init__(self, robot_type):
        self.robot_type = robot_type
        self.charge = 0

    def charge_battery(self, increment):
        self.charge += increment
        if self.charge > 100:
            self.charge = 100

    def is_battery_low(self):
        return self.charge < 40
