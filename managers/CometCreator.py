import random

from spaceObjects.Comet import Comet


class CometCreator:
    @staticmethod
    def create_comet(current_system, create_comet):
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
        create_comet(Comet(x_coordinate,
                     y_coordinate,
                     size, size,
                     x_speed, y_speed,
                     weight)
                     )


