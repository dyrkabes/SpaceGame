import random

import pygame

import Constants
import Settings
from Controller import Controller
from CurrentSystem import CurrentSystem
from managers.CollisionManager import CollisionManager
from managers.CometCreator import CometCreator
from managers.GameManager import GameManager
from managers.ObjectProcessor import ObjectProcessor
from managers.ResourceManager import ResourceManager
from spaceObjects.Ship import Ship
from spaceObjects.Star import Star
from spaceObjects.Planet import Planet
from view.Drawer import Drawer
from view.GUI import GUI
from view.InterfaceElements.Button import Button

# THAT IS A TEST FILE

# INITIALIZATION
drawer = Drawer()
controller = Controller()
GUI = GUI()

object_processor = ObjectProcessor()
current_system = CurrentSystem()
resource_manager = ResourceManager()
game_manager = GameManager()
collision_manager = CollisionManager()

GUI.init_resource_manager(resource_manager)
GUI.init_game_manager(game_manager)


drawer.set_current_system(current_system)
drawer.init_GUI(GUI)
drawer.init_game_manager(game_manager)

controller.init_drawer_and_rec_manager(drawer, resource_manager)
controller.init_current_system(current_system)
controller.init_object_processor(object_processor)
controller.init_GUI(GUI)


object_processor.init_current_system(current_system)
object_processor.init_resource_manager(resource_manager, ResourceManager.zoom)
object_processor.init_collision_manager(collision_manager)

collision_manager.init_object_processor(object_processor)



# INITIALIZATION OVER

GUI.create_inventory()
GUI.create_button(Button(Settings.screen_width/2-75,Settings.screen_height-100, 150, 100), "button.png", "button_pressed.png", game_manager.switch_running)
GUI.create_button(Button(Settings.screen_width-100,Settings.screen_height-100, 100, 100), "exit_button.png", "exit_button_pressed.png", controller.quit)
GUI.create_button(Button(Settings.screen_width-300,Settings.screen_height-100, 25, 25), "inv_button.png", "inv_button_pressed.png", GUI.switch_inventory)
GUI.init_drawer(drawer)


game_manager.register_enviroment_state_observer(GUI.enviromenatal_state_changed)
game_manager.register_enviroment_state_observer(drawer.enviromenatal_state_changed)

current_system.init_game_manager(game_manager)


ship = Ship(50,50, 6, 6,
            object_processor)
object_processor.create_entity(ship)
controller.init_ship(ship)
GUI.init_ship(ship)
GUI.inventory.init_ship(ship)
drawer.init_ship(ship)


ship.init_game_manager(game_manager)

ship1 = Ship(150,90, 6, 6,
            object_processor)
object_processor.create_entity(ship1)


ship2 = Ship(10,100, 6, 6,
            object_processor)
object_processor.create_entity(ship2)

# object_processor.create_entity(OuterSpaceObject(60,60.2,3,3, 44))
# object_processor.create_entity(OuterSpaceObject(60,66.3,3,3, 44))
# object_processor.create_entity(OuterSpaceObject(60,66.3,3,3, 44))
# object_processor.create_entity(OuterSpaceObject(59,50.6,3,3, 44))

# object_processor.create_comet(Comet(44, 28, 3, 3))
# object_processor.create_comet(Comet(58, 38, 5, 5))
# object_processor.create_comet(Comet(70, 10, 5, 5))
# object_processor.create_comet(Comet(110, 10, 5, 5))
# object_processor.create_comet(Comet(110, 110, 5, 5))
# object_processor.create_comet(Comet(150, 32, 5, 5))
# object_processor.create_comet(Comet(0, 0, 2, 2))
# object_processor.create_comet(Comet(40, 34, 5, 5))


object_processor.create_entity(Star(current_system.x_dimension/2, current_system.y_dimension/2, 50, 50))

planet = Planet(52, 52, 28, 28)
planet.init_star(current_system.star)
object_processor.create_entity(planet)
object_processor.create_entity(planet.planet_shade)

# later this one up and cur sys throws when to check entity
collision_manager.init_current_system(current_system)


clock = pygame.time.Clock()

game_exit = False

while not controller.game_exit:
    drawer.null_scene()

    # v otdel'nyi fail


    for event in pygame.event.get():
        controller.process_event(event)
    controller.count_still_mouse_ticks(pygame.mouse.get_pos())

    GUI.animate()

    if game_manager.get_state() == Constants.StateConstants.RUNNING:
        current_system.act()

        collision_manager.check_collided()
        game_manager.increase_cycles_past()

        # TODO: remove is somewhere else
        if random.randint(0, 1000) > 950:
            CometCreator.create_comet(current_system, object_processor.create_entity)
    else:
        current_system.get_urgent_messages()
        current_system.zoom_and_rotate()





    drawer.draw_entities()
    drawer.draw_GUI()

    drawer.update()

    clock.tick(Settings.FPS)



drawer.quit()

