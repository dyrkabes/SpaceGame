import Constants
import Settings
from view.InterfaceElements.InfoLabel import InfoLabel
from view.InterfaceElements.InfoPlate import InfoPlate
from view.InterfaceElements.Button import Button

from view.InterfaceElements.Inventory import Inventory

from shipComponents.Component import Component
from shipComponents.ComponentModule import ComponentModule

import copy


class GUI:
    def __init__(self):
        self.elements = []
        self.pressed_button = None
        self.resource_manager = None
        self.game_manager = None
        self.ship = None

        self.inventory = None

        self.prev_mouse_pos = None


    def init_resource_manager(self, resource_manager):
        self.resource_manager = resource_manager

    def init_game_manager(self, game_manager):
        self.game_manager = game_manager

    def init_ship(self, ship):
        self.ship = ship

    def add_element(self, element):
        self.elements.append(element)

    def init_drawer(self, drawer):
        self.drawer = drawer

    def check_if_collision(self, mouse_pos, interaction_type):

        for element in self.elements:
            if interaction_type == Constants.GUIConstants.CLICK:
                if element.type == Constants.GUIConstants.BUTTON:
                    if element.x_coordinate < mouse_pos[0] < element.x_coordinate + element.x_size:
                        if element.y_coordinate < mouse_pos[1] < element.y_coordinate + element.y_size:
                            element.state = Constants.GUIConstants.PRESSED
                            element.pressed()
                            self.pressed_button = element
                            return True

                elif element.type == Constants.GUIConstants.INVENTORY:
                    for component in element.components:
                        if component.x_coordinate < mouse_pos[0] < component.x_coordinate + component.x_size:
                            if component.y_coordinate < mouse_pos[1] < component.y_coordinate + component.y_size:
                                # if element.has_info_plate(component):
                                #     element.erase_info_plates()
                                # else:
                                element.create_info_plate(component)
                                return True

            elif interaction_type == Constants.GUIConstants.HOVER:
                if element.type == Constants.GUIConstants.INVENTORY:
                    for info_plate in element.info_plates:
                        for module in info_plate.modules:
                            if module.x_coordinate < mouse_pos[0] < module.x_coordinate + module.x_size:
                                if module.y_coordinate < mouse_pos[1] < module.y_coordinate + module.y_size:
                                    # TODO: write down somewhere that table is created.
                                    # TODO: if pointer moves, destroy info label
                                    # TODO: same for the click-popup sitution

                                    # TODO: probably we should somehow place create_info_plate outside inv, leaving only creating text for table there

                                    # if self.prev_mouse_pos == mouse_pos:
                                    element.create_info_plate(module, Constants.GUIConstants.HOVER)

                                    return True

                # TODO: create info label in the top left corner for every ship and comet



        return False

    def mouse_moved(self, mouse_pos):
        if self.prev_mouse_pos != mouse_pos:
            if self.inventory and self.inventory.visible and self.inventory.info_plates:
                self.inventory.erase_info_plates(option=ComponentModule)

        for element in self.elements:
            if element.type == Constants.GUIConstants.INFO_PLATE:
                self.elements.remove(element)

        self.prev_mouse_pos = mouse_pos

    def release_pressed_button(self):
        self.pressed_button.release()
        self.pressed_button = None

    def is_button_pressed(self):
        return self.pressed_button

    def create_button(self, button, image_name, image_name_pressed, action):
        self.add_element(button)
        self.resource_manager.set_image_for_button(button,
                                                   image_name,
                                                   image_name_pressed
                                                   )
        button.set_action(action)
        # button.set_image(self.resource_manager)
        # # vremennay procedura
        # TODO: behavior from box

        # button.set_action(self.game_manager.switch_running)
        # dinamich dobavlenie elementov
    #
    def create_info_label(self, x_coordinate, y_coordinate, message):
        self.add_element(InfoLabel(x_coordinate,
                                   y_coordinate,
                                   message))

    def create_info_plate(self, x_coordinate, y_coordinate, hovered_object):
        info_plate = InfoPlate(x_coordinate, y_coordinate, 80, 100)
        info_plate.create_captions(hovered_object)

        self.elements.append(info_plate)


    def create_inventory(self):
        self.inventory = Inventory()
        self.resource_manager.set_image(self.inventory, "inventory.png")
        self.inventory.init_ship(self.ship)
        self.inventory.init_set_image(self.resource_manager.set_image)
        self.inventory.init_zoom(self.resource_manager.zoom)

    def switch_inventory(self):
        if self.inventory.visible:
            self.inventory.switch_visible()
            self.inventory.erase_info_plates()
            self.elements.remove(self.inventory)
        else:
            self.inventory.switch_visible()
            self.add_element(self.inventory)

    def animate(self):
        for element in self.elements:
            if element.animatable or element.type == Constants.GUIConstants.INVENTORY:
                element.animate()

    def enviromenatal_state_changed(self):
        if self.game_manager.enviroment_state == Constants.StateConstants.PIT_STOP:
            # trader
            self.create_button(Button(Settings.screen_width-275, Settings.screen_height-100, 25, 25), "inv_button.png", "inv_button_pressed.png",None)
            # take off
            self.create_button(Button(Settings.screen_width-250,
                                      Settings.screen_height-100,
                                      25, 25),
                               "inv_button.png",
                               "inv_button_pressed.png",
                               self.ship.take_off)
            # land
            self.create_button(Button(Settings.screen_width-250,
                                      Settings.screen_height-75,
                                      25, 25),
                               "inv_button.png",
                               "inv_button_pressed.png",
                               self.ship.land)

        if self.game_manager.enviroment_state == Constants.StateConstants.LANDED:
            for i in range(25):
                self.drawer.zoom_in()
                # TODO: set camera
                # TODO: high texture planet?
                # TODO: do not zoom the ship
                # TODO: all other space object dont zoom as well. would be nice looking
                # v zumalku pishem proverku tsteita. ne proshel  - ne zoom
            pass

        if self.game_manager.enviroment_state == Constants.StateConstants.OUTER_SPACE:
            # buff_elements are needed bc after removing the element before the last it finishes the for loop
            buff_elements = copy.copy(self.elements)
            for element in buff_elements:
                if (element.type == Constants.GUIConstants.BUTTON and
                        (element.action == self.ship.take_off or
                         element.action == self.ship.land)):
                    self.elements.remove(element)
                    # TODO: add merchants etc





