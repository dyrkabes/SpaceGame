import Constants
from managers.DamageProcessor import DamageProcessor

import math


class CollisionManager:
    """
    Checks if any objects collide
    """
    def __init__(self):
        """
        For now all objects capable of colliding are placed in one
        list. In the future for better optimization I will palce
        them in different lists
        """
        self.collidables = []
        self.current_system = None
        self.object_processor = None
        self.GUI = None

    def init_current_system(self, current_system):
        self.current_system = current_system

    def init_object_processor(self, object_processor):
        self.object_processor = object_processor

    def process_entity(self, entity):
        """
        Adds a new entity to collidable list
        """
        self.collidables.append(entity)

    def remove_entity(self, entity):
        """
        Removes entity from the list
        """
        if entity.type == Constants.GeneralConstants.SHIP:
            # TODO: animation
            pass
        try:
            self.collidables.remove(entity)
        except ValueError:
            print("Value error catched")

    def check_collided(self):
        """
        Checks if any objects collided in this tick
        In case of collision delegates it further to DamageProcessor
        """
        num = 0
        for collidable in self.collidables:
            num += 1
            for collidable_pair in self.collidables[num:]:
                if (collidable.type != Constants.GeneralConstants.BULLET or
                        collidable_pair.type != Constants.GeneralConstants.BULLET):
                    if (
                        math.hypot((collidable.x_coordinate - collidable_pair.x_coordinate),
                                   (collidable.y_coordinate - collidable_pair.y_coordinate))
                                   <= (collidable.x_size + collidable_pair.x_size)/2
                    ):
                        DamageProcessor.process_collision(collidable,
                                                          collidable_pair,
                                                          self.object_processor.create_info_label)
