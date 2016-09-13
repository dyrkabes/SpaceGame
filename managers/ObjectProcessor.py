import random

import Constants
from OuterSpaceObject import OuterSpaceObject
from spaceObjects.Explosion import Explosion
from spaceObjects.PathPoint import PathPoint
from spaceObjects.Ship import Ship
from view.InterfaceElements.InfoLabel import InfoLabel


class ObjectProcessor:
    def __init__(self):
        self.current_system = None
        self.resource_manager = None
        self.collision_manager = None
        self.zoom = None

    def init_current_system(self, current_system):
        self.current_system = current_system

    def init_resource_manager(self, resource_manager, zoom):
        self.resource_manager = resource_manager
        self.zoom = zoom

    def init_collision_manager(self, collision_manager):
        self.collision_manager = collision_manager

    def create_entity(self, entity):
        """
        Creates entity. For now entities instance is given outside the procedure
        that should be fixed i think
        :param entity: created entity
        :return: None. Adds entity to all necessary lists and performs other actions
        """
        self.current_system.append_entity(entity)
        self.resource_manager.set_image(entity, entity.get_images_names())
        if (entity.collidable_type == Constants.CollidableTypes.COLLIDABLE
                or entity.collidable_type == Constants.CollidableTypes.COLLIDE_TARGET
                or entity.collidable_type == Constants.CollidableTypes.BULLET):
            self.collision_manager.process_entity(entity)

        # Initiation zoom
        self.zoom(entity)
        if entity.type == Constants.GeneralConstants.STAR:
            self.current_system.star = entity

        # procedures for destroying entity in future
        entity.collision_manager_remove = self.collision_manager.remove_entity
        entity.object_processor_remove = self.destroy_entity

        if entity.type == Constants.GeneralConstants.SHIP:
            Ship.id += 1


    def destroy_entity(self, entity, collide_target=None):
        """
        Destroys entity and perfoms necessary actions
        :param entity: entity to destroy
        :param collide_target: needed in case it is a comet
        :return: None. Removes the entity from lists and creates chunks/explosion
        """
        self.current_system.remove_entity(entity)
        self.create_chunks(entity, collide_target)
        self.create_explosion(entity)

    def create_chunks(self, entity, collide_target):
        """
        Procedure for destroying a comet
        :param entity: comet
        :param collide_target:
        :return: None. Creates OuterSpaceObjects
        """
        if (entity.type == Constants.GeneralConstants.COMET):
            if (collide_target.type != Constants.GeneralConstants.STAR):
                weight = 0
                while weight < entity.weight:
                    x_coordinate = random.randint(round(entity.x_coordinate - entity.x_size),
                                                  round(entity.x_coordinate + entity.x_size)
                                                  )
                    y_coordinate = random.randint(round(entity.y_coordinate - entity.y_size),
                                                  round(entity.y_coordinate + entity.y_size)
                                                  )
                    low_border = entity.weight // 10
                    top_border = entity.weight - weight

                    if low_border < top_border:
                        chunk_weight = random.randint(entity.weight // 10,
                                                  entity.weight - weight)
                    else:
                        chunk_weight = top_border
                    self.create_entity(OuterSpaceObject(x_coordinate,
                                                                    y_coordinate,
                                                                    2,
                                                                    2,
                                                                    chunk_weight)
                                                   )
                    weight += chunk_weight

    def create_explosion(self, entity):
        if entity.type == Constants.GeneralConstants.BULLET:
            if not entity.worn_out:
                self.create_entity(Explosion(entity.x_coordinate, entity.y_coordinate))

    def create_path(self, path):
        """
        Adds path points to the current system's list
        :param path: calculated path with it's points
        :return: None. Appends points to the list
        """
        for point in path.points:
            new_point = PathPoint(point)
            self.current_system.append_entity(new_point)
            new_point.set_image(self.resource_manager)
            self.resource_manager.zoom(new_point)

    def erase_path(self):
        """
        :return: Delets all the path points
        """
        for entity in self.current_system.entities:
            if entity.type == Constants.GeneralConstants.POINT:
                self.current_system.entities.remove(entity)

    def create_info_label(self, target, message, decrease_messages_count):
        """
        Creates info label
        :param target: info label emitter
        :param message: text
        :param decrease_messages_count: function for the time when info label is destroyed
        :return: None. Creates new info label
        """
        info_label = InfoLabel(target.x_coordinate + target.state_manager.message_manager.get_offset_x(),
                               target.y_coordinate + target.state_manager.message_manager.get_offset_y(),
                               decrease_messages_count)
        target.state_manager.message_manager.add_message()
        self.create_entity(info_label)
        info_label.set_text(message)







