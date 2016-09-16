import pygame
import Constants

import Settings

from Animation import Animation

class Entity(pygame.sprite.Sprite):
    def __init__(self, x_coordinate, y_coordinate,
                 x_size, y_size, type):
        pygame.sprite.Sprite.__init__(self)

        # these are the coordinates of the center
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

        self.x_size = x_size
        self.y_size = y_size

        # TODO: move coll manager and obj proc init to the entity
        self.collision_manager_remove = None
        self.object_processor_remove = None

        self.animatable = False

        self.image = None
        # image default is needed because the image spoils after some cycles of zoom/rotation
        self.image_default = None

        self.destroy_observers = []

        # TODO: rework zoom needed for every object
        self.zoom_needed = False

        self.type = type





        # self.z_dimension = Constants.ZDimensions.POINT






    def init_animation(self, images_names, delay_count):
        self.animatable = True
        self.animation = Animation(images_names, delay_count)

    def destroy(self, second_object=None):
        # if was registered in collision manager's lists
        if self.collidable_type != Constants.CollidableTypes.NON_COLLIDABLE:
            self.collision_manager_remove(self)

        # removes from current system and does other stuff if needed
        self.object_processor_remove(self, second_object)

        # if order had this object as a target
        if hasattr(self, "remove_order"):
            self.remove_order(self)

        # TODO: remove order vs destroy observer?
        for destroy_observer in self.destroy_observers:
            destroy_observer(self)

    def animate(self):
        # calls the animation block of entity
        self.animation.animate(self)

    def get_images_names(self):
        # returns images names to load from file system
        if self.animatable:
            return self.animation.images_names
        else:
            return self.images_names[0]



    # def get_default_slice(self, x_offset, x_size):
    #     self.default_slice = (x_offset, 0, x_size, self.y_size)
    #
    # def default_slice_in_grid(self):
    #     return [param * Settings.GRID_SIZE for param in self.default_slice]

    def register_destroy_observer(self, destroy_observer):
        self.destroy_observers.append(destroy_observer.target_destroyed)

