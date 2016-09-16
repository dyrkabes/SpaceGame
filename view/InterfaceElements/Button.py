import pygame
import Constants

from Entity import Entity

class Button(Entity):
    def __init__(self, x_coordinate, y_coordinate, x_size, y_size, type=Constants.GUIConstants.BUTTON):
        Entity.__init__(self, x_coordinate, y_coordinate, x_size, y_size, type)

        # For type like go, etc
        self.button_type = None

        self.state = Constants.GUIConstants.DEFAULT

        # self.type = Constants.GUIConstants.BUTTON

        self.action = None

    def set_image(self, resource_manager):
        # Will make different loads for different buttons.. somehow. And different types
        # TODO: One file for one button
        self.image_default = resource_manager.load_image("button.png")
        self.image_pressed = resource_manager.load_image("button_pressed.png")
        self.image = self.image_default
        self.rect = self.image.get_rect()

    def pressed(self):
        self.state = Constants.GUIConstants.PRESSED
        self.image = self.image_pressed


    def release(self):
        self.state = Constants.GUIConstants.DEFAULT
        self.image = self.image_default
        self.action()


# bad bad name
    def set_action(self, action):
        self.action = action