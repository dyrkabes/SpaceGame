import pygame

import Constants
from managers.GravityManager import GravityManager
from managers.ResourceManager import ResourceManager
from analyzers.OrderAnalyzer import OrderAnalyzer

class CurrentSystem:
    def __init__(self):

        #TODO: Reading from database file
        self.world_size = 50
        self.star = None
        self.x_dimension = 233
        self.y_dimension = 233
        self.entities = pygame.sprite.Group()

    def append_entity(self, entity):
         self.entities.add(entity)

    def remove_entity(self, entity):
        self.entities.remove(entity)

    def get_entities(self):
        return self.entities

    def act(self):
        for entity in self.entities:
            if entity.zoom_needed:
                ResourceManager.zoom(entity)
            if entity.rotatable:
                ResourceManager.rotate(entity)



            # Lishnee
            # if entity.type == Constants.GeneralConstants.POINT:
            #     if not entity.zoom_inited:
            #         ResourceManager.zoom(entity)
            #         entity.zoom_inited = True

            if (entity.type == Constants.GeneralConstants.SHIP
                    or entity.type == Constants.GeneralConstants.COMET
                    or entity.type == Constants.GeneralConstants.BULLET
                    or entity.type == Constants.GeneralConstants.TEXT
                    or entity.type == Constants.GeneralConstants.STAR
                    or entity.type == Constants.GeneralConstants.AIM_MARKER
                  or entity.type == Constants.GeneralConstants.EXPLOSION):
                if entity.type == Constants.GeneralConstants.COMET:
                    GravityManager.apply_gravity_effects(entity, self.star)
                if entity.type == Constants.GeneralConstants.SHIP:
                    OrderAnalyzer.select_target(entity, self)
                entity.act()

    def get_urgent_messages(self):
        for entity in self.entities:
            if entity.type == Constants.GeneralConstants.SHIP:
                if entity.state_manager.urgents:
                    entity.check_messages(urgent=True)





    def zoom_and_rotate(self):
        for entity in self.entities:
            if entity.rotatable:
                ResourceManager.rotate(entity)