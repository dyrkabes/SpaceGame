from Entity import Entity
import Constants
import math

class PlanetShade(Entity):
    def __init__(self, x_coordinate, y_coordinate, x_size, y_size, planet, type=Constants.GeneralConstants.PLANET_SHADE):
        Entity.__init__(self,x_coordinate, y_coordinate, x_size, y_size, type)

        # self.type = Constants.GeneralConstants.PLANET_SHADE

        self.rotatable = True
        self.angle = 0

        self.collidable_type = Constants.CollidableTypes.NON_COLLIDABLE


        self.init_animation(["planet_shade.png"], 2000)
        self.star = None
        self.planet = planet

    #
    # def get_mass(self):
    #     return self.weight

    def act(self):

        self.animation.animate(self)
        self.move()
        self.rotate()

    def move(self):
        self.x_coordinate = self.planet.x_coordinate
        self.y_coordinate = self.planet.y_coordinate

    def rotate(self):
        self.angle = math.degrees(
            math.atan2(
            self.y_coordinate - self.star.y_coordinate,
            self.x_coordinate - self.star.x_coordinate
            )
        ) - 180

    def init_star(self, star):
        self.star = star
        self.rotate()


