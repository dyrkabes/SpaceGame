from Entity import Entity
import Constants

import math

import random

import pygame

from Animation import Animation

import Settings

class Bullet(Entity):
    def __init__(self, x_coordinate, y_coordinate, x_size, y_size, movement_speed_max, x_destination, y_destination, ship_id,
                 damage, bullet_duration, type=Constants.GeneralConstants.BULLET):

        Entity.__init__(self, x_coordinate, y_coordinate, x_size, y_size, type)

        self.rotatable = True

        self.collidable_type = Constants.CollidableTypes.BULLET
        self.type = Constants.GeneralConstants.BULLET
        self.component_type = Constants.ShipConstants.WEAPON

        #TODO : owner
        self.owner = None

        self.x_destination = x_destination
        self.y_destination = y_destination

        self.angle_destination = math.atan2(
            self.y_coordinate - self.y_destination,
            self.x_coordinate - self.x_destination
        )
        self.angle = math.degrees(self.angle_destination)
        self.angle_speed = 0

        self.x_movement_speed = -movement_speed_max * math.cos(self.angle_destination)
        self.y_movement_speed = -movement_speed_max * math.sin(self.angle_destination)

        self.cycles_max = bullet_duration

        # dice = random.randint(0, 100)
        # if bullet_corruption < dice:
        #     self.cycles_max /= 3


        self.cycles = 0

        self.damage = damage

        self.ship_id = ship_id

        self.worn_out = False


        self.image = None
        self.image_default = None


        # self.slice = (15,0, 15,3)

        self.init_animation(["bullet.png", "bullet_blink1.png", "bullet_blink2.png"], 8)




    def move(self):
        self.x_coordinate += self.x_movement_speed
        self.y_coordinate += self.y_movement_speed
        self.cycles += 1

        # if self.cycles >= self.cycles_max - self.cycles_max/2:
        #     self.buff_image = self.image
        #     self.image = pygame.Surface((self.x_size, self.y_size))
        #     self.image.set_alpha(100)
        #     self.image.blit(self.buff_image, (0,0))
        #     # self.buff_image.set_alpha(155)
        #     # self.image = self.buff_image
        #     # self.image.convert_alpha()
        #     # self.image = self.image.convert_alpha()
        #     # self.image.set_alpha(200)

        if self.cycles >= self.cycles_max:
            self.worn_out = True
            self.destroy()

    def rotate(self):
        self.angle += self.angle_speed

    def act(self):
        if self.animatable:
            self.animation.animate(self)
        self.rotate()
        self.move()


    def damage_dealt(self):
        return self.damage


