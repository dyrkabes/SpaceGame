from Entity import Entity
import Constants

class Star(Entity):
    def __init__(self, x_coordinate, y_coordinate, x_size, y_size, type=Constants.GeneralConstants.STAR):
        Entity.__init__(self,x_coordinate, y_coordinate, x_size, y_size, type)

        self.weight = 5000

        self.rotatable = False

        self.collidable_type = Constants.CollidableTypes.COLLIDE_TARGET


        self.init_animation(["star.png", "star_animate.png"], 40)


    def get_mass(self):
        return self.weight

    def act(self):
        self.animation.animate(self)
