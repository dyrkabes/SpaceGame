import Constants
from managers.DamageProcessor import DamageProcessor

import math

class CollisionManager:
    def __init__(self):
        # for comets etc - stuff which could collide
        self.collidables = []
        # # stuff which could collide with collidables
        # self.collide_targets = []
        # # collides with everything
        # self.bullets = []
        pass

    def init_current_system(self, current_system):
        self.current_system = current_system
        # self.create_collidable_lists()

    def init_object_processor(self, object_processor):
        self.object_processor = object_processor

    def init_GUI(self, GUI):
        self.GUI = GUI

    def create_collidable_lists(self):
        for entity in self.current_system.entities:
            self.process_entity(entity)



    #  hook the system for new object creation
    def process_entity(self, entity):
        self.collidables.append(entity)

        # if entity.collidable_type == Constants.CollidableTypes.COLLIDABLE:
        #     self.collidables.append(entity)
        # elif entity.collidable_type == Constants.CollidableTypes.COLLIDE_TARGET:
        #     self.collide_targets.append(entity)
        # elif entity.collidable_type == Constants.CollidableTypes.BULLET:
        #     self.bullets.append(entity)
    def remove_entity(self, entity):
        print(entity.type)
        if entity.type == Constants.GeneralConstants.SHIP:
            print("s")
        try:
            self.collidables.remove(entity)
        except ValueError:
            print("Value error catched")


    def check_collided(self):
        num = 0
        for collidable in self.collidables:
            num += 1
            for collidable_pair in self.collidables[num:]:
                if (collidable.type != Constants.GeneralConstants.BULLET
                        or collidable_pair.type != Constants.GeneralConstants.BULLET):
                    if (
                        math.hypot((collidable.x_coordinate - collidable_pair.x_coordinate),
                                   (collidable.y_coordinate - collidable_pair.y_coordinate))
                                   <= (collidable.x_size + collidable_pair.x_size)/2
                    ):
                        DamageProcessor.process_collision(collidable, collidable_pair, self.object_processor.create_info_label)

                        # object_to_destroy, obstacle  = DamageProcessor.process_collision(target=collidable, damage_inflicter=collidable_pair)
                        # if object_to_destroy:
                        #     self.object_processor.destroy_entity(object_to_destroy, collide_target=obstacle)
                        #     # # TODO: If crushes some times probably we wil ljust need a try except for a situation when 2 collisions in 1 cycle
                            #
                            # self.collidables.remove(object_to_destroy)
                            # if obstacle.type == Constants.GeneralConstants.BULLET:
                            #     self.collidables.remove(obstacle)


        # for collidable in self.collidables:
        #     for collide_target in self.collide_targets:
        #         # Good for round objects
        #         if (
        #             math.hypot((collide_target.x_coordinate - collidable.x_coordinate),
        #                        (collide_target.y_coordinate - collidable.y_coordinate))
        #                        <= (collidable.x_size + collide_target.x_size)/2
        #         ):
        #
        #                     DamageProcessor.process_damage(collidable, collide_target)
        #                     self.object_processor.destroy_entity(collidable, collide_target)
        #                     self.collidables.remove(collidable)
        #
        #
        # bullet_collidables = self.collide_targets.copy()
        # bullet_collidables.extend(self.collidables)
        # if bullet_collidables:
        #     print(len(bullet_collidables))
        #
        #
        # for bullet in self.bullets:
        #     for collide_target in bullet_collidables:
        #         # TODO: algorythm is bad
        #         if (
        #             math.hypot((collide_target.x_coordinate - bullet.x_coordinate),
        #                        (collide_target.y_coordinate - bullet.y_coordinate))
        #                        <= (collide_target.x_size + bullet.x_size)/2
        #         ):
        #             print("BOOM")

        # Bullet cycles. Bullet owner


