import pygame
import os
import math

import Constants
import Settings


class ResourceManager:
    def __init__(self,
                 data_dir = "data",
                 image_dir = "image"):
        self.data_dir = data_dir
        self.image_dir = image_dir

    def load_image(self, image_name):
        # Loads image
        fullname = os.path.join(self.data_dir,
                                os.path.join(self.image_dir, image_name))
        try:
            image = pygame.image.load(fullname)
        except pygame.error:
            raise SystemExit

        else:
            image = image.convert_alpha()
            return image

    def set_image(self, entity, images_names):
        # sets entities image
        if entity.animatable:
            for frame_image_name in entity.animation.images_names:
                entity.animation.images_default.append(self.load_image(frame_image_name))
                entity.image_default = entity.animation.images_default[0]
                entity.image = entity.animation.images_default[0]
        else:
            # Only one image
            entity.image_default = self.load_image(entity.get_images_names())
            entity.image = entity.image_default


    def set_image_for_button(self, entity, image_name, image_name_pressed):
        entity.image_default = self.load_image(image_name)
        entity.image_pressed = self.load_image(image_name_pressed)
        entity.image = entity.image_default

    @staticmethod
    def zoom(entity, real_world_objects=True):
        # real world - describe
        if real_world_objects:
            entity.image = pygame.transform.smoothscale(entity.image_default,
                                              (entity.x_size*Settings.GRID_SIZE, entity.y_size*Settings.GRID_SIZE))
        else:
            entity.image = pygame.transform.smoothscale(entity.image_default,
                                              (entity.x_size, entity.y_size))

    @staticmethod
    def rotate(entity, game_state=None):
        # TODO: All the zoom and state issues move to the zoom function. Otherwise non rotetable are not affected!
        # Dont like the code repeating some much. Needs some thinking over it
        if game_state != Constants.StateConstants.LANDED:
            if entity.type == Constants.GeneralConstants.PLANET_SHADE:
                entity.image = pygame.transform.scale(entity.image_default,
                                                  (entity.x_size*Settings.GRID_SIZE, entity.y_size*Settings.GRID_SIZE))
            else:
                ResourceManager.zoom(entity)
        elif game_state == Constants.StateConstants.LANDED:
            # from constants loading the list of zoomable during landed state
            grid_size = Constants.ZoomsInLandedState.get_zoom_value(entity.type)
            print(grid_size)
            grid_size = grid_size[1]
            if grid_size:
                entity.image = pygame.transform.smoothscale(entity.image_default,
                                                  (entity.x_size*grid_size, entity.y_size*grid_size))
            else:
                if entity.type != Constants.GeneralConstants.PLANET_SHADE:
                    ResourceManager.zoom(entity)
                else:
                    entity.image = pygame.transform.scale(entity.image_default,
                                                  (entity.x_size*Settings.GRID_SIZE, entity.y_size*Settings.GRID_SIZE))
            # zooming zoomable. Non zoomable zoom to default value of 5


        entity.image = pygame.transform.rotate(entity.image, -entity.angle)
