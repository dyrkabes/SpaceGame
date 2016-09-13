import random


class MovementAnalyzer:
    """
    Class manages movement of AI ships
    In the future it will be combined with some sort of need analyzer
    so the destination will be meaningful
    """
    @staticmethod
    def get_destination(ship):
        """
        Creates new destination for the ship
        :param ship: ship to process movement analysis on
        :return: None. Sets new destination to the ship
        """
        if (not ship.x_movement_speed and
                not ship.y_movement_speed and not ship.player_ship):
            ship.x_destination = random.randint(-5, 200)
            ship.y_destination = random.randint(-5, 200)
