import math

import copy

import Constants
from Entity import Entity
from shipComponents.Engine import Engine
from shipComponents.Shell import Shell
from shipComponents.Grabber import Grabber
from shipComponents.Bilge import Bilge
from shipComponents.Weapon import Weapon

from Order import Order

from managers.BilgeManager import BilgeManager
# from managers.MessageManager import MessageManager
from managers.StateManager import StateManager

from analyzers.MovementAnalyzer import MovementAnalyzer

from view.AimMarker import AimMarker

from Animation import Animation

from managers.OrderHelper import OrderHelper



class Ship(Entity):
    # TODO: Needs lots of refactor. Probably some helper classes
    id = 0
    def __init__(self, x_coordinate, y_coordinate, x_size, y_size, object_processor):
        Entity.__init__(self, x_coordinate, y_coordinate, x_size, y_size)

        self.x_movement_speed = 0
        self.y_movement_speed = 0

        self.x_destination = self.x_coordinate
        self.y_destination = self.y_coordinate

        self.components = []

        self.angle = 0
        self.angle_destination = 0
        self.angle_speed_max = 0

        self.rotatable = True
        # Because ship rotates on arc it needs correction of angle destination
        self.rotation_check = 0

        # It's for the pseudo_ship, path calculation
        self.path_found = None

        self.ship_id = copy.copy(Ship.id)
        self.type = Constants.GeneralConstants.SHIP
        self.player_ship = False
        self.collidable_type = Constants.CollidableTypes.COLLIDE_TARGET

        # Default interaction type on mouse click
        self.component_type = Constants.ShipConstants.WEAPON

        self.state_manager = StateManager()

        # Hardcoded for now
        self.add_component(Engine(self))
        self.add_component(Shell(self))
        self.add_component(Grabber(self))
        self.add_component(Bilge(self))
        self.add_component(Bilge(self))
        self.add_component(Weapon(self, object_processor.create_entity))

        self.engine_state_changed()

        self.orders = []

        # object related functions
        self.object_processor_del_entity = object_processor.destroy_entity
        self.object_processor_create_entity = object_processor.create_entity
        self.object_processor_create_info_label = object_processor.create_info_label

        self.aim_markers = []

        self.init_animation(["ship.png", "ship_swinging1.png", "ship_swinging2.png", "ship_swinging1.png", "ship.png"], 13)


    def set_image(self, resource_manager):
        self.image_default = resource_manager.load_image("ship.png")
        self.image = resource_manager.load_image("ship.png")
        self.rect = self.image.get_rect()

    def add_component(self, component):
        self.components.append(component)
        component.create_info_label = self.create_info_label

    def get_components(self):
        return self.components

    def get_component(self, component_type):
        for component in self.components:
            if component.type == component_type:
                return component
        return None

    def get_coordinates(self):
        return (self.x_coordinate, self.y_coordinate)

    def engine_state_changed(self):
        self.movement_speed_max = self.get_component(Constants.ShipConstants.ENGINE).get_movement_speed()
        self.angle_speed_max = self.get_component(Constants.ShipConstants.ENGINE).get_rotation_speed()

    def move(self):
        self.set_movement_speed()
        self.x_coordinate += self.x_movement_speed
        self.y_coordinate += self.y_movement_speed

    def rotate(self):
        self.rotation_check += 1

        delta = math.floor(self.angle_destination) - math.floor(self.angle)
        if delta:
            if math.fabs(delta) < self.angle_speed_max:
                self.angle_speed = delta
            else:
                if delta < 0:
                    self.angle_speed = -self.angle_speed_max
                else:
                    self.angle_speed = self.angle_speed_max
        else:
            self.angle_speed = 0
            self.set_destination((self.x_destination, self.y_destination))
        self.angle += self.angle_speed

    def act(self):
        MovementAnalyzer.get_destination(self)
        if self.animatable:
            self.animation.animate(self)
        self.rotate()
        self.move()
        self.check_orders_aviability()
        self.check_messages()

    def calculate_movement_cycles(self):
        self.movement_cycles = math.hypot((self.x_coordinate-self.x_destination),
                                          (self.y_coordinate-self.y_destination)) / self.get_distance_per_turn()

    def set_movement_speed(self):
        #unylo
        if self.x_destination and self.y_destination:
            if math.hypot(self.x_coordinate - self.x_destination,
                    self.y_coordinate  - self.y_destination) < self.movement_speed_max * 5:
                self.x_movement_speed = 0
                self.y_movement_speed = 0
                self.x_destination = 0
                self.y_destination = 0
                if self.path_found:
                    self.path_found()
            else:
                # TODO: Star workaround
                self.x_movement_speed = self.movement_speed_max * math.sin(math.radians(self.angle))
                self.y_movement_speed = - self.movement_speed_max * math.cos(math.radians(self.angle))

    def set_destination(self, destination):
        self.x_destination, self.y_destination = destination
        self.get_angle_destination()

    def get_distance_per_turn(self):
        return self.get_component(Constants.ShipConstants.ENGINE).get_movement_speed()

    def get_angle_destination(self):
        self.angle_destination = math.degrees(
            math.atan2(
                (self.y_destination - self.y_coordinate),
                (self.x_destination - self.x_coordinate)
            )
        ) + 90

        delta = math.floor(self.angle_destination) - math.floor(self.angle)
        if delta > 180:
            self.angle += 360
        elif delta < -180:
            self.angle -= 360


    def add_path_observer(self, path_found):
        self.path_found = path_found

    def create_order(self, target):
        if not OrderHelper.is_order(self, target):
            # if ship had no such order
            OrderHelper.process_order(self, target)


    def remove_order(self, order):
        # Try except bc: a ship had an order and got destroyed. The order target still has remove_order
        # And when it is destroyed it tries to remove it's order from the players's ship (which is not destroed properly for now
        # So, we need todo: 1) remove player ship properly
        # TODO: 2) remove opponents orders properly
        try:
            self.orders.remove(order)
        except ValueError:
            print("Error concerning remove_order occured.")

    def remove_order_by_target(self, target):
        for order in self.orders:
            if order.target == target:
                self.orders.remove(order)
                break

    def check_orders_aviability(self):
        for order in self.orders:
            # get component that perfoms order
            order_perfomer = self.get_component(order.component_type)
            distance = math.hypot((order.target.x_coordinate - self.x_coordinate),
                (order.target.y_coordinate - self.y_coordinate))

            if order_perfomer.type == Constants.ShipConstants.GRABBER:
                if distance <= order_perfomer.get_distance():
                    if distance >= self.x_size/2:
                        order_perfomer.interact(order.target)
                    else:
                        # TODO: remove removing from here :D
                        BilgeManager.select_bilge(self, order.target)
                        # esli bilgi zapolneny - to otmenyat' order. inache prityagivaet i unichtojaet prosto
                        order.target.destroy(self)
                        # self.orders.remove(order)
                        BilgeManager.analyze_rest_orders(self)


            elif order_perfomer.type == Constants.ShipConstants.WEAPON:
                if distance <= order_perfomer.get_distance():
                    order_perfomer.interact(order.target)

    def create_info_label(self, message):
        self.object_processor_create_info_label(
            self,
            message,
            self.state_manager.message_manager.decrease_messages_count
        )

    def check_messages(self, urgent=False):
        if len(self.state_manager.messages):
            message = self.state_manager.pop_message(urgent)
            self.create_info_label(message)
            for component in self.components:
                if component.type == message:
                    component.load_modules()
                if component.type == Constants.ShipConstants.ENGINE:
                    self.engine_state_changed()
                if message == "Destroyed":
                    self.destroy()
                    message = None


#                     I nado j sebe ih opyat' read? how ms from engine?

    def target_destroyed(self, target):
        for order in self.orders:
            if order.target == target:
                self.orders.remove(order)





    # TODO: Ship beaten sprite. Rework default sprites

