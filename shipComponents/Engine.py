from Constants import ShipConstants
from shipComponents.Component import Component

from shipComponents.ComponentModule import ComponentModule

import Constants


class Engine(Component):
    def __init__(self, ship):
        Component.__init__(self, ShipConstants.ENGINE, ship)
        self.name = ShipConstants.ENGINE
        self.hitpoints = 1

        self.engine_state_changed = ship.engine_state_changed

        module = ComponentModule(
                self.type,
        )
        module.add_module_type_and_value(Constants.ModuleTypes.ENGINE_SPEED,
                0.6)
        self.add_module(module)

        module = ComponentModule(
                self.type,
        )
        module.add_module_type_and_value(Constants.ModuleTypes.ENGINE_ROTATION_SPEED,
                8)
        self.add_module(module)

        self.load_modules()

        self.init_animation(["engine.png", "engine_blink.png", "engine_blink1.png"], 40)





    def get_movement_speed(self):
        return self.get_parameter(Constants.ModuleTypes.ENGINE_SPEED)

    def get_rotation_speed(self):
        return self.get_parameter(Constants.ModuleTypes.ENGINE_ROTATION_SPEED)

    # def load_modules(self):
    #     for module in self.modules:
    #         for type_and_value in module.get_types_and_values():
    #             type, value = type_and_value[0], type_and_value[1]
    #             if type == Constants.ModuleTypes.ENGINE_SPEED:
    #                 self.movement_speed = value
    #                 if module.damaged:
    #                     self.movement_speed /= 2
    #             if type == Constants.ModuleTypes.ENGINE_ROTATION_SPEED:
    #                     self.rotation_speed = value
    #                     if module.damaged:
    #                         self.rotation_speed /= 2

    #
    # def get_damage(self, damage):
    #     self.hitpoints -= damage
    #     if self.hitpoints <= 0:
    #         self.movement_speed = self.movement_speed_max / 50
    #         self.engine_state_changed()
    #     print("MESSAGE: engine")
