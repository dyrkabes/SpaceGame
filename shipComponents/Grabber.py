import math

from Constants import ShipConstants
from shipComponents.Component import Component


class Grabber(Component):
    def __init__(self, ship):
        Component.__init__(self, ShipConstants.GRABBER, ship)
        self.power = 66
        self.distance_max = 80
        self.grabbing_speed_max = 0.1
        self.name = ShipConstants.GRABBER
        self.hitpoints = 1
        # self.grabber_perfoming = ship.stop
        self.get_ship_coordinates = ship.get_coordinates

    def get_distance(self):
        return self.distance_max

    def interact(self, target):
        delta_x = target.x_coordinate - self.get_ship_coordinates()[0]
        delta_y = target.y_coordinate - self.get_ship_coordinates()[1]

        delta_x = delta_x / math.fabs(delta_x)
        delta_y = delta_y / math.fabs(delta_y)
        target.x_coordinate -= delta_x * self.grabbing_speed_max
        target.y_coordinate -= delta_y * self.grabbing_speed_max

    def load_modules(self):
        pass

    # TODO: obv
    # def get_damage(self, damage):
    #     print("MESSAGE: grabber")
    #     # self.hitpoints -= damage
    #     # if self.hitpoints <= 0:
    #     #     self.movement_speed = self.movement_speed_max / 50
    #     #     self.engine_state_changed()
        #     print(self.movement_speed)
