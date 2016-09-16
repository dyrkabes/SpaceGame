import Settings
import Constants
import pygame

from Path import Path
from managers.ClickManager import ClickManager

from view.Drawer import Drawer

class Controller:
    def __init__(self):
        pass

    def init_drawer_and_rec_manager(self, drawer, resource_manager):
        self.drawer = drawer
        self.resource_manager = resource_manager
        self.game_exit = False
        self.mouse_down = False

        self.still_mouse_ticks = 0
        self.mouse_pos = None

    def init_current_system(self, current_system):
        # Would be nice to remove current system somewhere else
        self.current_system = current_system

    def init_ship(self, ship):
        self.ship = ship
        ship.player_ship = True

    def init_object_processor(self, object_processor):
        self.object_processor = object_processor

    def init_GUI(self, GUI):
        self.GUI = GUI


    def process_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                self.quit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if not self.GUI.check_if_collision(event.pos, Constants.GUIConstants.CLICK):
                    clicked_object = ClickManager.instance_clicked(Drawer.real_world_mouse(event.pos), self.current_system)

                    if clicked_object:
                        # TODO: move the logic away
                        if clicked_object.type == Constants.GeneralConstants.SHIP and clicked_object.player_ship:
                            self.GUI.switch_inventory()
                            # print("CLICKED")
                        elif (clicked_object.type == Constants.GeneralConstants.SHIP
                                or clicked_object.type == Constants.GeneralConstants.COMET
                                or clicked_object.type == Constants.GeneralConstants.OUTER_SPACE_OBJECT
                              or clicked_object.type == Constants.GeneralConstants.PLANET):
                            self.ship.create_order(clicked_object)
                    else:



                        self.object_processor.erase_path()
                        print(event.pos)
                        x_clicked = event.pos[0] / Settings.GRID_SIZE + self.drawer.camera.x_coordinate
                        y_clicked = event.pos[1] / Settings.GRID_SIZE + self.drawer.camera.y_coordinate
                        self.ship.set_destination((x_clicked, y_clicked))


                        path = Path(self.ship)
                        path.cycle()


                        self.object_processor.create_path(path)

                else:
                    print("GUI catched")



            if event.button == 3:
                self.mouse_down = True

            elif event.button == 4:
                tiles_were_x = self.drawer.tile_count_x()
                tiles_were_y = self.drawer.tile_count_y()
                self.drawer.zoom_in()
                tiles_are_x = self.drawer.tile_count_x()
                tiles_are_y = self.drawer.tile_count_y()
                mouse_x, mouse_y = pygame.mouse.get_pos()
                self.drawer.camera.move((tiles_were_x - tiles_are_x) * ( 1 - (Settings.screen_width - mouse_x)/Settings.screen_width),
                                   (tiles_were_y - tiles_are_y) * ( 1 - (Settings.screen_height - mouse_y)/Settings.screen_height))
                for entity in self.current_system.entities:
                    self.resource_manager.zoom(entity)

            elif event.button == 5:
                tiles_were_x = self.drawer.tile_count_x()
                tiles_were_y = self.drawer.tile_count_y()
                self.drawer.zoom_out()
                tiles_are_x = self.drawer.tile_count_x()
                tiles_are_y = self.drawer.tile_count_y()
                mouse_x, mouse_y = pygame.mouse.get_pos()
                self.drawer.camera.move((tiles_were_x - tiles_are_x) * ( 1 - (Settings.screen_width - mouse_x)/Settings.screen_width),
                                   (tiles_were_y - tiles_are_y) * ( 1 - (Settings.screen_height - mouse_y)/Settings.screen_height))
                for entity in self.current_system.entities:
                    self.resource_manager.zoom(entity)

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if self.GUI.is_button_pressed():
                    self.GUI.release_pressed_button()
            if event.button == 3:
                self.mouse_down = False



        if self.mouse_down and event.type == pygame.MOUSEMOTION:
            self.drawer.camera.move(-event.rel[0]/Settings.GRID_SIZE, -event.rel[1]/Settings.GRID_SIZE)


        if event.type == pygame.MOUSEMOTION:
            self.GUI.mouse_moved(event.pos)


    def count_still_mouse_ticks(self, mouse_pos):
        if mouse_pos == self.mouse_pos:
            self.still_mouse_ticks += 1
            if self.still_mouse_ticks > 20:
                # TODO: why GUI checks obj collisisons with mouse?
                if not self.GUI.check_if_collision(mouse_pos, Constants.GUIConstants.HOVER):
                    hovered_object = ClickManager.instance_clicked(Drawer.real_world_mouse(mouse_pos), self.current_system)
                    if hovered_object:

                        if (hovered_object.type == Constants.GeneralConstants.SHIP
                                or hovered_object.type == Constants.GeneralConstants.COMET):
                            self.GUI.create_info_plate(50,40, hovered_object)


        else:
            self.still_mouse_ticks = 0
            self.mouse_pos = mouse_pos


    # TODO: prevent from moving, ordering etc
    def enviroment_state_changed(self):
        pass




    def quit(self):
        self.game_exit = True