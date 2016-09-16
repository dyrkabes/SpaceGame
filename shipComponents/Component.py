import pygame
import random

from Entity import Entity


class Component(Entity):
    def __init__(self, type, ship):
        Entity.__init__(self, 0, 0, 50, 50, type=None)
        self.type = type
        self.state_manager = ship.state_manager
        self.modules = []

        self.parameters = {}

        self.images_names = ["component.png"]
        self.image = None

    def init_position(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def get_damage(self, damage):
        self.state_manager.new_message(self.type)
        alive_modules = [module for module in self.modules if module.hit_points]
        if alive_modules:
            module_damaged = random.choice(alive_modules)
            module_damaged.hit_points -= 1


    def add_module(self, module):
        self.modules.append(module)

    def load_modules(self):
        for module in self.modules:
            for type_and_value in module.get_types_and_values():
                type, value = type_and_value[0], type_and_value[1]
                if module.hit_points == 1:
                    value /= 2
                elif not module.hit_points:
                    value /= 4
                self.parameters[type] = value

            for restriction in module.get_restrictions_types_and_values():
                type, value = restriction[0], restriction[1]
                # TODO: probably restriction should decrease as well for damaged
                if module.hit_points:
                    self.parameters[type] *= value

    def get_parameter(self, parameter_name):
        return self.parameters[parameter_name]

    def get_parameters(self):
        return self.parameters

    def get_modules(self):
        return self.modules






