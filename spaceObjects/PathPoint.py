import pygame

import Constants


class PathPoint(pygame.sprite.Sprite):
    def __init__(self, xy):
        pygame.sprite.Sprite.__init__(self)

        self.x_coordinate = xy[0]
        self.y_coordinate = xy[1]

        self.x_size = self.y_size = 1

        self.rotatable = False
        self.zoom_inited = False

        self.type = Constants.GeneralConstants.POINT

        self.collidable_type = Constants.CollidableTypes.NON_COLLIDABLE

        self.images_names = ["point.png"]
        self.zoom_needed = False

    def set_image(self, resource_manager):
        self.image_default = resource_manager.load_image("point.png")
        self.image = resource_manager.load_image("point.png")
        self.rect = self.image.get_rect()