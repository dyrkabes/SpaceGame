import pygame
import Constants

from Entity import Entity

class InfoPlate(Entity):
    def __init__(self, x_coordinate, y_coordinate, x_size=225, y_size=250, type=Constants.GUIConstants.INFO_PLATE):
        Entity.__init__(self, x_coordinate, y_coordinate, x_size, y_size, type)

        # self.type = Constants.GUIConstants.INFO_PLATE
        self.visible = True

        self.image = pygame.Surface((x_size, y_size))
        self.image.fill((233,233,233))
        self.image.set_alpha(200)
        # self.image.set_colorkey((0,0,0))

        self.font = pygame.font.Font(None, 26)

        self.x_offset = 5

        self.y_offset = 5
        self.y_offset_step = 20

        self.modules = []


    def init_source(self, source):
        self.source = source


    def switch_visible(self):
        self.visible = not self.visible

    def add_caption(self, text, pos):
        text = self.font.render(text, False, (255,33,5))
        self.image.blit(text, pos)

    def create_captions_for_component(self, component):
        self.add_caption(component.type, (self.x_offset, self.y_offset))
        self.y_offset += self.y_offset_step
        for name, value in component.get_parameters().items():
            text = str(name) + ' : ' + str(value)
            self.add_caption(text, (self.x_offset, self.y_offset))
            self.y_offset += self.y_offset_step

    def create_modules(self, modules):
        self.modules = modules
        for module in modules:
            self.image.blit(module.image, (self.x_offset, self.y_offset))
            module.init_absolute_pos((self.x_coordinate + self.x_offset,
                                      self.y_coordinate + self.y_offset))
            self.x_offset += 25


    #TODO: NEEDS REFACTORING
    def create_captions_for_module(self, module):
        text = "hp: " + str(module.hit_points)
        self.add_caption(text, (self.x_offset, self.y_offset))

        for type_and_value in module.get_types_and_values():
            self.y_offset += self.y_offset_step
            text = str(type_and_value[0]) + " : " + str(type_and_value[1])
            self.add_caption(text, (self.x_offset, self.y_offset))

        text = "==================="
        self.y_offset += self.y_offset_step
        self.add_caption(text, (self.x_offset, self.y_offset))

        for restriction_type_and_value in module.get_restrictions_types_and_values():
            self.y_offset += self.y_offset_step
            text = str(restriction_type_and_value[0]) + " : " + str(restriction_type_and_value[1])
            self.add_caption(text, (self.x_offset, self.y_offset))

    def create_captions_for_ship(self, ship):
        text = "hp: " + str(ship.get_component(Constants.ShipConstants.SHELL).get_hitpoints())
        self.add_caption(text, (5,5))

    def create_captions(self, entity):
        if entity.type == Constants.GeneralConstants.SHIP:
            self.create_captions_for_ship(entity)
