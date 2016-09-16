import pygame

import Settings
import Constants
from view.Camera import Camera


class Drawer:
    camera = Camera()

    def __init__(self):
        pygame.init()
        self.game_display = pygame.display.set_mode((Settings.screen_width, Settings.screen_height))

        self.current_system = None
        self.GUI = None
        # I still think about how to position the ship (giving it to drawer who shouldnt have any game logic
        # seems pretty bad for me. Tho is already has cur_sys and GUI
        self.ship = None
        self.game_manager = None

    def set_current_system(self, current_system):
        self.current_system = current_system
        self.camera.current_system = current_system

    def init_GUI(self, GUI):
        self.GUI = GUI

    def init_game_manager(self, game_manager):
        self.game_manager = game_manager

    def init_ship(self, ship):
        self.ship = ship

    def draw_entities(self):
        # Trello fall so i will write it there
        # TODO: Draw (and rotozoom) nothing except the objects which are close to camera
        z_list = [[] for i in range(12)]
        for entity in self.current_system.entities:
            z_value = Constants.ZDimensions.get_z(entity.type)
            z_list[z_value].append(entity)

        for elements in z_list:
            for entity in elements:
                rect = entity.image.get_height()
                entity.rect = [(entity.x_coordinate - self.camera.x_coordinate - rect/2/Settings.GRID_SIZE)* Settings.GRID_SIZE,
                             (entity.y_coordinate - self.camera.y_coordinate - rect/2/Settings.GRID_SIZE)* Settings.GRID_SIZE]
                self.game_display.blit(entity.image, entity.rect)

    def draw_GUI(self):
        for element in self.GUI.elements:
            if element.type != Constants.GUIConstants.INVENTORY:
                self.game_display.blit(element.image, (element.x_coordinate, element.y_coordinate))
            else:
                self.game_display.blit(element.image, (element.x_coordinate, element.y_coordinate))
                element.draw(self.game_display.blit)


    def null_scene(self):
        self.game_display.fill((0,0,0))

    def zoom_in(self):
        Settings.GRID_SIZE += 1

    def zoom_out(self):
        Settings.GRID_SIZE -= 1
        if Settings.GRID_SIZE < 1:
            Settings.GRID_SIZE = 1




    def update(self):
        pygame.display.update()


    def tile_count_x(self):
        return Settings.screen_width / Settings.GRID_SIZE

    def tile_count_y(self):
        return Settings.screen_height / Settings.GRID_SIZE

    @staticmethod
    def real_world_mouse(mouse_pos):
        " return coordinates of mouse clicked concerning zoom and camera offset"
        return (mouse_pos[0] / Settings.GRID_SIZE + Drawer.camera.x_coordinate,
            mouse_pos[1] / Settings.GRID_SIZE + Drawer.camera.y_coordinate)

    def enviromenatal_state_changed(self):
        if self.game_manager.enviroment_state == Constants.StateConstants.LANDED:
            self.camera.move_to(
                self.ship.x_coordinate - 10,
                self.ship.y_coordinate - 10
            )

    def quit(self):
        pygame.quit()
