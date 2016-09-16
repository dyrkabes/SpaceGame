from Entity import Entity
import Constants
import math
from spaceObjects.PlanetShade import PlanetShade

class Planet(Entity):
    def __init__(self, x_coordinate, y_coordinate, x_size, y_size, type=Constants.GeneralConstants.PLANET):
        Entity.__init__(self,x_coordinate, y_coordinate, x_size, y_size, type)

        self.type = Constants.GeneralConstants.PLANET

        self.rotatable = False

        self.collidable_type = Constants.CollidableTypes.NON_COLLIDABLE


        self.init_animation(["planet.png"], 2000)
        self.planet_shade = None

        self.init_planet_shade()

        self.movement_speed = 0.2

        self.angle = 0



    #
    # def get_mass(self):
    #     return self.weight

    def act(self):
        self.move()
        self.animation.animate(self)
        self.planet_shade.act()

    def init_planet_shade(self):
        self.planet_shade = PlanetShade(self.x_coordinate,
                                        self.y_coordinate,
                                        self.x_size,
                                        self.y_size,
                                        self)

    def move(self):
        self.angle = math.degrees(
            math.atan2(
            self.y_coordinate - self.star.y_coordinate,
            self.x_coordinate - self.star.x_coordinate
            )
        ) + 90
        delta_x = self.x_coordinate - self.star.x_coordinate
        delta_y = self.y_coordinate - self.star.y_coordinate
        delta_x /= math.fabs(delta_x)
        delta_y /= math.fabs(delta_y)

        print(self.angle, " angle")

        # delt = self.movement_speed * math.sin(math.degrees(self.angle)) #* delta_x
        # print(delt)

        self.x_coordinate += self.movement_speed * math.cos(math.radians(self.angle)) #* delta_x
        self.y_coordinate += self.movement_speed * math.sin(math.radians(self.angle)) #* delta_y

    def init_star(self, star):
        self.star = star
        self.planet_shade.init_star(star)
