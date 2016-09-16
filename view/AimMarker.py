
from Entity import Entity
import Constants

import math


class AimMarker(Entity):
    def __init__(self, target, x_size=4, y_size=4, type=Constants.GeneralConstants.AIM_MARKER):

        Entity.__init__(self, self.shift_from_target(target.x_coordinate),
                        self.shift_from_target(target.y_coordinate), x_size, y_size,
                        type)

        self.target = target
        self.rotatable = False

        self.collidable_type = Constants.CollidableTypes.NON_COLLIDABLE
        # self.type = Constants.GeneralConstants.AIM_MARKER


        self.images_names = ["aim_marker.png"]


    def move(self):
        self.x_coordinate = self.shift_from_target(self.target.x_coordinate)
        self.y_coordinate = self.shift_from_target(self.target.y_coordinate)

    def act(self):
        self.move()

    def shift_from_target(self, coordinate):
        return coordinate - 5

    def target_destroyed(self, target):
        self.destroy()

