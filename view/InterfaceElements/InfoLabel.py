import pygame
import Constants

from Entity import Entity

class InfoLabel(Entity):
    def __init__(self, x_coordinate, y_coordinate, decrease_message_count, type=Constants.GeneralConstants.TEXT):
        Entity.__init__(self, x_coordinate-3, y_coordinate-3, 10, 10, type)
        self.font = pygame.font.Font(None, 22)
        self.images_names = ["text.png"]
        self.collidable_type = Constants.CollidableTypes.NON_COLLIDABLE
        # self.type = Constants.GeneralConstants.TEXT
        self.rotatable = False
        self.cycles = 0


        self.decrease_message_count = decrease_message_count

    def set_text(self, message):
        self.image.blit(self.font.render(message, True, (255,105,105)), (0,0))
        self.image_default = self.image

    def act(self):
        self.cycles += 1
        if self.cycles > 66:
            self.destroy()

    def destroy(self, second_object=None):
        Entity.destroy(self, second_object)
        self.decrease_message_count()


