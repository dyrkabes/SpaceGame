import random

import Constants
from OuterSpaceObject import OuterSpaceObject
from spaceObjects.Explosion import Explosion
from spaceObjects.PathPoint import PathPoint
from spaceObjects.Ship import Ship
from view.InterfaceElements.InfoLabel import InfoLabel


class ObjectProcessor:
    def __init__(self):
        pass

    def init_current_system(self, current_system):
        self.current_system = current_system

    def init_resource_manager(self, resource_manager, zoom):
        self.resource_manager = resource_manager
        self.zoom = zoom

    def init_collision_manager(self, collision_manager):
        self.collision_manager = collision_manager

    def create_entity(self, entity):
        self.current_system.append_entity(entity)
        self.resource_manager.set_image(entity, entity.get_images_names())
        if (entity.collidable_type == Constants.CollidableTypes.COLLIDABLE
                or entity.collidable_type == Constants.CollidableTypes.COLLIDE_TARGET
                or entity.collidable_type == Constants.CollidableTypes.BULLET):
            self.collision_manager.process_entity(entity)
        self.zoom(entity)
        if entity.type == Constants.GeneralConstants.STAR:
            self.current_system.star = entity
        entity.collision_manager_remove = self.collision_manager.remove_entity
        entity.object_processor_remove = self.destroy_entity
        if entity.type == Constants.GeneralConstants.SHIP:
            Ship.id += 1
            # if self.
            # TODO: In controller ship needs to be destroyed as well


    def destroy_entity(self, entity, collide_target=None):
        # curr system remove
        self.current_system.remove_entity(entity)
        self.create_chunks(entity, collide_target)
        self.create_explosion(entity)

    def create_chunks(self, entity, collide_target):
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
        for point in path.points:
            new_point = PathPoint(point)
            self.current_system.append_entity(new_point)
            new_point.set_image(self.resource_manager)
            self.resource_manager.zoom(new_point)

    def erase_path(self):
        for entity in self.current_system.entities:
            if entity.type == Constants.GeneralConstants.POINT:
                self.current_system.entities.remove(entity)

    def create_info_label(self, target, message, decrease_messages_count):
        info_label = InfoLabel(target.x_coordinate + target.state_manager.message_manager.get_offset_x(),
                               target.y_coordinate + target.state_manager.message_manager.get_offset_y(),
                               decrease_messages_count)
        target.state_manager.message_manager.add_message()
        self.create_entity(info_label)
        info_label.set_text(message)







