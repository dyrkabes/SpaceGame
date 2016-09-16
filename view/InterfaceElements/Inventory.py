import pygame
import Constants

from Entity import Entity
from view.InterfaceElements.InfoPlate import InfoPlate

from shipComponents.Component import Component
from shipComponents.ComponentModule import ComponentModule

class Inventory(Entity):
    def __init__(self, x_coordinate=50, y_coordinate=50,
                 type = Constants.GUIConstants.INVENTORY):
        Entity.__init__(self, x_coordinate=200, y_coordinate=200, x_size=400, y_size=400, type=Constants.GUIConstants.INVENTORY)
        self.visible = False
        # self.type = Constants.GUIConstants.INVENTORY
        self.set_image = None
        self.zoom = None

        self.components = []
        self.modules = []
        self.info_plates = []

        self.images_names = ["inventory.png"]


    def switch_visible(self):
        self.visible = not self.visible
        self.components = []
        self.load_ship_components()

    def init_ship(self, ship):
        self.ship = ship

    def init_set_image(self, set_image):
        self.set_image = set_image

    def init_zoom(self, zoom):
        self.zoom = zoom

    def load_ship_components(self):
        for component in self.ship.get_components():
            self.components.append(component)
            self.set_image(component, component.images_names)
            self.zoom(component, False)

    def load_component_modules(self, component):
        self.modules = []
        for module in component.get_modules():
            self.modules.append(module)
            self.set_image(module, module.images_names)


    def draw(self, game_display_blit):
        x_offset = self.x_coordinate
        y_offset = self.y_coordinate
        for component in self.components:
            # ZOOM NEEDED FOR that
            self.zoom(component, False)
            game_display_blit(component.image, (x_offset, y_offset))
            component.init_position(x_offset, y_offset)
            x_offset += 50

        # TODO: MODULES

        for info_plate in self.info_plates:
            if info_plate.visible:
                game_display_blit(info_plate.image, (info_plate.x_coordinate,
                                               info_plate.y_coordinate))

            # y_offset += 25
# TODO: probably not the best idea about HVOER/CLKICK
    def create_info_plate(self, source, option=Constants.GUIConstants.CLICK):
        """
        Creates new InfoPlate or deletes the old one if clicked on the same component
        :param source: is needed to determine if this InfoPlate was clicked
        :return: None. Appends InfoPlate to the inventorie's InfoPlate which will be later drawn
        """
        clicked_on_opened = False
        for info_plate in self.info_plates:
            if option != Constants.GUIConstants.HOVER and info_plate.source == source:
                self.info_plates.remove(info_plate)
                clicked_on_opened = True

        if not clicked_on_opened:
            info_plate = InfoPlate(source.x_coordinate + 15,
                                       source.y_coordinate + 15)
            if Component in source.__class__.__bases__:
                self.load_component_modules(source)
                # self.info_plates = []

                # DOUBLE
                info_plate.create_captions_for_component(source)

                info_plate.create_modules(self.modules)


            else:
                # DOUBLE
                info_plate.create_captions_for_module(source)
                pass

            info_plate.init_source(source)
            self.info_plates.append(info_plate)

    # def erase_module_info_plates(self):




    def erase_info_plates(self, option=None):
        for info_plate in self.info_plates:
            if option:
                if option.__name__ is info_plate.source.__class__.__name__:
                    self.info_plates.remove(info_plate)
            else:
                self.info_plates = []
                return True

    def has_info_plate(self, source):
        for info_plate in self.info_plates:
            if info_plate.source == source:
                return True
        return False
        # self.info_plates = []

    def animate(self):
        for component in self.components:
            if component.animatable:
                component.animate()
            for module in self.modules:
                if module.animatable:
                    module.animate()



