from Entity import Entity
import Constants

class Explosion(Entity):
    def __init__(self, x_coordinate, y_coordinate, type=Constants.GeneralConstants.EXPLOSION):
        Entity.__init__(self, x_coordinate, y_coordinate, 2, 2, type)

        self.break_delay = 3
        self.current_delay = 0
        self.collidable_type = Constants.CollidableTypes.NON_COLLIDABLE
        # self.type = Constants.GeneralConstants.EXPLOSION

        self.rotatable = False
        # del?
        self.angle = 0

        self.sizes = [4, 3, 1, 0]



        self.images_names = ["explosion.png"]


    def act(self):
        self.resize()


    def resize(self):
        self.current_delay += 1
        if self.current_delay > self.break_delay:
            self.x_size = self.sizes.pop()
            self.y_size = self.x_size
            self.current_delay = 0
            self.zoom_needed = True
        else:
            self.zoom_needed = False
        if len(self.sizes) <= 0:
            self.destroy()