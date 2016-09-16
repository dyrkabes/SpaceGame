from Entity import Entity
import Constants

class OuterSpaceObject(Entity):
    def __init__(self, x_coordinate, y_coordinate, x_size, y_size, weight, type=Constants.GeneralConstants.OUTER_SPACE_OBJECT):
         Entity.__init__(self,x_coordinate, y_coordinate, x_size, y_size, type)
         self.weight = weight

         # self.type = Constants.GeneralConstants.OUTER_SPACE_OBJECT

         self.rotatable = False

         self.collidable_type = Constants.CollidableTypes.NON_COLLIDABLE

         self.component_type = Constants.ShipConstants.GRABBER

         self.images_names = ["outer_space_object.png"]


