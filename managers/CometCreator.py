import random

from spaceObjects.Comet import Comet


class CometCreator:
    """
    Creates comets.
    Soon will head them to the center not a random direction
    """
    @staticmethod
    def create_comet(current_system, create_entity):
        """
        Creates comes
        :param current_system: currents system with it's dimensions
        :param create_entity: ObjectProcessor's creating procedure
        :return: None. Creates a new comet
        """
        side = random.randint(0,1)
        if side:
            y_coordinate = random.choice([0, current_system.y_dimension])
            x_coordinate = random.randint(0, current_system.x_dimension)
        else:
            x_coordinate = random.choice([0, current_system.x_dimension])
            y_coordinate = random.randint(0, current_system.y_dimension)
        size = random.randint(3,5)
        x_speed = random.randint(1, 4)/random.randint(8, 15) * random.choice([-1, 1])
        y_speed = random.randint(1, 4)/random.randint(8, 15) * random.choice([-1, 1])
        weight = random.randint(10, 120)
        create_entity(Comet(x_coordinate,
                     y_coordinate,
                     size, size,
                     x_speed, y_speed,
                     weight)
                     )


