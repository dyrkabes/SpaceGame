from Entity import Entity
import Constants

class Comet(Entity):
    def __init__(self, x_coordinate, y_coordinate, x_size, y_size, x_movement_speed, y_movement_speed, weight,
                 type=Constants.GeneralConstants.COMET):
        Entity.__init__(self, x_coordinate, y_coordinate, x_size, y_size, type)

        self.x_movement_speed = x_movement_speed
        self.y_movement_speed = y_movement_speed

        self.rotatable = True

        self.angle_speed = 8
        self.angle = 0

        self.collidable_type = Constants.CollidableTypes.COLLIDABLE

        self.weight = weight

        # self.type = Constants.GeneralConstants.COMET

        self.component_type = Constants.ShipConstants.WEAPON


        self.init_animation(["comet.png", "comet_animate.png", "comet_animate2.png", "comet_animate.png"], 30)

    def move(self):
        self.x_coordinate += self.x_movement_speed
        self.y_coordinate += self.y_movement_speed

    def rotate(self):
        self.angle += self.angle_speed

    def act(self):
        if self.animatable:
            self.animation.animate(self)
        self.move()
        self.rotate()

    def change_movement_speed(self, movement_speed_x, movement_speed_y):
        self.x_movement_speed += movement_speed_x
        self.y_movement_speed += movement_speed_y

    def damage_dealt(self):
        return self.weight






