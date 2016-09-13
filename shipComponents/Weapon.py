import math

import Constants
from Constants import ShipConstants
from shipComponents.Component import Component
from shipComponents.ComponentModule import ComponentModule
from spaceObjects.Bullet import Bullet


class Weapon(Component):
    count = 0


    def __init__(self, ship, create_bullet):
        # TODO: Im not sure it works at all
        Component.__init__(self, ShipConstants.WEAPON, ship)

        # for semiauto
        self.default_reload = 40
        self.shot_delay = 0
        self.shots_fired = 0
        self.shotgun_offsets = []


        self.bullets = []


        self.hitpoints = 1
        self.create_bullet = create_bullet
        self.get_ship_coordinates = ship.get_coordinates

        self.cycles_past = 0
        self.count = Weapon.count
        Weapon.count += 1
        self.ship_id = ship.ship_id


        module = ComponentModule(
            self.type
        )
        module.add_module_type_and_value(Constants.ModuleTypes.BULLET_DAMAGE, 22)
        self.add_module(module)


        module = ComponentModule(
            self.type
        )
        module.add_module_type_and_value(Constants.ModuleTypes.BULLET_DURATION,
            155)
        self.add_module(module)


        module = ComponentModule(
            self.type,

        )
        module.add_module_type_and_value(Constants.ModuleTypes.BULLET_SPEED,
            2)
        self.add_module(module)

        module = ComponentModule(
            self.type,
        )
        module.add_module_type_and_value(Constants.ModuleTypes.WEAPON_AIM_REANGE,
            188)
        self.add_module(module)


        module = ComponentModule(
            self.type,
        )
        module.add_module_type_and_value(Constants.ModuleTypes.WEAPON_RELOAD,
            1)
        self.add_module(module)



        # module = ComponentModule(
        #     self.type
        # )
        # module.add_module_type_and_value(Constants.ModuleTypes.BULLET_SPEED, 6)
        # module.add_module_restriction(Constants.ModuleTypes.WEAPON_RELOAD, 0.2)
        # self.add_module(module)

        module = ComponentModule(
            self.type
        )
        module.add_module_type_and_value(Constants.ModuleTypes.AMOUNT_OF_SHOTS, 4)
        module.add_module_restriction(Constants.ModuleTypes.WEAPON_RELOAD, 1)
        self.add_module(module)


        module = ComponentModule(
            self.type
        )
        module.add_module_type_and_value(Constants.ModuleTypes.SHOTGUN, 2)
        module.add_module_restriction(Constants.ModuleTypes.BULLET_DAMAGE, 0.3)
        # module.add_module_restriction(Constants.ModuleTypes.BULLET_CORRUPTION, 90)
        self.add_module(module)





        self.load_modules()

        self.init_animation(["weapon.png", "weapon_fire.png"], 60)

    def get_movement_speed(self):
        return self.movement_speed

    def load_modules(self):
        Component.load_modules(self)
        self.calc_shotgun_offset()

# TODO : Fix obv
    def calc_shotgun_offset(self):
        if self.get_parameter(Constants.ModuleTypes.SHOTGUN) % 2 == 0:
            start = - self.get_parameter(Constants.ModuleTypes.SHOTGUN) / 2 * Constants.ShipConstants.SHOTGUN_SPREAD + Constants.ShipConstants.SHOTGUN_SPREAD
        else:
            start = - self.get_parameter(Constants.ModuleTypes.SHOTGUN) / 2 * Constants.ShipConstants.SHOTGUN_SPREAD
        offset = 0
        for i in range(math.ceil(self.get_parameter(Constants.ModuleTypes.SHOTGUN))):
            self.shotgun_offsets.append(start + offset)
            offset += Constants.ShipConstants.SHOTGUN_SPREAD
        print(self.shotgun_offsets)

    def get_distance(self):
        return self.get_parameter(Constants.ModuleTypes.WEAPON_AIM_REANGE)

    def interact(self, target):
        self.cycles_past += 1
        if self.cycles_past >= self.default_reload / self.get_parameter("reload"):
            if self.shots_fired < self.get_parameter(Constants.ModuleTypes.AMOUNT_OF_SHOTS):
                if self.shot_delay:
                    self.shot_delay -= 1
                else:
                    for shot in range(math.ceil(self.get_parameter("shotgun"))):
                        self.create_bullet(Bullet(self.get_ship_coordinates()[0],
                                              self.get_ship_coordinates()[1],
                                              3,
                                              1,
                                              self.get_parameter("bullet_speed"),
                                              target.x_coordinate+self.shotgun_offsets[shot],
                                              target.y_coordinate,
                                              self.ship_id,
                                              self.get_parameter(Constants.ModuleTypes.BULLET_DAMAGE),
                                              self.get_parameter(Constants.ModuleTypes.BULLET_DURATION),
                                              # self.get_parameter(Constants.ModuleTypes.BULLET_CORRUPTION)
                        ))
                    self.shot_delay = Constants.ShipConstants.SHOT_DELAY
                    self.shots_fired += 1
            else:
                self.cycles_past = 0
                self.shot_delay = 0
                self.shots_fired = 0