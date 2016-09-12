import pygame

from Entity import Entity

class ComponentModule(Entity):
    def __init__(self, component_type, name="module"):
        Entity.__init__(self, 0, 0, 25, 25)
        self.component_type = component_type
        self.types_and_values = []
        self.hit_points = 2

        self.restrictions_types_and_values = []

        self.images_names = ["module.png"]

        self.name = name
        self.animatable = False

    def add_module_type_and_value(self, type, value):
        self.types_and_values.append((type,value))

    def get_types_and_values(self):
        return self.types_and_values

    def add_module_restriction(self, type, value):
        self.restrictions_types_and_values.append((type,value))

    def get_restrictions_types_and_values(self):
        return self.restrictions_types_and_values

    def init_absolute_pos(self, pos):
        self.x_coordinate = pos[0]
        self.y_coordinate = pos[1]